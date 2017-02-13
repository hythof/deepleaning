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

    def normalize(self):
        self.train_img = self.train_img.astype(np.float32) / 255.0
        self.test_img = self.test_img.astype(np.float32) / 255.0

    def flatten(self):
        self.train_img = self.train_img.reshape(-1, 1, 28, 28)
        self.test_img = self.test_img.reshape(-1, 1, 28, 28)

    def one_hot(self):
        self.train_label = self._one_hot(self.train_label)
        self.test_label = self._one_hot(self.test_label)

    def _label(self, path):
        with gzip.open(path, 'rb') as f:
            return np.frombuffer(f.read(), np.uint8, offset=8)

    def _img(self, path):
        with gzip.open(path, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=16)
        return data.reshape(-1, self.img_size)
    
    def _one_hot(self, x):
        t = np.zeros((x.size, 10))
        for index, row in enumerate(t):
            row[x[index]] = 1
        return t


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y)) / batch_size

def main():
    mnist = MNIST()
    mnist.normalize()
    mnist.one_hot()

    print(mnist.train_img.shape)
    print(mnist.train_label.shape)

    train_size = mnist.train_img.shape[0]
    batch_size = 10
    batch_mask = np.random.choice(train_size, batch_size)
    train_img_batch = mnist.train_img[batch_mask]
    train_label_batch = mnist.train_label[batch_mask]
    print(train_img_batch)
    print(train_label_batch)

if __name__ == '__main__':
    main()
