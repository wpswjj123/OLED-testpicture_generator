width = 3120;
height = 2080;
filepath='\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\图片\GAC-1_crosstalk';

% 创建127背景图像
background = uint8(ones(height, width, 3));
background=background*127;

width_b=width/3;
heigh_b=height/3;

%黑块长宽取整
width_b=floor(width_b);
heigh_b=floor(heigh_b);

bg_img=background;
%REF图
%左上角
bg_img(1:heigh_b,1:width_b,:)=0;
%左下角
bg_img(end-heigh_b+1:end,1:width_b,:)=0;
%右上角
bg_img(1:heigh_b,end-width_b+1:end,:)=0;
%右下角
bg_img(end-heigh_b+1:end,end-width_b+1:end,:)=0;
% 保存图像
filename='REF.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%HINF图
%左中
bg_img(heigh_b:2*heigh_b-1,1:width_b,:)=0;
%右中
bg_img(heigh_b:2*heigh_b-1,end-width_b+1:end,:)=0;
% 保存图像
filename='HINF.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%VINF图
%上中
bg_img(1:heigh_b,width_b+1:2*width_b,:)=0;
%下中
bg_img(end-heigh_b+1:end,width_b+1:2*width_b,:)=0;
% 保存图像
filename='VINF.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);