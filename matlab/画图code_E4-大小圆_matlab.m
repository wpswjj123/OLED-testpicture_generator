width = 3200;
height = 2000;
filepath='C:\Users\WPSgululu\Desktop\图片';
background_color = [255, 255, 255]; % 白色 (RGB)
circle_color = [
    255, 255, 255;
    230,230,230;
    209,209,209;
    186,186,186;
    158,158,158;
    0,0,0;
    115,82,66;
    194,150,130;
    94,122,156;
    89,107,66;
    130,128,176;
    99,189,168;
    217,120,41;
    74,92,163;
    194,84,97;
    92,61,107;
    158,186,64;
    230,161,46;
    51,61,150;
    71,148,71;
    176,48,59;
    237,199,33;
    186,84,145;
    0,133,163;
    255,0,0;
    0,255,0;
    0,0,255;
    0,255,255;
    255,0,255;
    255,255,0;
    112,64,38;
    204,138,102;
    255,199,153;
    255,199,171;
    247,171,125;
    199,140,92;
    143,92,51;
    207,150,115;
    161,87,33;
    214,133,92;
    209,138,105;
    250,153,115;
    199,143,107;
    201,140,107;
    204,143,105;
    122,74,38;
    217,140,94
    ]; % 灰色 (RGB)

% 计算圆的半径（面积占30%）
total_pixels = width * height;
circle_area = 0.3 * total_pixels;
circle_radius = sqrt(circle_area / pi); % ≈781

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

bg_img = uint8(ones(height, width, 3));
bg_img=bg_img*255;

% 计算圆心位置
center_x = width / 2;
center_y = height / 2;

% 生成网格坐标
[X, Y] = meshgrid(1:width, 1:height);

% 计算每个像素到圆心的距离
distance = sqrt((X - center_x).^2 + (Y - center_y).^2);

% 绘制圆形（距离 <= 半径的像素设为灰色）
circle_mask = distance <= circle_radius;
for i=1:size(circle_color,1)
    img=bg_img;
    current_color=circle_color(i,:);
for c = 1:3
    channel = img(:, :, c);
    channel(circle_mask) = current_color(c);
    img(:, :, c) = channel;
end

% 保存图像
filename=sprintf('C%d_0.3.png',i);
full_path=fullfile(filepath,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);
end
