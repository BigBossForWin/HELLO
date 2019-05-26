import os
from PIL import Image

'''
把目录下的图片拼接成一张大图片
'''

# 图片压缩后的大小
width_i = 200
height_i = 300

# 每行每列显示图片数量
line_max = 5
row_max = 5

# 参数初始化
all_path = []
num = 0
pic_max = line_max * row_max

for filename in os.listdir('./images'):
    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    # 这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中
    # filename 类型 str
    if filename.endswith('jpg') or filename.endswith('png'):
        # 字符串以 jpg or png 结尾的
        all_path.append(os.path.join('./images', filename))
#  会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
# 以上一种情况为先。在上一种情况确保情况下，若出现”./”开头的参数，会从”./”开头的参数的上一个参数开始拼接。
# 将路径拼接
toImage = Image.new('RGBA', (width_i * line_max, height_i * row_max))
# 建立一个新的图像，mode表示色彩空间;size表示大小;color表示初始颜色,缺省时为黑色。如果color为None，
# 则图片不会初始化，以便于画图或复制图片。
for i in range(0, row_max):
    for j in range(0, line_max):

        # 图片比计划的少
        if num >= len(all_path):
            print("breadk")
            break

        pic_fole_head = Image.open(all_path[num])
        # print(pic_fole_head)
        #  <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=200x300 at 0x1EA89E8>
        width, height = pic_fole_head.size

        tmppic = pic_fole_head.resize((width_i, height_i))
        # 返回一个调整过大小的图片的复制品。size参数给出一个，以像素为单位的二维元组（weight, height）
        # 参数filter可以是NEAREST（使用临近取样）
        # ,BILINEAR（在2x2环境中的线性插值），BICUBIC（在4x4环境下的三次样条插值），
        # 或者ANTIALIAS（一个高质量的下采样过滤器），如果缺省，或图像的模式为“1”或者“P”，它将被设置为NEAREST。
        loc = (int(i % line_max * width_i), int(j % line_max * height_i))
        # loc 为图片摆放的坐标 为元组
        # print("第" + str(num) + "存放位置" + str(loc))
        toImage.paste(tmppic, loc)
        # 将其他的图片粘贴到这张图片上。这个box参数是一个提供上左角的2元组，或是一个提供左，上，右，下的4维元组候选区，或是空（None或者（0,0））
        # 如果提供了4维元组，被粘贴的图片必须与这个元组所确定的的区域的尺寸相符
        num = num + 1
        # 计数

    # 图片比计划的多
    if num >= pic_max:
        break
    # 多余的不要
print(toImage.size)
toImage.save('merged.png')