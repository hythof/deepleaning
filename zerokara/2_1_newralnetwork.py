import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def main():
    x = np.arange(-5.0, 5.0, 0.1)
    y1 = step_function(x)
    y2 = sigmoid(x)
    y3 = relu(x)
    plt.plot(x, y1, label="step")
    plt.plot(x, y2, label="sigmoid")
    plt.plot(x, y3, label="relu")
    plt.ylim(-0.1, 1.1)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
