#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2000.m 的 Python 版。

生成 25 张纯色图 E1.png ~ E25.png，尺寸 3120 x 2080。
输出目录默认 output/E2000/，可用环境变量 OUTPUT_DIR 覆盖根目录。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3120, 2080

# RGB 色板（对应 MATLAB circle_color）
COLORS = [
    (255, 255, 255),
    (115, 82, 68),
    (194, 150, 130),
    (98, 122, 157),
    (87, 108, 67),
    (133, 128, 177),
    (103, 189, 170),
    (214, 126, 44),
    (80, 91, 166),
    (193, 90, 99),
    (94, 60, 108),
    (157, 188, 64),
    (224, 163, 46),
    (56, 61, 150),
    (70, 148, 73),
    (175, 54, 60),
    (231, 199, 31),
    (187, 86, 149),
    (8, 133, 161),
    (243, 243, 242),
    (200, 200, 200),
    (160, 160, 160),
    (122, 122, 121),
    (85, 85, 85),
    (52, 52, 52),
]


def out_dir(name):
    root = os.environ.get("OUTPUT_DIR", "output")
    path = os.path.join(root, name)
    os.makedirs(path, exist_ok=True)
    return path


def main():
    d = out_dir("E2000")
    for i, color in enumerate(COLORS, start=1):
        img = np.empty((HEIGHT, WIDTH, 3), dtype=np.uint8)
        img[:, :] = color
        path = os.path.join(d, "E%d.png" % i)
        Image.fromarray(img, "RGB").save(path)
        print("已生成:", path)


if __name__ == "__main__":
    main()
