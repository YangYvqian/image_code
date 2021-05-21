from PIL import Image

# 打开要处理的图像
img_src = Image.open(r'image\est.JPG')

# 转换图片的模式为RGBA
img_src = img_src.convert('RGB')

# 获得文字图片的每个像素点
src_strList = img_src.load()
data = list()
# 100,100 是像素点的坐标
data.append(src_strList[581, 335])  # 左 上
data.append(src_strList[944, 335])  # 右上
data.append(src_strList[944, 712])  # 右下
data.append(src_strList[581, 712])  # 左下
# 结果data是一个元组包含这个像素点的颜色信息    栗子：(0, 0, 0, 255)
print(data)

