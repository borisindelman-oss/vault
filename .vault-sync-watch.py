#!/usr/bin/env python3
"""Event-based vault sync using Linux inotify (no external deps)."""
import ctypes
import ctypes.util
import errno
import os
import select
import struct
import subprocess
import sys
import time

VAULT = "/home/borisindelman/git/vault"
SYNC_SCRIPT = os.path.join(VAULT, ".vault-sync.sh")
DEBOUNCE_SECONDS = 2.0
PULL_INTERVAL_SECONDS = 60.0

# Edit these if you want to ignore additional paths
IGNORE_DIR_NAMES = {".git"}
IGNORE_FILE_NAMES = {"workspace.json", "workspace.json.tmp"}

IN_ACCESS = 0x00000001
IN_MODIFY = 0x00000002
IN_ATTRIB = 0x00000004
IN_CLOSE_WRITE = 0x00000008
IN_MOVED_FROM = 0x00000040
IN_MOVED_TO = 0x00000080
IN_CREATE = 0x00000100
IN_DELETE = 0x00000200
IN_DELETE_SELF = 0x00000400
IN_MOVE_SELF = 0x00000800
IN_ISDIR = 0x40000000

WATCH_MASK = (
    IN_CLOSE_WRITE
    | IN_CREATE
    | IN_DELETE
    | IN_MOVED_TO
    | IN_ATTRIB
    | IN_MODIFY
)

EVENT_STRUCT = "iIII"
EVENT_SIZE = struct.calcsize(EVENT_STRUCT)


def should_ignore(path: str) -> bool:
    parts = path.split(os.sep)
    if any(p in IGNORE_DIR_NAMES for p in parts if p):
        return True
    base = os.path.basename(path)
    if base in IGNORE_FILE_NAMES:
        return True
    return False


def get_libc():
    libc_path = ctypes.util.find_library("c")
    if not libc_path:
        raise RuntimeError("libc not found")
    return ctypes.CDLL(libc_path, use_errno=True)


def add_watch(fd, libc, path):
    if should_ignore(path):
        return None
    try:
        wd = libc.inotify_add_watch(fd, path.encode(), WATCH_MASK)
    except Exception:
        return None
    if wd < 0:
        return None
    return wd


def add_watches_recursive(fd, libc, root, wd_to_path):
    for dirpath, dirnames, _ in os.walk(root):
        # Prune ignored dirs in-place
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIR_NAMES]
        if should_ignore(dirpath):
            continue
        wd = add_watch(fd, libc, dirpath)
        if wd is not None:
            wd_to_path[wd] = dirpath


def run_sync():
    try:
        subprocess.run([SYNC_SCRIPT], check=False)
    except Exception as exc:
        print(f"[vault-sync] failed to run sync: {exc}", file=sys.stderr)


def main():
    if not os.path.isdir(VAULT):
        print(f"vault not found: {VAULT}", file=sys.stderr)
        return 1
    if not os.path.isfile(SYNC_SCRIPT):
        print(f"sync script not found: {SYNC_SCRIPT}", file=sys.stderr)
        return 1

    libc = get_libc()
    libc.inotify_init1.restype = ctypes.c_int
    libc.inotify_add_watch.restype = ctypes.c_int

    fd = libc.inotify_init1(0)
    if fd < 0:
        err = ctypes.get_errno()
        raise OSError(err, os.strerror(err))

    wd_to_path = {}
    add_watches_recursive(fd, libc, VAULT, wd_to_path)

    # Initial sync on start
    run_sync()
    next_periodic_sync = time.time() + PULL_INTERVAL_SECONDS

    next_sync_at = None

    while True:
        timeout = None
        if next_sync_at is not None:
            timeout = max(0.0, next_sync_at - time.time())
        if next_periodic_sync is not None:
            periodic_timeout = max(0.0, next_periodic_sync - time.time())
            timeout = periodic_timeout if timeout is None else min(timeout, periodic_timeout)
        rlist, _, _ = select.select([fd], [], [], timeout)
        if rlist:
            try:
                data = os.read(fd, 4096)
            except OSError as exc:
                if exc.errno == errno.EINTR:
                    continue
                raise
            offset = 0
            while offset + EVENT_SIZE <= len(data):
                wd, mask, _, name_len = struct.unpack_from(EVENT_STRUCT, data, offset)
                offset += EVENT_SIZE
                name_bytes = data[offset : offset + name_len]
                offset += name_len
                name = name_bytes.split(b"\0", 1)[0].decode(errors="ignore")
                base_path = wd_to_path.get(wd, VAULT)
                full_path = os.path.join(base_path, name) if name else base_path

                # Update watches for new directories
                if mask & IN_ISDIR and mask & (IN_CREATE | IN_MOVED_TO):
                    if os.path.isdir(full_path) and not should_ignore(full_path):
                        new_wd = add_watch(fd, libc, full_path)
                        if new_wd is not None:
                            wd_to_path[new_wd] = full_path

                # Remove watches for deleted directories
                if mask & (IN_DELETE_SELF | IN_MOVE_SELF):
                    if wd in wd_to_path:
                        wd_to_path.pop(wd, None)

                if not should_ignore(full_path):
                    next_sync_at = time.time() + DEBOUNCE_SECONDS
        else:
            now = time.time()
            did_sync = False
            if next_sync_at is not None and now >= next_sync_at:
                run_sync()
                next_sync_at = None
                did_sync = True
            if next_periodic_sync is not None and now >= next_periodic_sync:
                if not did_sync:
                    run_sync()
                next_periodic_sync = time.time() + PULL_INTERVAL_SECONDS
            elif did_sync:
                next_periodic_sync = time.time() + PULL_INTERVAL_SECONDS


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)
