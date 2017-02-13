from __future__ import print_function
import numpy as np
import matplotlib.pylab as plt

def f1(x):
    return 0.01 * x ** 2 + 0.1 * x

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2 * h)

def tangent_line(f, x, t):
    d = numerical_diff(f, x)
    y = f(x) - d * x
    return d * t + y

x = np.arange(0.0, 20.0, 0.1)
y = f1(x)

v5 = numerical_diff(f1, 5)
v10 =  numerical_diff(f1, 10)
print(5, v5)
print(10, v10)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.plot(x, tangent_line(f1, 5, x))
plt.plot(x, tangent_line(f1, 10, x))
plt.show()
