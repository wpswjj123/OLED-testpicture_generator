#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HCS_crosstalk.m 的 Python 版。

生成 V1~V4.png / H1~H4.png，尺寸 3200 x 3200，灰色底 128。
输出目录默认 output/hcs_crosstalk/。
"""
import os

import numpy as np
from PIL import Image

WIDTH, HEIGHT = 3200, 3200
BG = 128
PIXEL_SIZE = 112


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
    d = out_dir("hcs_crosstalk")

    n1 = int(WIDTH / 3)
    m1 = int(HEIGHT / 3)
    b = int(9 * 1000 / PIXEL_SIZE)
    half_h = int(WIDTH / 2)
    half_v = int(HEIGHT / 2)
    n2 = int(WIDTH / 6)
    m2 = int(HEIGHT / 6)

    def new_img():
        return np.full((HEIGHT, WIDTH, 3), BG, dtype=np.uint8)

    # V1
    img = new_img()
    img[0:m1, half_h - b:half_h - b + n1] = 0
    img[HEIGHT - m1:HEIGHT, half_h - b:half_h - b + n1] = 0
    save(img, d, "V1.png")

    # V2
    img = new_img()
    img[0:m1, half_h + b:half_h + b + n1] = 0
    img[HEIGHT - m1:HEIGHT, half_h + b:half_h + b + n1] = 0
    save(img, d, "V2.png")

    # V3
    img = new_img()
    img[0:m1, n2 + b:n2 + b + n1] = 0
    img[HEIGHT - m1:HEIGHT, n2 + b:n2 + b + n1] = 0
    save(img, d, "V3.png")

    # V4
    img = new_img()
    img[0:m1, n2 - b:n2 - b + n1] = 0
    img[HEIGHT - m1:HEIGHT, n2 - b:n2 - b + n1] = 0
    save(img, d, "V4.png")

    # H1
    img = new_img()
    img[half_v - b:half_v - b + m1, 0:n1] = 0
    img[half_v - b:half_v - b + m1, WIDTH - n1:WIDTH] = 0
    save(img, d, "H1.png")

    # H2
    img = new_img()
    img[half_v + b:half_v + b + m1, 0:n1] = 0
    img[half_v + b:half_v + b + m1, WIDTH - n1:WIDTH] = 0
    save(img, d, "H2.png")

    # H3
    img = new_img()
    img[m2 + b:half_v + b, 0:n1] = 0
    img[m2 + b:half_v + b, WIDTH - n1:WIDTH] = 0
    save(img, d, "H3.png")

    # H4
    img = new_img()
    img[m2 - b:half_v - b, 0:n1] = 0
    img[m2 - b:half_v - b, WIDTH - n1:WIDTH] = 0
    save(img, d, "H4.png")


if __name__ == "__main__":
    main()
