width = 2760;
height = 1256;
filepathW='D:\wjj\GAMMA\W';
filepathR='D:\wjj\GAMMA\R';
filepathG='D:\wjj\GAMMA\G';
filepathB='D:\wjj\GAMMA\B';

% 创建白色背景图像
bg_img = uint8(ones(height, width, 3));

for j=0:255
img=bg_img*j;
% 保存图像
filename=sprintf('W%d.png',j);
full_path=fullfile(filepathW,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);
end
for j=0:255
img(:,:,1)=bg_img(:,:,1)*j;
img(:,:,2)=bg_img(:,:,2)*0;
img(:,:,3)=bg_img(:,:,3)*0;
% 保存图像
filename=sprintf('R%d.png',j);
full_path=fullfile(filepathR,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);
end
for j=0:255
img(:,:,1)=bg_img(:,:,1)*0;
img(:,:,2)=bg_img(:,:,2)*j;
img(:,:,3)=bg_img(:,:,3)*0;
% 保存图像
filename=sprintf('G%d.png',j);
full_path=fullfile(filepathG,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);
end
for j=0:255
img(:,:,1)=bg_img(:,:,1)*0;
img(:,:,2)=bg_img(:,:,2)*0;
img(:,:,3)=bg_img(:,:,3)*j;
% 保存图像
filename=sprintf('B%d.png',j);
full_path=fullfile(filepathB,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);
end

