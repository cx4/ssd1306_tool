# -*— coding:utf-8 -*-
'''author：Roy-Chang
   email：royalive#outlook.com
   https://cx4.tw
'''
from PIL import Image
img = Image.open('108.png')#文件的路径
img = img.convert('L')#将文件转换为灰度模式，或者‘1’ 1bit模式
#限制图像的宽度和屏幕的宽度一致
w,h = img.size
if w > 128:
    h = int((128/w) * h/1.8)
    w = 128
#使用ANTIALIAS滤镜精细化处理图像的缩放
#img = img.resize((w,h),Image.ANTIALIAS)
img = img.resize((w,h),)
width = img.width
height = img.height
img_list = []
def conver2(xx):
    if(xx == 255):
        return 0
    else:
        return 1
for x in range(height):
    scanline_list = []
    for y in range(width):
        pixel = img.getpixel((y,x))
        pixel = conver2(pixel)
        scanline_list.append(pixel)
        out = "'" + ''.join('%s' %id for id in scanline_list) + "',"
        #这个地方，在使用".join"的时候，因为上面的scanline_list里面的每个数据都是数字而不是str需要处理一下。
    img_list.append(out)
f = open('2bin.txt','w')#生成的01矩阵文本文件的存放位置。
for d in img_list:
    print(d,file=f)
f.close()
