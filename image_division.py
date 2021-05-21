from PIL import Image, ImageEnhance
# image = Image.open('image/est.JPG')
# w, h = image.size
# # box对背景图进行上下分割。
# print(w, h)
# box1 = (0, 0, w, int(h/2))
# box2 = (0, int(h/2), w, h)
# # im1是上半部分
# # im2是下半部分
# im1 = image.crop(box1)
# im2 = image.crop(box2)
# # 新建画布
# flag = Image.new('RGB', (w, h))
# # 对图片上半部分进行明暗处理，对下半部分进行对比度处理
# im1 = ImageEnhance.Brightness(im1).enhance(0.5)
# im2 = ImageEnhance.Contrast(im2).enhance(2.0)
# flag.paste(im1, (0, 0))
# flag.paste(im2, (0, int(h/2)))
# flag.save('image/result.jpg', quality=100)
# flag.show()
# -*- coding: utf-8 -*-

filename = r'image/est.JPG'
img = Image.open(filename)
size = img.size
print(size)

# 准备将图片切割成9张小图片
weight = int(size[0] // 3)
height = int(size[1] // 3)
# 切割后的小图的宽度和高度
print(weight, height)

for j in range(3):
    for i in range(3):
        box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
        region = img.crop(box)
        region.save('{}{}.png'.format(j, i))
