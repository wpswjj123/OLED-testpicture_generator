#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""img_resize2.m（img_resize_demo）的 Python 版。

读取图片分辨率，并缩放到任意指定分辨率。

用法:
    python img_resize2.py in.jpg 500 300 stretch
    python img_resize2.py in.jpg 500 300 fit  out.png 255,255,255
    python img_resize2.py in.jpg 500 300 crop out.png

mode:
    stretch  直接拉伸铺满（可能变形）
    fit      等比缩放 + 居中留边（不变形，有留边）
    crop     等比缩放 + 居中裁剪（不变形，无留边）
"""
import argparse
import os
import sys

from PIL import Image


def _parse_bg(bg):
    if bg is None:
        return (255, 255, 255)
    if isinstance(bg, (list, tuple)):
        vals = [int(v) for v in bg]
    else:
        vals = [int(v) for v in str(bg).split(",")]
    if len(vals) == 1:
        return tuple(vals * 3)
    return tuple(vals[:3])


def img_resize_demo(input_path, W, H, mode="stretch", out_path=None, bg=None):
    """读取图片并缩放到严格 W x H。"""
    bg = _parse_bg(bg)

    img = Image.open(input_path)
    w, h = img.size
    print("原始分辨率: %d × %d" % (w, h))

    mode = (mode or "stretch").lower()

    if mode == "stretch":
        out = img.resize((W, H), Image.BILINEAR)
    elif mode == "fit":
        scale = min(W / w, H / h)
        nw = max(1, round(w * scale))
        nh = max(1, round(h * scale))
        tmp = img.resize((nw, nh), Image.BILINEAR)
        out = Image.new("RGB", (W, H), bg)
        out.paste(tmp, ((W - nw) // 2, (H - nh) // 2))
    elif mode == "crop":
        scale = max(W / w, H / h)
        nw = max(W, round(w * scale))
        nh = max(H, round(h * scale))
        tmp = img.resize((nw, nh), Image.BILINEAR)
        r0 = (nh - H) // 2
        c0 = (nw - W) // 2
        out = tmp.crop((c0, r0, c0 + W, r0 + H))
    else:
        raise ValueError("未知模式: %s（可选 stretch / fit / crop）" % mode)

    if not out_path:
        p, n = os.path.split(input_path)
        base, _ = os.path.splitext(n)
        out_path = os.path.join(p, "%s_%dx%d.png" % (base, W, H))

    out.save(out_path)
    ow, oh = out.size
    print("输出分辨率: %d × %d  ->  %s" % (ow, oh, out_path))
    return out_path


def main(argv=None):
    ap = argparse.ArgumentParser(description="图片缩放（demo / stretch / fit / crop）")
    ap.add_argument("input", help="输入图片路径")
    ap.add_argument("W", type=int, help="目标宽度")
    ap.add_argument("H", type=int, help="目标高度")
    ap.add_argument("mode", nargs="?", default="stretch",
                    choices=["stretch", "fit", "crop"])
    ap.add_argument("out", nargs="?", default=None, help="输出路径（可选）")
    ap.add_argument("bg", nargs="?", default=None, help="fit 模式留边颜色，如 255,255,255")
    args = ap.parse_args(argv)

    img_resize_demo(args.input, args.W, args.H, args.mode, args.out, args.bg)
    return 0


if __name__ == "__main__":
    sys.exit(main())