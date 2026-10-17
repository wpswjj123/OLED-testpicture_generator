#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""oppo41color.m 的 Python 版。

生成 41 张纯色图 C1.png ~ C41.png，尺寸 3200 x 2000。
输出目录默认 output/oppo41color/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3200, 2000

COLORS = [
    (255, 255, 255),
    (255, 0, 0),
    (255, 126, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 130, 255),
    (0, 0, 255),
    (158, 0, 255),
    (255, 0, 255),
    (255, 0, 151),
    (255, 73, 73),
    (255, 148, 88),
    (255, 255, 124),
    (110, 255, 110),
    (125, 255, 255),
    (93, 150, 255),
    (77, 77, 255),
    (170, 86, 255),
    (255, 100, 255),
    (255, 83, 163),
    (255, 114, 114),
    (255, 169, 134),
    (255, 255, 174),
    (160, 255, 160),
    (176, 255, 255),
    (140, 174, 255),
    (120, 120, 255),
    (186, 132, 255),
    (255, 149, 255),
    (255, 128, 180),
    (255, 164, 164),
    (255, 202, 185),
    (255, 255, 216),
    (206, 255, 206),
    (218, 255, 255),
    (190, 207, 255),
    (171, 171, 255),
    (211, 182, 255),
    (255, 197, 255),
    (255, 178, 206),
]


def out_dir(name):
    root = os.environ.get("OUTPUT_DIR", "output")
    path = os.path.join(root, name)
    os.makedirs(path, exist_ok=True)
    return path


def main():
    d = out_dir("oppo41color")
    for i, color in enumerate(COLORS, start=1):
        img = np.empty((HEIGHT, WIDTH, 3), dtype=np.uint8)
        img[:, :] = color
        path = os.path.join(d, "C%d.png" % i)
        Image.fromarray(img, "RGB").save(path)
        print("已生成:", path)


if __name__ == "__main__":
    main()
