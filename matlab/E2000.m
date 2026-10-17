width = 3120;
height = 2080;
filepath='\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\图片\E2000';
circle_color = [
    255,255,255;
    115,82,68;
    194,150,130;
    98,122,157;
    87,108,67;
    133,128,177;
    103,189,170;
    214,126,44;
    80,91,166;
    193,90,99;
    94,60,108;
    157,188,64;
    224,163,46;
    56,61,150;
    70,148,73;
    175,54,60;
    231,199,31;
    187,86,149;
    8,133,161;
    243,243,242;
    200,200,200;
    160,160,160;
    122,122,121;
    85,85,85;
    52,52,52
    ]; % 灰色 (RGB)
% 创建白色背景图像
bg_img = uint8(ones(height, width, 3));


for i=1:size(circle_color,1)
    for c=1:3
    img(:,:,c)=bg_img(:,:,c)*circle_color(i,c);
    end

% 保存图像
filename=sprintf('E%d.png',i);
full_path=fullfile(filepath,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);
end