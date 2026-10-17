width = 1680;
height = 2520;
filepath='\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\图片\OPPO_crosstalk';

% 创建127背景图像
background = uint8(ones(height, width, 3));
background=background*127;

width_b=width/3;
heigh_b=height*3/8;
heigh_c=height/3;

%黑块长宽取整
width_b=floor(width_b);
heigh_b=floor(heigh_b);
heigh_c=floor(heigh_c);

bg_img=background;

%工字型1图
filename='GH_1.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

%工字型2图
%上白块
bg_img(1:heigh_b,width_b+1:2*width_b,:)=255;
%上白块
bg_img(end-heigh_b+1:end,width_b+1:2*width_b,:)=255;
% 保存图像
filename='G_2.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%工字型3图
%左白块
bg_img(heigh_b+1:end-heigh_b,1:width_b,:)=255;
%右白块
bg_img(heigh_b+1:end-heigh_b,end+1-width_b:end,:)=255;
% 保存图像
filename='G_3.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%工字型4图
%上黑块
bg_img(1:heigh_b,width_b+1:2*width_b,:)=0;
%上黑块
bg_img(end-heigh_b+1:end,width_b+1:2*width_b,:)=0;
% 保存图像
filename='G_4.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%工字型5图
%左黑块
bg_img(heigh_b+1:end-heigh_b,1:width_b,:)=0;
%右黑块
bg_img(heigh_b+1:end-heigh_b,end+1-width_b:end,:)=0;
% 保存图像
filename='G_5.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%回字型2图
%中白块
bg_img(heigh_c+1:end-heigh_c,width_b+1:end-width_b,:)=255;
% 保存图像
filename='H_2.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);

bg_img=background;
%回字型3图
%中白块
bg_img(heigh_c+1:end-heigh_c,width_b+1:end-width_b,:)=0;
% 保存图像
filename='H_3.bmp';
full_path=fullfile(filepath,filename);
imwrite(bg_img,full_path);
fprintf('已生成:%s_ ', filename);