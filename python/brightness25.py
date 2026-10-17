#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""偷亮25图code.m 的 Python 版。

生成 25 张纯色图 C1.png ~ C25.png，尺寸 3200 x 2000。
输出目录默认 output/brightness25/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3200, 2000

COLORS = [
    (48, 0, 0),
    (96, 0, 0),
    (0, 48, 0),
    (48, 48, 0),
    (96, 48, 0),
    (0, 96, 0),
    (48, 96, 0),
    (96, 96, 0),
    (0, 0, 48),
    (48, 0, 48),
    (96, 0, 48),
    (0, 48, 48),
    (48, 48, 48),
    (96, 48, 48),
    (0, 96, 48),
    (48, 96, 48),
    (96, 96, 48),
    (0, 0, 96),
    (48, 0, 96),
    (96, 0, 96),
    (0, 48, 96),
    (48, 48, 96),
    (96, 48, 96),
    (0, 96, 96),
    (48, 96, 96),
]


def out_dir(name):
    root = os.environ.get("OUTPUT_DIR", "output")
    path = os.path.join(root, name)
    os.makedirs(path, exist_ok=True)
    return path


def main():
    d = out_dir("brightness25")
    for i, color in enumerate(COLORS, start=1):
        img = np.empty((HEIGHT, WIDTH, 3), dtype=np.uint8)
        img[:, :] = color
        path = os.path.join(d, "C%d.png" % i)
        Image.fromarray(img, "RGB").save(path)
        print("已生成:", path)


if __name__ == "__main__":
    main()
