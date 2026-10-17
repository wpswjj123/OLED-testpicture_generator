#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OPPO_crosstalk.m 的 Python 版。

生成 GH_1 / G_2~G_5 / H_2 / H_3（.bmp），尺寸 1680 x 2520，灰色底 127。
输出目录默认 output/oppo_crosstalk/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 1680, 2520
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
    d = out_dir("oppo_crosstalk")
    background = np.full((HEIGHT, WIDTH, 3), BG, dtype=np.uint8)

    wb = int(WIDTH / 3)
    hb = int(HEIGHT * 3 / 8)
    hc = int(HEIGHT / 3)

    # 工字型 1：纯底
    save(background.copy(), d, "GH_1.bmp")

    # 工字型 2：上、下白块
    img = background.copy()
    img[0:hb, wb:2 * wb] = 255
    img[HEIGHT - hb:HEIGHT, wb:2 * wb] = 255
    save(img, d, "G_2.bmp")

    # 工字型 3：左、右白块
    img = background.copy()
    img[hb:HEIGHT - hb, 0:wb] = 255
    img[hb:HEIGHT - hb, WIDTH - wb:WIDTH] = 255
    save(img, d, "G_3.bmp")

    # 工字型 4：上、下黑块
    img = background.copy()
    img[0:hb, wb:2 * wb] = 0
    img[HEIGHT - hb:HEIGHT, wb:2 * wb] = 0
    save(img, d, "G_4.bmp")

    # 工字型 5：左、右黑块
    img = background.copy()
    img[hb:HEIGHT - hb, 0:wb] = 0
    img[hb:HEIGHT - hb, WIDTH - wb:WIDTH] = 0
    save(img, d, "G_5.bmp")

    # 回字型 2：中白块
    img = background.copy()
    img[hc:HEIGHT - hc, wb:WIDTH - wb] = 255
    save(img, d, "H_2.bmp")

    # 回字型 3：中黑块
    img = background.copy()
    img[hc:HEIGHT - hc, wb:WIDTH - wb] = 0
    save(img, d, "H_3.bmp")


if __name__ == "__main__":
    main()
