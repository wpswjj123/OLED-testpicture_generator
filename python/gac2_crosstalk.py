#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GAC-2_crosstalk.m 的 Python 版。

生成 REF.bmp / H.bmp / V.bmp，尺寸 3120 x 2080，白色底（255），线条灰阶 127。
输出目录默认 output/gac2_crosstalk/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3120, 2080
BG = 255
LINE = 127


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
    d = out_dir("gac2_crosstalk")
    background = np.full((HEIGHT, WIDTH, 3), BG, dtype=np.uint8)

    wb = int(WIDTH / 3)
    hb = int(HEIGHT / 3)
    wc = int(WIDTH / 6)
    hc = int(HEIGHT / 6)

    # REF 图：竖列 + 横列
    img = background.copy()
    img[hb:2 * hb, :] = LINE
    img[:, wb:2 * wb] = LINE
    save(img, d, "REF.bmp")

    # H 图：上、下横纹 + 竖条纹
    img = background.copy()
    img[0:hc, :] = LINE
    img[HEIGHT - hc:HEIGHT, :] = LINE
    img[:, wb:2 * wb] = LINE
    save(img, d, "H.bmp")

    # V 图：左、右竖纹 + 横纹
    img = background.copy()
    img[:, 0:wc] = LINE
    img[:, WIDTH - wc:WIDTH] = LINE
    img[hb:2 * hb, :] = LINE
    save(img, d, "V.bmp")


if __name__ == "__main__":
    main()
