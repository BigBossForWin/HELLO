# -*-coding:utf8-*-
import os
import cv2
import shutil

def getAllPath(dirpath):
    PathArray = []
    for filename in os.listdir(dirpath):
        if filename.endswith('jpg') or filename.endswith('png'):
            PathArray.append(os.path.join(dirpath, filename))
    return PathArray

# 从源路径中读取所有图片放入一个list，然后逐一进行检查，把其中的脸扣下来，存储到目标路径中
def readPicSaveFace(sourcePath,invalidPath):
    try:
        ImagePaths = getAllPath(sourcePath)
        # 对list中图片逐一进行检查,找出其中的人脸然后写到目标文件夹下
        # haarcascade_frontalface_alt.xml为库训练好的分类器文件，下载opencv，安装目录中可找到
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        # 人脸识别模型文件（haarcascade_frontalface_alt.xml）
        for imagePath in ImagePaths:
            img = cv2.imread(imagePath)
            # 使用opencv读取图像，直接返回numpy.ndarray 对象，
            # 通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
            if type(img) != str:
                faces = face_cascade.detectMultiScale(img, 1.1, 5)
                # 2.调用detectMultiScale()函数检测，调整函数的参数可以使检测结果更加精确。
                '''1.image表示的是要检测的输入图像
                   2.objects表示检测到的人脸目标序列
                   3.scaleFactor表示每次图像尺寸减小的比例
                   4. minNeighbors表示每一个目标至少要被检测到3次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸),
                   5.minSize为目标的最小尺寸
                   6.minSize为目标的最大尺寸'''
                if len(faces):
                    print(imagePath + " have face")
                else:
                    shutil.move(imagePath, invalidPath)
    except IOError:
        print("Error")


if __name__ == '__main__':
    invalidPath = './user_no_face'
    sourcePath = 'user'
    readPicSaveFace(sourcePath,invalidPath)