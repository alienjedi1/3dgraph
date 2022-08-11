import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import math
import time
import nltk


def initalize():
    t = np.linspace(-299792458, 299792459, 1000)
    h = np.arcsinh(t)

    x = np.cos(t)
    y = np.sin(t)
    z = np.sin(h)
    return ([x, y, z, t])


class Parametric3D:
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z

        ax = plt.figure().add_subplot(projection='3d')

        N = len(t)
        for i in range(N - 1):
            ax.plot(x[i:i + 2],
                    y[i:i + 2],
                    z[i:i + 2],
                    color=plt.cm.jet(255 * t[i] / N),
                    linewidth=0.05)
            print(f"{i / N * 100}%")
        # ax = plt.axes(projection='3d')
        # ax.plot3D(x, y, z, color="black", linewidth=0.03)
        plt.show()


Parametric3D(initalize()[0], initalize()[1], initalize()[2], initalize()[3])
