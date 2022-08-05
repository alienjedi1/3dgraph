import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import math
import time
import tkinter as tk


def initalize():
    t = np.linspace(-299792458, 299792459, 1000)

    x = np.cos(t)
    y = np.sin(t)
    h = np.arcsinh(t)
    z = np.sin(h)
    return ([x, y, z, t])


class Parametric3D:
    def __init__(self, x, y, z, t=initalize()[3]):
        self.x = x
        self.y = y
        self.z = z
        print(initalize()[2])
        ax = plt.axes(projection='3d')

        ax.plot3D(x, y, z, color='black', linewidth=0.03)
        plt.show()


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI")
        inputtxt = tk.Text(root, height=5, width=20)
        inputtxt.pack()
        daButton = tk.Button(root, text="this", command=print("hi"))
        daButton.pack()


Parametric3D(initalize()[0], initalize()[1], initalize()[2])

# root = tk.Tk()
# my_gui = GUI(root)
# root.mainloop()
