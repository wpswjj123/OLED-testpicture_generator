#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gamma画图code.m 的 Python 版。

生成 4 组灰阶图，每组 256 张（0~255），尺寸 2760 x 1256：
  W0~W255.png  白（R=G=B=j）
  R0~R255.png  红（R=j）
  G0~G255.png  绿（G=j）
  B0~B255.png  蓝（B=j）
输出目录默认 output/gamma/{W,R,G,B}/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 2760, 1256


def out_dir(*parts):
    root = os.environ.get("OUTPUT_DIR", "output")
    path = os.path.join(root, *parts)
    os.makedirs(path, exist_ok=True)
    return path


def save_gray(d, prefix, j):
    img = np.full((HEIGHT, WIDTH, 3), j, dtype=np.uint8)
    path = os.path.join(d, "%s%d.png" % (prefix, j))
    Image.fromarray(img, "RGB").save(path)


def main():
    d_w = out_dir("gamma", "W")
    d_r = out_dir("gamma", "R")
    d_g = out_dir("gamma", "G")
    d_b = out_dir("gamma", "B")

    for j in range(256):
        save_gray(d_w, "W", j)
        save_gray(d_r, "R", j)
        save_gray(d_g, "G", j)
        save_gray(d_b, "B", j)
        if j % 32 == 0:
            print("已生成灰阶 %d/255" % j)

    print("完成：共生成 4 x 256 张图。")


if __name__ == "__main__":
    main()
