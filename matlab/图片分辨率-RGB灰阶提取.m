clear; clc;
% 1. 设置路径参数
bmpFolder = '\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\100% APL';  % 替换为你的BMP文件夹路径
outputExcel = '\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\BMP灰阶分析结果.csv';

% 3. 获取所有BMP文件
bmpFiles = dir(fullfile(bmpFolder, '*.bmp'));
if isempty(bmpFiles)
    error('未找到任何BMP文件，请检查路径是否正确');
end

% 4. 准备结果表格
results = cell(length(bmpFiles)+1, 6);
header = {'文件名', '宽度', '高度', 'R灰阶', 'G灰阶', 'B灰阶'};
results(1,:) = header;

% 5. 处理每张BMP图片
for i = 1:length(bmpFiles)
    try
        % 读取BMP文件
        filePath = fullfile(bmpFolder, bmpFiles(i).name);
        bmpInfo = imfinfo(filePath);
        colorImg = imread(filePath);
        
        % 检查并转换图像类型
        if bmpInfo.BitDepth == 1
            % 二值图像直接处理
            grayImg = logical(colorImg);
        elseif bmpInfo.BitDepth == 8
            % 8位灰度图像
            if size(colorImg,3) == 1
                grayImg = colorImg;
            else
                grayImg = rgb2gray(colorImg);
            end
        elseif bmpInfo.BitDepth == 24
            % 24位真彩色图像
            R_grayImg = colorImg(1,1,1);
            G_grayImg = colorImg(1,1,2);
            B_grayImg = colorImg(1,1,3);
        else
            % 其他格式提示
            warning('不支持的BMP位深度: %d, 文件名: %s', bmpInfo.BitDepth, bmpFiles(i).name);
            continue;
        end
        
        
        % 存储结果
        results{i+1,1} = bmpFiles(i).name;
        results{i+1,2} = size(colorImg,2);
        results{i+1,3} = size(colorImg,1);
        results{i+1,4} = R_grayImg;
        results{i+1,5} = G_grayImg;
        results{i+1,6} = B_grayImg;
        
        fprintf('成功处理: %s (%d/%d)\n', bmpFiles(i).name, i, length(bmpFiles));
        fprintf('R: %s %d\n', bmpFiles(i).name,size(R_grayImg,1));
    catch ME
        warning('处理文件失败: %s\n错误信息: %s', bmpFiles(i).name, ME.message);
        continue;
    end
end

% 6. 保存Excel结果
fid=fopen('\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\灰阶分析结果.csv','w');
for i= 2:size(results,1)
    %fprintf(fid,'%s,%s,%s,%s,%s,%s\n',results{i,:});
    fprintf(fid,'%s,%d,%d,%d,%d,%d\n',results{i,:});
end
fclose(fid);