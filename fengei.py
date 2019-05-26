from PIL import Image

def cut_image(image,count):
# 每一行count个
    width, height = image.size
    item_width = int(width / count)
# 每次宽度的增量
    item_height = int(height / count)
#每次高度的增量
    box_list = []
    # (left, upper, right, lower)
# 使用PIL裁切图片使用PIL需要引用Image，使用Image的open(file)方法可以返回打开的图片，使用crop((x0,y0,x1,y1))方法可以对图片做裁切。
#
# 区域由一个4元组定义，表示为坐标是 (left, upper, right, lower)，Python Imaging Library 使用左上角为 (0, 0)的坐标系统

    for i in range(0,count):
        for j in range(0,count):
            box = (j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    # 类型<class 'PIL.Image.Image'>
    return image_list

#保存
def save_images(image_list):
    index = 1
    #计数
    for image in image_list:
        image.save('images/'+str(index) + '.png', 'PNG')

        index += 1

if __name__ == '__main__':
    file_path = "girls.png"  # 图片保存的地址
    image = Image.open(file_path)
    image_list = cut_image(image,5)
    save_images(image_list)