import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import shutil

# 新建文件夹用于存放相关文件
os.mkdir('./format')
os.mkdir('./gray')
os.mkdir('./shape')
# 新建文件夹 用于存放清洗后的数据
os.mkdir('processed_data')

dst_data = ('./processed_data')
# 读取图片的路径
rock_path = os.listdir('./unprocessed_data/rock')
hand_path = os.listdir('./unprocessed_data/hand')
scissors_path = os.listdir('./unprocessed_data/scissors')

files_rock = os.listdir('./unprocessed_data/rock')
files_scissors = os.listdir('./unprocessed_data/scissors')
files_hand = os.listdir('./unprocessed_data/hand')

print(f'rock: ', len(files_rock))
print(f'scissors: ', len(files_scissors))
print(f'hand: ', len(files_hand))

dst_format = './format'  # 设置筛选后文件的目录路径'

for files in rock_path:
    filename1 = os.path.splitext(files)[1]  # 读取文件扩展名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    # 筛选扩展名不是jpg、png以及bmp的文件
    if filename1 != '.jpg' and filename1 != '.png' and filename1 != '.bmp':
        print(filename0, filename1, 'is a improper format')
        src_format = os.path.join('./unprocessed_data/rock', files)
        # 将分离出的非规定格式的文件移动到 format 目录中
        shutil.move(src_format, dst_format)

# 处理非彩色图像文件之后通过读取图像的存储维度来判断图像是否为彩色图像若图像的维度为二维，则图像是灰度图。
# 重新读取需要进行数据清洗的文件列表
rock_path = os.listdir('./unprocessed_data/rock')
dst_gray = './gray'  # 设置筛选后文件的目标路径
for files in rock_path:
    # 读取文件并将其拼接到路径中
    filename = os.path.join('./unprocessed_data/rock', files)
    # 读取rock目录下的图像文件，注意：flag需要设置为-1，这样才能保证图像的通道与原来的保持一致
    img = cv2.imread(filename, -1)
    dim = img.ndim  # 读取img 的维度
    if dim == 2:  # 若维度为二维，则为单通道灰度图
        print(files, "is a gray image")
        src_gray = os.path.join('./unprocessed_data/rock', files)
        # 将分离出的灰度图移动到gray目录中
        shutil.move(src_gray, dst_gray)

# 检验图像尺寸
# 重新读取需要进行数据清洗的文件列表
rock_path = os.listdir('./unprocessed_data/rock')
dst_shape = './shape/'  # 设置筛选后文件的目标路径
for k in rock_path:
    img = cv2.imread('./unprocessed_data/rock/' + k)
    h, w, c = img.shape
    if h != 200 and w != 300:
        print(k, 'is not the right size')
        src_shape = os.path.join('./unprocessed_data/rock', k)
        shutil.move(src_shape, dst_shape)
src_data1 = ('./unprocessed_data/rock')
# shutil.move(src_data1, dst_data)

# scissors类
for files in scissors_path:
    filename1 = os.path.splitext(files)[1]
    filename0 = os.path.splitext(files)[0]
    filename = os.path.join('./unprocessed_data/scissors', files)
    img = cv2.imread(filename, -1)

    if filename1 != '.jpg' and filename1 != '.png' and filename1 != '.bmp':
        print(filename0, filename1, 'is a improper format')
        src_format = os.path.join('./unprocessed_data/scissors/', files)
        shutil.move(src_format, dst_format)
    if img.ndim == 2:
        print(files, "is a gray image")
        src_gray = os.path.join("./unprocessed_data/scissors", files)
        shutil.move(src_gray, dst_gray)

# 重新读取需要进行数据清洗的文件列表
scissors_path = os.listdir('./unprocessed_data/scissors')
for k in scissors_path:
    img = cv2.imread('./unprocessed_data/scissors/' + k)
    h, w, c = img.shape
    if h != 200 and w != 300:
        print("k is not the right size")
        src_shape = os.path.join('./unprocessed_data/scissors', k)
        shutil.move(src_shape, dst_shape)
src_data2 = "./unprocessed_data/scissors"
shutil.move(src_data2, dst_data)

# hand类
for files in hand_path:
    filename1 = os.path.splitext(files)[1]
    filename0 = os.path.splitext(files)[0]
    filename = os.path.join('./unprocessed_data/hand/', files)
    img = cv2.imread(filename, -1)

    if filename1 != '.jpg' and filename1 != '.png' and filename1 != '.bmp':
        print(filename0, filename1, 'is a improper format')
        src_format = os.path.join('./unprocessed_data/hand/', files)
        shutil.move(src_format, dst_format)

    if img.ndim == 2:
        print(files, "is a gray image")
        src_gray = os.path.join('./unprocessed_data/hand/', files)
        shutil.move(src_gray, dst_gray)

# 重新读取需要进行数据清洗的文件列表
hand_path = os.listdir('./unprocessed_data/hand')
for k in hand_path:
    img = cv2.imread('./unprocessed_data/hand/' + k)
    h, w, c = img.shape
    if h != 200 and w != 300:
        print(k, 'is not the right size')
        src_shape = os.path.join('./unprocessed_data/hand', k)
        shutil.move(src_shape, dst_shape)
src_data3 = ('./unprocessed_data/hand')
shutil.move(src_data3, dst_data)
