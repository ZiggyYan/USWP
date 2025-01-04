import random
import os
import cv2
import numpy as np
import shutil
from PIL import Image
def get_pixels_with_value(image, value):
    coordinates = []
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x, y)) == value:
                coordinates.append((x, y))
                
    return coordinates
def split_patches(data_dir, post_fix=None):
    import math
    """ split large image into small patches """

    image_list = os.listdir(data_dir)
    for image_name in image_list:
        if '.png' in image_name:

            name = image_name.split('.')[0]
            if post_fix and name[-len(post_fix):] != post_fix:
                continue
            image_path = os.path.join(data_dir, image_name)
            gray_img = Image.open(image_path).convert('L')
            pixels = get_pixels_with_value(gray_img,255)
            print(len(pixels))
            # try:
            #     gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # except:
            #     print(image_name)
            # if np.sum(gray_img==255)==0:
            #     print(np.sum(gray_img==255))
            # print(type(image))
            # print(image.shape)
            # print(image.max())
            # hist, bin_edges = np.histogram(gray_img, bins=10)  # bins参数定义了分布的区间数量
            # # 打印分布
            # for i in range(len(hist)):
            #     if i == len(hist) - 1:
            #         if hist[i]==0:
            #             print(f"从{bin_edges[i]:.2f}到{bin_edges[i + 1]:.2f}: {hist[i]}个")
def copy_file(source_path, destination_folder):
        shutil.copy(source_path, destination_folder)

if __name__ == '__main__':
    # label_point_dir = './Dataset/BUSB_Binded/labels_point/train1'
    # split_patches(label_point_dir)
    source = './/Dataset/BUSB/binded/patches/labels_voronoi/binded_100_repeated360_4_label_point.png'
    target= './/Dataset/BUSB_Binded/labels_voronoi/val/binded_100_repeated360_4_label_point.png'
    copy_file(source,target)