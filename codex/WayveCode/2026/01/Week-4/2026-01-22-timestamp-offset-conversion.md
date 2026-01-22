# Timestamp offset → timestamp_unixus (Zak branch)

## Overview
Documented the offset-to-absolute timestamp conversion logic used in Zak's branch for `timestamp_unixus` lookups, with notes for microsecond offsets.

## Source
- `origin/zmurez/trt:wayve/ai/language/action/demo/demo.py#get_corrected_timestamp_unixus`

## Code snippet (Zak branch)
```python
def get_corrected_timestamp_unixus(run_id: str, timestamp_or_offset_str: str) -> int:
    timestamp_unixus = int(timestamp_or_offset_str)
    if timestamp_unixus <= 1e10:
        timestamp_unixus_since_start_of_run = int(float(timestamp_or_offset_str) * 1e6)
        time_table_df = get_run_df(run_id)
        index = (time_table_df["timestamp_offset"] - timestamp_unixus_since_start_of_run).abs().idxmin()
        timestamp_unixus = int(time_table_df.loc[index]["timestamp_unixus"])
    return timestamp_unixus
```

## Notes
- The code treats small values as offsets since run start and snaps to the nearest recorded `timestamp_unixus`.
- If your offsets are already in **microseconds**, skip the `* 1e6` conversion and match directly against `timestamp_offset`.

## Standalone script (inline)
```python
#!/usr/bin/env python3
import argparse
import asyncio
import os
from typing import Iterable, List

import numpy as np

import wayve.ai.lib.data.storage.binary_keys as BK
from wayve.ai.language.action.interfaces import FRAME_PATH
from wayve.ai.lib.data.pipes.utils import cache_and_load_npz_file_async
from wayve.ai.lib.map_async import get_loop


def _load_timestamps(run_id: str) -> np.ndarray:
    meta_data = asyncio.run_coroutine_threadsafe(
        cache_and_load_npz_file_async(run_id, os.path.join(FRAME_PATH, "metadata"), "~/.cache/frame_meta_data"),
        get_loop(),
    ).result()
    key = f"{run_id}{BK.FRAMES_METADATA_TIMESTAMP_KEY_SUFFIX}"
    return np.sort(meta_data[key])


def _resolve_offsets(
    timestamps_unixus: np.ndarray,
    offsets: Iterable[float],
    offset_unit: str,
) -> List[int]:
    if offsets is None:
        return []
    offsets = list(offsets)
    if not offsets:
        return []

    first_ts = int(timestamps_unixus[0])
    offset_us_values = []
    for value in offsets:
        if value >= 1e12:
            offset_us_values.append(int(value) - first_ts)
        elif offset_unit == "seconds":
            offset_us_values.append(int(value * 1e6))
        else:
            offset_us_values.append(int(value))

    timestamp_offset = timestamps_unixus - first_ts
    resolved = []
    for offset_us in offset_us_values:
        idx = int(np.abs(timestamp_offset - offset_us).argmin())
        resolved.append(int(timestamps_unixus[idx]))
    return resolved


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Convert offsets since run start to nearest timestamp_unixus using run metadata. "
            "If a value looks like absolute unix microseconds (>= 1e12), it is treated as absolute."
        )
    )
    parser.add_argument("run_id", help="Run ID (e.g., fme10010/2024-12-12--05-22-42--...)")
    parser.add_argument(
        "offsets",
        nargs="+",
        type=float,
        help="Offsets since run start, or absolute timestamp_unixus values.",
    )
    parser.add_argument(
        "--offset-unit",
        choices=("microseconds", "seconds"),
        default="microseconds",
        help="Unit for offset inputs when values are not absolute (default: microseconds).",
    )
    args = parser.parse_args()

    timestamps_unixus = _load_timestamps(args.run_id)
    resolved = _resolve_offsets(timestamps_unixus, args.offsets, args.offset_unit)

    for offset_value, timestamp_unixus in zip(args.offsets, resolved):
        print(f"{offset_value} -> {timestamp_unixus}")


if __name__ == "__main__":
    main()
```
