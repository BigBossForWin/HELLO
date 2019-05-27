from PIL import Image, ImageDraw, ImageFont
import os

def gen_text_img(text, font_size=20, font_path=None):
    # 从文字生成图像，输入：文字内容，文字字体大小，字体路径
    font = ImageFont.truetype(font_path, font_size) if font_path is not None else None
    # 加载一个TrueType或者OpenType字体文件，并且创建一个字体对象。
    # 这个函数从指定的文件加载了一个字体对象，
    # 并且为指定大小的字体创建了字体对象。
    # 在windows系统中，如果指定的文件不存在，加载器会顺便看看windows的字体目录下是否存在。
    # 这个函数需要_imagingft服务。
    (width, length) = font.getsize(text)  # 获取文字大小
    text_img = Image.new('RGBA', (width, length))
    draw = ImageDraw.Draw(text_img)
    # 第一个tuple表示未知(left,up)，之后是文字，然后颜色，最后设置字体
    draw.text((0, 0), text, fill=(0, 0, 0), font=font)
    # draw.text(position,string, options)
    # 含义：在给定的位置绘制一个字符创。变量position给出了文本的左上角的位置。
    # 变量option的font用于指定所用字体。它应该是类ImangFont的一个实例，
    # 使用ImageFont模块的load()
    # 方法从文件中加载的。
    # 变量options的fill给定文本的颜色。
    text_img.save('testtext.png')
    return text_img

def trans_alpha(img, pixel):
    '''根据rgba的pixel调节img的透明度
    这里传进来的pixel是一个四元组（r,g,b,alpha）
    '''
    # 给图像添加透明度（alpha通道）
    _, _, _, alpha = img.split()
    # print(type(alpha))
    # < class 'PIL.Image.Image'>
    alpha = alpha.point(lambda i: pixel[-1]*10)
    # print(type(alpha))
    # < class 'PIL.Image.Image'>
    # 改变像素点(函数)
    img.putalpha(alpha)
    #改变alpha通道
    return img

def picture_wall_mask(text_img, edge_len, pic_dir="./user"):
    # 根据文字图像生成对应的照片墙，输入：文字图像，各个照片边长，照片所在路径
    new_img = Image.new('RGBA', (text_img.size[0] * edge_len, text_img.size[1] * edge_len))
    # new_img.show()
    file_list = os.listdir(pic_dir)
    img_index = 0
    # 计数
    for x in range(0, text_img.size[0]):
        for y in range(0, text_img.size[1]):
            pixel = text_img.getpixel((x, y))
            # print(pixel) (0, 0, 0, 0)
            # 获取像素点
            file_name = file_list[img_index % len(file_list)]
            # 取img_index的照片名字 存在不同位置有相同图片，如果图片不够的话
            try:
                img = Image.open(os.path.join(pic_dir, file_name)).convert('RGBA')
                # 转换成RGBA图片
                img = img.resize((edge_len, edge_len))
                img = trans_alpha(img, pixel)
                new_img.paste(img, (x * edge_len, y * edge_len))
                img_index += 1
            except Exception as e:
                img_index += 1
                print(f"open file {file_name} failed! {e}")
    return new_img


def main(text='', font_size = 20, edge_len = 60,pic_dir = "./user", out_dir = "./out/", font_path = './simfang.ttf'):

    '''生成照片墙

    :param text: Text of picture wall, if not defined this will generage a rectangle picture wall
    :param font_size: font size of a clear value
    :param edge_len: sub picture's egde length

    '''

    if len(text) >= 1:
        text_ = ' '.join(text)#将字符串用空格分隔开
        print(f"generate text wall for '{text_}' with picture path:{pic_dir}")

        text_img = gen_text_img(text_, font_size, font_path)
        # text_img.show()
        img_ascii = picture_wall_mask(text_img, edge_len, pic_dir)
        # img_ascii.show()
        img_ascii.save(out_dir + os.path.sep + '_'.join(text) + '.png')

if __name__ == '__main__':
    main(text='戴嘉翘')