#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LCB_crosstalk.m 的 Python 版。

生成 REF.png / HINF.png / VINF.png，尺寸 3200 x 2000，灰色底 186。
输出目录默认 output/lcb_crosstalk/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3200, 2000
BG = 186


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
    d = out_dir("lcb_crosstalk")
    background = np.full((HEIGHT, WIDTH, 3), BG, dtype=np.uint8)

    wb = int(WIDTH / 3)
    hb = int(HEIGHT / 3)

    # REF 图：四角黑块
    img = background.copy()
    img[0:hb, 0:wb] = 0
    img[HEIGHT - hb:HEIGHT, 0:wb] = 0
    img[0:hb, WIDTH - wb:WIDTH] = 0
    img[HEIGHT - hb:HEIGHT, WIDTH - wb:WIDTH] = 0
    save(img, d, "REF.png")

    # HINF 图：居中的左、右黑块
    img = background.copy()
    r0 = int(HEIGHT / 2) - hb + 1          # 1-based 起点
    r1 = int(HEIGHT / 2) + hb              # 1-based 终点（含）
    img[r0 - 1:r1, 0:wb] = 0
    img[r0 - 1:r1, WIDTH - wb:WIDTH] = 0
    save(img, d, "HINF.png")

    # VINF 图：居中的上、下黑块
    img = background.copy()
    c0 = int(WIDTH / 2) - wb + 1
    c1 = int(WIDTH / 2) + wb
    img[0:hb, c0 - 1:c1] = 0
    img[HEIGHT - hb:HEIGHT, c0 - 1:c1] = 0
    save(img, d, "VINF.png")


if __name__ == "__main__":
    main()
