import os, sys
from PIL import Image,ImageFilter,ImageDraw,ImageFont
im = Image.open("image/Hu.JPG")
# im.show()
# xsize,ysize=im.size
# im.thumbnail((xsize//2,ysize//2))
# im.save("image/thumb_pic01.jpg","JPEG")
# im=im.resize((im.size[0]//2,im.size[1]//2))
# out=im.rotate(90).save("pic01_rotate_90.jpg")
# out=im.transpose(Image.FLIP_LEFT_RIGHT)  # 将图片进行左右翻转操作
# out.show()
# out=im.transpose(Image.FLIP_TOP_BOTTOM)  # 将图片进行上下翻转操作
# out.show()
# out=im.transpose(Image.ROTATE_180)  # 将图片旋转180°
# out.show()

# 截取图片并实现将图片沿着某一方向滑动的效果
# def roll_x_side(image, delta):
#     "Roll an image sideways"
#     xsize, ysize = image.size
#     delta = delta % xsize
#     if delta == 0: return image
#     part1 = image.crop((0, 0, delta, ysize))
#     part2 = image.crop((delta, 0, xsize, ysize))
#     image.paste(part2, (0, 0, xsize - delta, ysize))
#     image.paste(part1, (xsize - delta, 0, xsize, ysize))
#     return image
# def roll_y_side(image, delta):
#     "Roll an image sideways"
#     xsize, ysize = image.size
#     delta = delta % ysize
#     if delta == 0: return image
#     part1 = image.crop((0, 0, xsize, delta))
#     part2 = image.crop((0, delta, xsize, ysize))
#     image.paste(part2, (0, 0, xsize, ysize - delta))
#     image.paste(part1, (0, ysize - delta, xsize, ysize))
#     return image
#
#
# im = Image.open("image/est.JPG")
# im_01 = roll_x_side(im, 600)
# im_01.save("image/pic01_x_roll.jpg")
# im_01.show()
# im_02 = roll_y_side(im, 600)
# im_02.save("image/pic01_y_roll.jpg")
# im_02.show()


# 将彩色图片分开成单个通道再合并
# im.show()
# r, g, b = im.split()
# r.show()
# g.show()
# b.show()  # 将这几个单通道的图片重新组合成一张新的图片
# im = Image.merge("RGB", (b, r, g))
# im.show()
# 颜色变换：将彩色图片转换为灰度图
# im.show()
# out=im.convert("L")#将RGB格式的图片转换为灰度图
# out.show()
# print(out.mode,out.format,out.size)


# 图像滤波
# out=im.filter(ImageFilter.DETAIL)  # 细节增强
# out.show()
# out=im.filter(ImageFilter.BLUR)  # 模糊化
# out.show()
# out=im.filter(ImageFilter.CONTOUR)  # 轮廓滤波，将图片的轮廓提取出来
# out.show()
# out=im.filter(ImageFilter.EDGE_ENHANCE)  # 边缘强化
# out.show()
# out=im.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 深度边缘增强滤波，会使得图像中边缘部分更加明显
# out.show()
# out=im.filter(ImageFilter.EMBOSS)  # 浮雕滤波，会使图像呈现出浮雕效果
# out.show()
# out=im.filter(ImageFilter.SMOOTH)  # 平滑滤波
# out.show()

# 转换图像格式的脚本（jpg 转为 png 格式）
root = 'image/'
# for name in os.listdir(root):
#     infile = root + name
#     f, e = os.path.splitext(infile)   # f 变量是除扩展名以外的文件名，e 变量是扩展名
#     if os.path.isfile(infile):
#         outfile = f +".png"  # 拼凑输出文件名
#         print(f)
#         if infile != outfile:   # 保存的图像格式跟原图像格式不一样
#             try:
#                 Image.open(infile).save(outfile)  # 转换图像格式
#             except IOError:
#                 print("Cannot convert", infile)  # 图像无法打开，则处理异常

# 创建缩略图
# for name in os.listdir(root):
#     infile = root + name
#     if os.path.isfile(infile):
#         outfile = os.path.splitext(infile)[0] + ".thumbnail" # 缩略图文件名+后缀
#         if infile != outfile:
#             try:
#                 im   = Image.open(infile) # 打开图像
#                 x, y = im.size  # 获取原图像的大小（width、height）
#                 im.thumbnail((x//2, y//2)) # 缩略图大小
#                 im.save(outfile, "JPEG") # 保存为 JPEG 格式
#             except IOError:
#                 print("cannot create thumbnail for", infile)

# 图像的剪切、粘贴与合并操作
# 裁剪子矩形
# box = (80, 80, 300, 300)
# region = im.crop(box)
# region.show()
# # 处理子图，粘贴回原图
# region = region.transpose(Image.ROTATE_270)   # 旋转180°
# im.paste(region, box)
# im.show()


# transpose() 方法可以将图片左右颠倒、上下颠倒、旋转 90°90°、旋转 180°180° 或旋转 270°270°。paste() 方法则可以将一个 Image 实例粘贴到另一个 Image 实例上。
# def roll(image, delta):
#     "Roll an image sideways"
#
#     xsize, ysize = image.size
#
#     delta = delta % xsize  # 翻卷多少像素
#     if delta == 0: return image   # 不翻卷图形
#
#     part1 = image.crop((0, 0, delta, ysize))  # 左边矩形选区
#     part2 = image.crop((delta, 0, xsize, ysize))  # 右边矩形选区
#     part1.load()
#     part2.load()
#     image.paste(part2, (0, 0, xsize-delta, ysize)) # 原右边图形贴到左边
#     image.paste(part1, (xsize-delta, 0, xsize, ysize))  # 原左边图形贴到右边
#
#     return image
#
#
# im = Image.open("image/Hu.JPG")
# print(im.size)   # (356, 362)
# roll(im,100).save('image/5a2e2075f331d.png','JPEG')


# 几何变换
# Image 类包含了 resize() 和 rotate 方法来变换图像。前者需要传入一个表示新大小的元组，后者需要传入旋转的角度。
# 简单的几何变换
# out = im.resize((128, 128))
# out.show()
# 顺时针角度表示
# rout = out.rotate(45)
# rout.show()
# 旋转图像
# out = im.transpose(Image.FLIP_LEFT_RIGHT) # 左右颠倒
# out = im.transpose(Image.FLIP_TOP_BOTTOM) # 上下颠倒
# out = im.transpose(Image.ROTATE_90)  # 旋转90°
# out = im.transpose(Image.ROTATE_180)  # 旋转180°
# out = im.transpose(Image.ROTATE_270)  # 旋转270°


# 画直线
# drawAvatar = ImageDraw.Draw(im)
# xSize,ySize = im.size
#
# # 三等分位置
# drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize],\
#     fill = (255, 100, 0), width = 3)
# # 左下角到中心点，右下角到中心点
# drawAvatar.line([(0, ySize), (0.5 * xSize, 0.5 * ySize), (xSize, ySize)],\
#     fill = (255, 0, 0), width = 3)
# im.save('image/5a2e2075f331d.jpg')

with Image.open("image/Hu.png").convert("RGBA") as base:

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("C:\Windows\Fonts/Arial.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((10,10), "Hello", font=fnt, fill=(25,255,255,128))
    # draw text, full opacity
    d.text((10,60), "World", font=fnt, fill=(255,25,255,255))

    out = Image.alpha_composite(base, txt)

    out.show()