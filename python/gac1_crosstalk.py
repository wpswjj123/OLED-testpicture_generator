#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GAC-1_crosstalk.m 的 Python 版。

生成 REF.bmp / HINF.bmp / VINF.bmp，尺寸 3120 x 2080，灰色底 127。
输出目录默认 output/gac1_crosstalk/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3120, 2080
BG = 127


def out_dir(name):
    root = os.environ.get("OUTPUT_DIR", "output")
    path = os.path.join(root, name)
    os.makedirs(path, exist_ok=True)
    return path


def save(img, d, name):
    path = os.path.join(d, name)
    Image.fromarray(img, "RGB").save(path)
    print("已生成:", path)


def main():
    d = out_dir("gac1_crosstalk")
    background = np.full((HEIGHT, WIDTH, 3), BG, dtype=np.uint8)

    wb = int(WIDTH / 3)
    hb = int(HEIGHT / 3)

    # REF 图：四角黑块
    img = background.copy()
    img[0:hb, 0:wb] = 0
    img[HEIGHT - hb:HEIGHT, 0:wb] = 0
    img[0:hb, WIDTH - wb:WIDTH] = 0
    img[HEIGHT - hb:HEIGHT, WIDTH - wb:WIDTH] = 0
    save(img, d, "REF.bmp")

    # HINF 图：左中、右中黑块
    img = background.copy()
    img[hb:2 * hb, 0:wb] = 0
    img[hb:2 * hb, WIDTH - wb:WIDTH] = 0
    save(img, d, "HINF.bmp")

    # VINF 图：上中、下中黑块
    img = background.copy()
    img[0:hb, wb:2 * wb] = 0
    img[HEIGHT - hb:HEIGHT, wb:2 * wb] = 0
    save(img, d, "VINF.bmp")


if __name__ == "__main__":
    main()
