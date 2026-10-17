width = 3120;
height = 2080;
filepath='\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\图片\GAC-2_crosstalk';

% 创建186背景图像
background = uint8(ones(height, width, 3));
background=background*255;

width_b=width/3;
heigh_b=height/3;
width_c=width/6;
heigh_c=height/6;

%黑块长宽取整
width_b=floor(width_b);
heigh_b=floor(heigh_b);
width_c=floor(width_c);
heigh_c=floor(heigh_c);

bg_img=background;
%REF图
%竖列
bg_img(heigh_b+1:2*heigh_b,:,:)=127;
%横列
bg_img(:,width_b+1:2*width_b,:)=127;
% 保存图像
filename='REF.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%HINF图
%上横纹
bg_img(1:heigh_c,:,:)=127;
%下横纹
bg_img(end-heigh_c+1:end,:,:)=127;
%竖条纹
bg_img(:,width_b+1:2*width_b,:)=127;
% 保存图像
filename='H.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%VINF图
%左竖纹
bg_img(:,1:width_c,:)=127;
%右竖纹
bg_img(:,end-width_c+1:end,:)=127;
%横纹
bg_img(heigh_b+1:2*heigh_b,:,:)=127;
% 保存图像
filename='V.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);