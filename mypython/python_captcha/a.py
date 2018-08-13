#-*- coding:utf8 -*-
from PIL import Image

im = Image.open("captcha.gif")
#(将图片转换为8位像素模式)
im.convert("P")

#打印颜色直方图
print im.histogram()


his = im.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
    print j,k


im = Image.open("captcha.gif")
im.convert("P")
im2 = Image.new("P",im.size,255)


for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227: # these are the numbers to get
            im2.putpixel((y,x),0)

im2.show()
