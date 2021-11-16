import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math
import numpy as np

matplotlib.use('TkAgg')

root = tk.Tk()
class MatTK:
    column=0
    fig = plt.figure(1)


    canvas = FigureCanvasTkAgg(fig, master=root)

    plot_widget = canvas.get_tk_widget()
    x = []
    for i in range(0, 500):
        x.append(i/10)
        y = []
    for i in x:
        y.append(math.sin(i))
    plt.fill_between(x, y)

    plot_widget.grid(row=0, column=column)
    #main_entry
    user_function = tk.StringVar()
    user_function_entry = tk.Entry(textvariable=user_function)
    user_function_entry.grid(row = 2, column=0)
    #entry first x
    first_x = tk.StringVar()
    first_x_entry = tk.Entry(textvariable=user_function)
    first_x_entry.grid(row = 3, column=0)
    #entry second x
    second_x = tk.StringVar()
    second_x_entry = tk.Entry(textvariable=user_function)
    second_x_entry.grid(row = 4, column=0)

    button_function = tk.Button(text='Интегрировать', command = display_newPlot)
    button_function.grid(row=1, column=0)
class MatTk2:
    column=1
    fig2 = plt.figure(2)


    canvas2 = FigureCanvasTkAgg(fig2, master=root)

    plot_widget = canvas.get_tk_widget()
    x = []
    for i in range(0, 500):
        x.append(i/10)
        y = []
    for i in x:
        y.append(math.sin(i))
    plt.fill_between(x, y)

    plot_widget.grid(row=0, column=column)
matTk3=MatTk2()
matTk4=MatTK()

def display_newPlot():
    pass





root.mainloop()
