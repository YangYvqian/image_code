from PIL import Image

# 打开要处理的图像
img_src = Image.open('image\est.JPG')

# 转换图片的模式为RGBA
img_src = img_src.convert('RGBA')

# 获得文字图片的每个像素点
src_strlist = img_src.load()

# 100,100 是像素点的坐标
data = src_strlist[982, 761]
# 结果data是一个元组包含这个像素点的颜色信息    栗子：(0, 0, 0, 255)
print(data)

