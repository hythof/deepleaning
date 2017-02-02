# coding: utf-8

import sys
import os
import numpy as np
import pickle
import gzip
from PIL import Image

class MNIST(object):
    # see http://yann.lecun.com/exdb/mnist/
    # train_num = 60000
    # test_num = 10000
    # img_dim = (1, 28, 28)
    img_size = 784

    def __init__(self):
        self.train_img =  self._img('mnist/train-images-idx3-ubyte.gz')
        self.train_label = self._label('mnist/train-labels-idx1-ubyte.gz')
        self.test_img = self._img('mnist/t10k-images-idx3-ubyte.gz')
        self.test_label = self._label('mnist/t10k-labels-idx1-ubyte.gz')

    def _label(self, path):
        with gzip.open(path, 'rb') as f:
            return np.frombuffer(f.read(), np.uint8, offset=8)

    def _img(self, path):
        with gzip.open(path, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=16)
        return data.reshape(-1, self.img_size)
    
    def normalize(self):
        self.train_img = self.train_img.astype(np.float32) / 255.0
        self.test_img = self.test_img.astype(np.float32) / 255.0

    def flatten(self):
        self.train_img = self.train_img.reshape(-1, 1, 28, 28)
        self.test_img = self.test_img.reshape(-1, 1, 28, 28)

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def main():
    mnist = MNIST()
    mnist.normalize()
    mnist.flatten()

    img = mnist.train_img[0]
    label = mnist.train_label[0]
    print(label)  # 5

    print(img.shape)  # (784,)
    img = img.reshape(28, 28)  # 形状を元の画像サイズに変形
    print(img.shape)  # (28, 28)

    img_show(img)                                                                                                   

if __name__ == '__main__':
    main()
