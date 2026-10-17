#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""图片分辨率-RGB灰阶提取.m 的 Python 版。

扫描一个文件夹里的 BMP，输出 文件名/宽度/高度/R灰阶/G灰阶/B灰阶 到 CSV。

用法:
    python rgb_gray_extract.py <bmp文件夹> [输出csv]

默认: 输入 ./input，输出 ./灰阶分析结果.csv
"""
import csv
import os
import sys

import numpy as np
from PIL import Image


def rgb_gray_extract(bmp_folder, output_csv):
    files = [f for f in sorted(os.listdir(bmp_folder)) if f.lower().endswith(".bmp")]
    if not files:
        raise SystemExit("未找到任何BMP文件，请检查路径是否正确")

    rows = []
    for name in files:
        path = os.path.join(bmp_folder, name)
        try:
            with Image.open(path) as im:
                width, height = im.size
                arr = np.asarray(im.convert("RGB"))

            r = int(arr[0, 0, 0])
            g = int(arr[0, 0, 1])
            b = int(arr[0, 0, 2])
            rows.append([name, width, height, r, g, b])
            print("成功处理: %s (%d/%d)" % (name, len(rows), len(files)))
        except Exception as exc:  # noqa: BLE001
            print("处理文件失败: %s\n错误信息: %s" % (name, exc))
            continue

    with open(output_csv, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["文件名", "宽度", "高度", "R灰阶", "G灰阶", "B灰阶"])
        w.writerows(rows)

    print("已写入：%s（%d 行）" % (output_csv, len(rows)))
    return output_csv


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    bmp_folder = argv[0] if len(argv) > 0 else os.path.join("input")
    output_csv = argv[1] if len(argv) > 1 else "灰阶分析结果.csv"
    rgb_gray_extract(bmp_folder, output_csv)
    return 0


if __name__ == "__main__":
    sys.exit(main())