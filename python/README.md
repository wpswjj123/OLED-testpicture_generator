# Python 版：OLED 测试图生成脚本

这是 `matlab/` 目录下 13 个 MATLAB 脚本的 **Python 等价实现**，用于在没有 MATLAB 的环境
（如 GitHub Codespaces / Linux / CI）中直接运行生成测试图。

## 为什么有这一版

原 MATLAB 脚本存在两个无法在 GitHub 上运行的问题：

1. **运行环境**：`.m` 文件需要 MATLAB + Image Processing Toolbox；
2. **写死路径**：源码里 `filepath` 指向公司内网 / 本机 Windows 路径
   （`\\p5oanas.csot.tcl.com\...`、`D:\wjj`、`C:\Users\WPSgululu\...`），
   云端（Linux）无法访问。

本版用 **numpy + Pillow** 重写，输出目录统一可配置，不再依赖任何本地路径。

## 环境准备

```bash
pip install -r requirements.txt      # numpy, Pillow
```

## 运行

所有脚本默认把图片写到 `./output/<脚本名>/`。
可用环境变量 `OUTPUT_DIR` 覆盖根目录：

```bash
OUTPUT_DIR=/workspaces/out python e2000.py
```

生成**全部**图片（注意 `gamma_plot.py` 会生成 1024 张，耗时略长）：

```bash
python run_all.py
```

## 脚本对照表

| MATLAB 源文件 | Python 脚本 | 输出 | 尺寸 |
| --- | --- | --- | --- |
| `E2000.m` | `e2000.py` | `output/E2000/E1..E25.png` | 3120×2080 |
| `oppo41color.m` | `oppo41color.py` | `output/oppo41color/C1..C41.png` | 3200×2000 |
| `偷亮25图code.m` | `brightness25.py` | `output/brightness25/C1..C25.png` | 3200×2000 |
| `画图code_E4-大小圆_matlab.m` | `draw_e4_circles.py` | `output/draw_e4_circles/C1..C46.png`、`C1..C46_0.3.png` | 3200×2000 |
| `GAC-1_crosstalk.m` | `gac1_crosstalk.py` | `output/gac1_crosstalk/REF,HINF,VINF.bmp` | 3120×2080 |
| `GAC-2_crosstalk.m` | `gac2_crosstalk.py` | `output/gac2_crosstalk/REF,H,V.bmp` | 3120×2080 |
| `LCB_crosstalk.m` | `lcb_crosstalk.py` | `output/lcb_crosstalk/REF,HINF,VINF.png` | 3200×2000 |
| `HCS_crosstalk.m` | `hcs_crosstalk.py` | `output/hcs_crosstalk/V1..V4,H1..H4.png` | 3200×3200 |
| `OPPO_crosstalk.m` | `oppo_crosstalk.py` | `output/oppo_crosstalk/GH_1,G_2..G_5,H_2,H_3.bmp` | 1680×2520 |
| `gamma画图code.m` | `gamma_plot.py` | `output/gamma/{W,R,G,B}/<通道>0..255.png` | 2760×1256 |
| `img_resize.m` | `img_resize.py` | 命令行缩放工具 | 任意 |
| `img_resize2.m` | `img_resize2.py` | 命令行缩放工具 | 任意 |
| `图片分辨率-RGB灰阶提取.m` | `rgb_gray_extract.py` | BMP 灰阶分析 CSV | — |

## 两个命令行工具

```bash
# 缩放单张图片到 500x300
python img_resize.py in.jpg 500 300 stretch
python img_resize.py in.jpg 500 300 fit out.png 255,255,255
python img_resize.py in.jpg 500 300 crop

# BMP 灰阶批量分析
python rgb_gray_extract.py ./某图片文件夹 ./BMP灰阶分析结果.csv
```

## 在 GitHub Codespaces 里跑

1. 仓库页面点 **Code → Codespaces → Create codespace on main**；
2. 终端里 `cd python && pip install -r requirements.txt`；
3. `python e2000.py`（或 `python run_all.py`）；
4. 生成的图片在 `python/output/` 下。

## 说明

- 颜色表、尺寸、文件名、灰阶值均按原 `.m` 脚本 1:1 还原；
- MATLAB 里 `img(:,:,c)=bg_img(:,:,c)*circle_color(i,c)` 对 `uint8(1)*255` 会因类型饱和
  产生截断，本版按等效结果直接填充目标 RGB 值，输出与原脚本一致；
- 原脚本中没有可移植的值（如 `filepath`）已全部移除，改为 `OUTPUT_DIR` 控制。