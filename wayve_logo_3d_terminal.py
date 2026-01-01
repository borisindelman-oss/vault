#!/usr/bin/env python3
"""3D-ish terminal animation of the Wayve logo using ANSI truecolor."""
import argparse
import math
import sys
import time
from pathlib import Path

from PIL import Image

DEFAULT_LOGO = "/home/borisindelman/git/vault/Wayve_logo_Package/DIGITAL/PNG/Wayve_Icon_only_Navy.png"


def load_mask(path: str) -> Image.Image:
    img = Image.open(path).convert("RGBA")
    alpha = img.split()[-1]
    return alpha


def resize_mask(mask: Image.Image, max_w: int, max_h: int) -> Image.Image:
    w, h = mask.size
    scale = min(max_w / w, max_h / h)
    if scale <= 0:
        scale = 1.0
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    return mask.resize((new_w, new_h), Image.LANCZOS)


def shear_mask(mask: Image.Image, skew: int) -> Image.Image:
    if skew == 0:
        return mask
    w, h = mask.size
    out_w = w + abs(skew)
    out = Image.new("L", (out_w, h), 0)
    for y in range(h):
        shift = int(skew * (y / max(1, h - 1) - 0.5))
        row = mask.crop((0, y, w, y + 1))
        x = max(0, shift) if skew > 0 else max(0, shift + abs(skew))
        out.paste(row, (x, y))
    return out


def render_frame(mask: Image.Image, angle: float, cols: int, rows: int, depth: int) -> Image.Image:
    # Base colors (navy-ish)
    base_r, base_g, base_b = 12, 28, 43

    # Rotate around Y by scaling width; skew for perspective
    scale_x = max(0.2, abs(math.cos(angle)))
    skew = int(math.sin(angle) * (mask.size[0] * 0.12))

    scaled = mask.resize((max(1, int(mask.size[0] * scale_x)), mask.size[1]), Image.BICUBIC)
    shaped = shear_mask(scaled, skew)

    # Center on canvas with depth
    canvas = Image.new("RGB", (cols, rows), (0, 0, 0))

    sign = -1 if math.sin(angle) > 0 else 1
    dx = sign
    dy = 1

    x0 = (cols - shaped.size[0]) // 2
    y0 = (rows - shaped.size[1]) // 2

    for z in range(depth, 0, -1):
        shade = 0.35 + 0.65 * (z / depth)
        r = int(base_r * shade)
        g = int(base_g * shade)
        b = int(base_b * shade)
        x = x0 + dx * z
        y = y0 + dy * z
        canvas.paste((r, g, b), (x, y), shaped)

    # Front face brighter
    front = 0.75 + 0.25 * max(0.0, math.cos(angle))
    fr = int(base_r * front + 120)
    fg = int(base_g * front + 120)
    fb = int(base_b * front + 120)
    canvas.paste((min(fr, 255), min(fg, 255), min(fb, 255)), (x0, y0), shaped)

    return canvas


def frame_to_ansi(img: Image.Image) -> str:
    w, h = img.size
    px = img.load()
    lines = []
    for y in range(h):
        line = []
        last_color = None
        for x in range(w):
            r, g, b = px[x, y]
            if r == 0 and g == 0 and b == 0:
                if last_color is not None:
                    line.append("\x1b[0m ")
                    last_color = None
                else:
                    line.append(" ")
                continue
            color = (r, g, b)
            if color != last_color:
                line.append(f"\x1b[38;2;{r};{g};{b}m█")
                last_color = color
            else:
                line.append("█")
        line.append("\x1b[0m")
        lines.append("".join(line))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Wayve logo 3D-ish terminal animation")
    parser.add_argument("--logo", default=DEFAULT_LOGO, help="Path to logo PNG (with alpha)")
    parser.add_argument("--cols", type=int, default=80)
    parser.add_argument("--rows", type=int, default=40)
    parser.add_argument("--fps", type=int, default=20)
    parser.add_argument("--duration", type=int, default=12)
    parser.add_argument("--depth", type=int, default=8)
    args = parser.parse_args()

    logo_path = Path(args.logo)
    if not logo_path.exists():
        print(f"Logo not found: {logo_path}", file=sys.stderr)
        return 1

    mask = load_mask(str(logo_path))

    # Adjust for character aspect ratio (characters are taller than wide)
    max_w = int(args.cols * 0.7)
    max_h = int(args.rows * 0.7)
    mask = resize_mask(mask, max_w, max_h)

    frames = max(1, args.fps * args.duration)

    sys.stdout.write("\x1b[2J\x1b[?25l")
    sys.stdout.flush()

    try:
        for i in range(frames):
            angle = 2 * math.pi * (i / frames)
            frame = render_frame(mask, angle, args.cols, args.rows, args.depth)
            sys.stdout.write("\x1b[H")
            sys.stdout.write(frame_to_ansi(frame))
            sys.stdout.flush()
            time.sleep(1 / args.fps)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\x1b[0m\x1b[?25h\n")
        sys.stdout.flush()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
