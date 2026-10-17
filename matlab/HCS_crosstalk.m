Path='\\p5oanas.csot.tcl.com\oavdi\OAData\wujingjie1\Desktop\软件\图片\HCS_crosstalk'; 
 num=0;
 width = 3200;
 height = 3200;

 pixelsize = 112;

n1=fix(width/3);
m1=fix(height/3);
b=fix(9*1000/pixelsize);
HalfH=fix(width/2);
HalfV=fix(height/2);
n2=fix(width/6);
m2=fix(height/6);

img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(1:m1,HalfH-b:HalfH-b+n1,1:3)=0;
img(height-m1:height,HalfH-b:HalfH-b+n1,1:3)=0;
filename='V1.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);



img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(1:m1,HalfH+b:HalfH+b+n1,1:3)=0;
img(height-m1:height,HalfH+b:HalfH+b+n1,1:3)=0;
filename='V2.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);

img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(1:m1,n2+b:n2+b+n1,1:3)=0;
img(height-m1:height,n2+b:n2+b+n1,1:3)=0;
filename='V3.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);

img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(1:m1,n2-b:n2-b+n1,1:3)=0;
img(height-m1:height,n2-b:n2-b+n1,1:3)=0;
filename='V4.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);


img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(HalfV-b:HalfV-b+m1,1:n1,1:3)=0;
img(HalfV-b:HalfV-b+m1,width-n1:width,1:3)=0;
filename='H1.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);

img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(HalfV+b:HalfV+b+m1,1:n1,1:3)=0;
img(HalfV+b:HalfV+b+m1,width-n1:width,1:3)=0;
filename='H2.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);

img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(m2+b:HalfV+b,1:n1,1:3)=0;
img(m2+b:HalfV+b,width-n1:width,1:3)=0;
filename='H3.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);

img=zeros(height,width,3,'uint8');
img(:,:,1:3)=128;
img(m2-b:HalfV-b,1:n1,1:3)=0;
img(m2-b:HalfV-b,width-n1:width,1:3)=0;
filename='H4.png';
full_path=fullfile(Path,filename);
imwrite(img,full_path);
fprintf('已生成:%s_ ', full_path);