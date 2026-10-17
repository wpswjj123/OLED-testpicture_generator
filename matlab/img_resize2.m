function img_resize_demo(inputPath, W, H, mode, outPath, bg)
% IMG_RESIZE_DEMO  读取图片分辨率，并缩放到任意指定分辨率
%
% 用法:
%   img_resize_demo('in.jpg', 500, 300, 'stretch')
%   img_resize_demo('in.jpg', 500, 300, 'fit',   'out.png', [255 255 255])
%   img_resize_demo('in.jpg', 500, 300, 'crop',  'out.png')
%
% mode:  'stretch' 直接拉伸铺满（可能变形）
%        'fit'     等比缩放 + 居中留边（不变形，有留边）
%        'crop'    等比缩放 + 居中裁剪（不变形，无留边）

    if nargin < 4 || isempty(mode), mode = 'stretch'; end
    if nargin < 6 || isempty(bg),   bg   = [255 255 255]; end

    %% 1. 读图并打印原始分辨率
    img = imread(inputPath);
    [h, w, ~] = size(img);               % h = 高度(行数), w = 宽度(列数)
    fprintf('原始分辨率: %d × %d\n', w, h);

    %% 2. 按模式缩放到严格 W×H
    switch lower(mode)
        case 'stretch'
            out = imresize(img, [H W]);              % 直接重采样，可能变形

        case 'fit'
            scale = min(W/w, H/h);
            nw = max(1, round(w * scale));
            nh = max(1, round(h * scale));
            tmp = imresize(img, [nh nw]);
            if size(img, 3) == 3
                out = repmat(reshape(uint8(bg(:)'), 1, 1, 3), H, W, 1);
            else
                out = repmat(uint8(bg(1)), H, W);
            end
            r0 = floor((H - nh)/2) + 1;
            c0 = floor((W - nw)/2) + 1;
            out(r0:r0+nh-1, c0:c0+nw-1, :) = tmp;

        case 'crop'
            scale = max(W/w, H/h);
            nw = max(W, round(w * scale));
            nh = max(H, round(h * scale));
            tmp = imresize(img, [nh nw]);
            r0 = floor((nh - H)/2) + 1;
            c0 = floor((nw - W)/2) + 1;
            out = tmp(r0:r0+H-1, c0:c0+W-1, :);

        otherwise
            error('未知模式: %s（可选 stretch / fit / crop）', mode);
    end

    %% 3. 保存并打印输出分辨率
    if nargin < 5 || isempty(outPath)
        [p, n, ~] = fileparts(inputPath);
        outPath = fullfile(p, sprintf('%s_%dx%d.png', n, W, H));
    end
    imwrite(out, outPath);
    [oh, ow, ~] = size(out);
    fprintf('输出分辨率: %d × %d  ->  %s\n', ow, oh, outPath);
end