#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量运行全部脚本（可选，用于一次生成所有图片）。

用法:
    python run_all.py            # 生成到 ./output
    OUTPUT_DIR=/tmp/out python run_all.py

注意：gamma_plot.py 会生成 4 x 256 = 1024 张图，其余为小批量。
"""
import importlib
import sys

MODULES = [
    "e2000",
    "oppo41color",
    "brightness25",
    "draw_e4_circles",
    "gac1_crosstalk",
    "gac2_crosstalk",
    "lcb_crosstalk",
    "hcs_crosstalk",
    "oppo_crosstalk",
    "gamma_plot",
]


def main():
    for name in MODULES:
        print("=== 运行 %s ===" % name)
        mod = importlib.import_module(name)
        mod.main()
    print("全部完成。")
    return 0


if __name__ == "__main__":
    sys.exit(main())