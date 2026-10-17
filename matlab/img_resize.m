function img_resize(inputPath,W,H,mode,outPath,bg)
% IMG_RESIZE 读取图片分辨率并缩放（不依赖 Image Processing Toolbox）
%
% 用法:
% img_resize('in.jpg', 500, 300, 'stretch')
% img_resize('in.jpg', 500, 300, 'fit', 'out.png', [255 255 255])
% img_resize('in.jpg', 500, 300, 'crop')
%
% mode: 'stretch' 直接拉伸 / 'fit' 等比+留边 / 'crop' 等比+居中裁剪
 if nargin < 4 || isempty(mode), mode = 'stretch'; end
 if nargin < 6 || isempty(bg), bg = [255 255 255]; end
 %% 1. 读图，打印原始分辨率
 img = imread(inputPath);
 [h, w, c] = size(img);
 fprintf('原始分辨率: %d × %d\n', w, h);
 %% 2. 缩放
 switch lower(mode)
 case 'stretch'
 out = local_resize(img, W, H);
 case 'fit'
 scale = min(W/w, H/h);
 nw = max(1, round(w*scale)); nh = max(1, round(h*scale));
 tmp = local_resize(img, nw, nh);
 if c == 3
 out = repmat(reshape(uint8(bg(:)'), 1, 1, 3), H, W, 1);
 else
 out = repmat(uint8(bg(1)), H, W);
 end
 r0 = floor((H-nh)/2)+1; c0 = floor((W-nw)/2)+1;
 out(r0:r0+nh-1, c0:c0+nw-1, :) = tmp;
 case 'crop'
 scale = max(W/w, H/h);
 nw = max(W, round(w*scale)); nh = max(H, round(h*scale));
 tmp = local_resize(img, nw, nh);
 r0 = floor((nh-H)/2)+1; c0 = floor((nw-W)/2)+1;
 out = tmp(r0:r0+H-1, c0:c0+W-1, :);
 otherwise
 error('未知模式: %s', mode);
 end
 %% 3. 保存
 if nargin < 5 || isempty(outPath)
 [p,n,~] = fileparts(inputPath);
 outPath = fullfile(p, sprintf('%s_%dx%d.png', n, W, H));
 end
 imwrite(out, outPath);
 [oh,ow,~] = size(out);
 fprintf('输出分辨率: %d × %d -> %s\n', ow, oh, outPath);
end
% ================= 本地重采样（用 imresize 的替代）=================
function out = local_resize(img, W, H)
% 用基础函数 interp2 做双线性重采样，输出严格 H×W×c
 [h, w, c] = size(img);
 % 目标像素的源坐标（1-based，均匀铺满 [1,w] 与 [1,h]，不越界）
 xi = linspace(1, w, W); % 1×W
 yi = linspace(1, h, H); % 1×H
 [XI, YI] = meshgrid(xi, yi); % H×W
 out = zeros(H, W, c, 'like', img);
 for k = 1:c
 out(:,:,k) = interp2(double(img(:,:,k)), XI, YI, 'linear');
 end
 out = cast(out, 'like', img); % 转回原类型(uint8 等)
end