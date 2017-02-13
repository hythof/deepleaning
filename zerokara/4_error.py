from __future__ import print_function
import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y1 = [0.1, 0.1, 0.6, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
y2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.7, 0.1, 0.1, 0.1]

print("mean_squared_error hit", mean_squared_error(np.array(y1), np.array(t)))
print("mean_squared_error miss", mean_squared_error(np.array(y2), np.array(t)))
print("cross_entropy_error hit", cross_entropy_error(np.array(y1), np.array(t)))
print("cross_entropy_error miss", cross_entropy_error(np.array(y2), np.array(t)))
