width = 3200;
height = 2000;
filepath='D:\wjj';
background_color = [255, 255, 255]; % 白色 (RGB)
circle_color = [
    48,0,0;
96,0,0;
0,48,0;
48,48,0;
96,48,0;
0,96,0;
48,96,0;
96,96,0;
0,0,48;
48,0,48;
96,0,48;
0,48,48;
48,48,48;
96,48,48;
0,96,48;
48,96,48;
96,96,48;
0,0,96;
48,0,96;
96,0,96;
0,48,96;
48,48,96;
96,48,96;
0,96,96;
48,96,96
    ]; % 灰色 (RGB)



% 创建白色背景图像
bg_img = uint8(ones(height, width, 3));


for i=1:size(circle_color,1)
    for c=1:3
img(:,:,c)=bg_img(:,:,c)*circle_color(i,c);
    end

% 保存图像
filename=sprintf('C%d.png',i);
full_path=fullfile(filepath,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);
end