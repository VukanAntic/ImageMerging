# Database used: https://www.kaggle.com/datasets/puneet6060/intel-image-classification/data
# TODO Maybe we should not be using pictures of glaciers, mountains, etc., just one single type of image
#  (for now)

import os
import tensorflow as tf
from matplotlib import pyplot as plt

import cv2
def load(image_path):
    sample_image = tf.io.read_file(image_path)
    sample_image = tf.io.decode_jpeg(sample_image)
    print(sample_image.shape)
    plt.figure()
    plt.imshow(sample_image)


train_path = "dataset/seg_train/seg_train/mountain"

def go_though_database(database_path):
    all_image_paths = []
    for filename in os.listdir(database_path):
        f = os.path.join(database_path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            all_image_paths.append(f)
            load(f)
            return
    return f


go_though_database(train_path)




