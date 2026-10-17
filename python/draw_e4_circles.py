#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""画图code_E4-大小圆_matlab.m 的 Python 版。

两组输出，尺寸均为 3200 x 2000：
  1) 纯色图  C1.png ~ C46.png
  2) 白底 + 大圆（面积占比 30%）C1_0.3.png ~ C46_0.3.png
输出目录默认 output/draw_e4_circles/。
"""
import math
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3200, 2000

COLORS = [
    (255, 255, 255),
    (230, 230, 230),
    (209, 209, 209),
    (186, 186, 186),
    (158, 158, 158),
    (0, 0, 0),
    (115, 82, 66),
    (194, 150, 130),
    (94, 122, 156),
    (89, 107, 66),
    (130, 128, 176),
    (99, 189, 168),
    (217, 120, 41),
    (74, 92, 163),
    (194, 84, 97),
    (92, 61, 107),
    (158, 186, 64),
    (230, 161, 46),
    (51, 61, 150),
    (71, 148, 71),
    (176, 48, 59),
    (237, 199, 33),
    (186, 84, 145),
    (0, 133, 163),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 255, 255),
    (255, 0, 255),
    (255, 255, 0),
    (112, 64, 38),
    (204, 138, 102),
    (255, 199, 153),
    (255, 199, 171),
    (247, 171, 125),
    (199, 140, 92),
    (143, 92, 51),
    (207, 150, 115),
    (161, 87, 33),
    (214, 133, 92),
    (209, 138, 105),
    (250, 153, 115),
    (199, 143, 107),
    (201, 140, 107),
    (204, 143, 105),
    (122, 74, 38),
    (217, 140, 94),
]


def out_dir(name):
    root = os.environ.get("OUTPUT_DIR", "output")
    path = os.path.join(root, name)
    os.makedirs(path, exist_ok=True)
    return path


def main():
    d = out_dir("draw_e4_circles")

    # 1) 纯色图
    for i, color in enumerate(COLORS, start=1):
        img = np.empty((HEIGHT, WIDTH, 3), dtype=np.uint8)
        img[:, :] = color
        path = os.path.join(d, "C%d.png" % i)
        Image.fromarray(img, "RGB").save(path)
        print("已生成:", path)

    # 2) 白底 + 大圆（面积占 30%）
    circle_area = 0.3 * WIDTH * HEIGHT
    circle_radius = math.sqrt(circle_area / math.pi)

    # 网格坐标（1-based 与 MATLAB 对齐）
    xs = np.arange(1, WIDTH + 1, dtype=np.float64)
    ys = np.arange(1, HEIGHT + 1, dtype=np.float64)
    grid_x, grid_y = np.meshgrid(xs, ys)          # HEIGHT x WIDTH
    distance = np.sqrt((grid_x - WIDTH / 2.0) ** 2 + (grid_y - HEIGHT / 2.0) ** 2)
    mask = distance <= circle_radius

    for i, color in enumerate(COLORS, start=1):
        img = np.full((HEIGHT, WIDTH, 3), 255, dtype=np.uint8)
        img[mask] = color
        path = os.path.join(d, "C%d_0.3.png" % i)
        Image.fromarray(img, "RGB").save(path)
        print("已生成:", path)


if __name__ == "__main__":
    main()
