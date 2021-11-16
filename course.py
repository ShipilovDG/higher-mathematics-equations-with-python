from logging import root
import tkinter as tk
from tkinter import Button, Entry, Tk, font,Canvas
import tkinter
from types import ClassMethodDescriptorType, new_class
from matplotlib import interactive
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import *
from time import sleep
import random
global COLORS
COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
def main():
    class Interface:
        def __init__(self) -> None:
            pass
    class First_ex:
        close = True
        def __init__(self) -> None:
            self.window = tk.Toplevel()
            self.label_function = tk.Label(self.window,text="Введите функцию",font=18)
            self.label_function.grid(row=1,column=0,pady=(40,0))
                                
            self.user_function = tk.StringVar()
            self.user_function_entry = tk.Entry(self.window,textvariable=self.user_function, font=18)
            self.user_function_entry.grid(row=2,column=0)
                                
            #entry first x
                                
            self.label_function = tk.Label(self.window,text="Введите нижний предел X",font=18)
            self.label_function.grid(row=3,column=0,pady=(10,0))
                                
            self.first_x = tk.StringVar()
            self.first_x_entry = tk.Entry(self.window,textvariable=self.first_x, font=18)
            self.first_x_entry.grid(row=4,column=0)
                                
            #entry second x
    
            self.label_function = tk.Label(self.window,text="Введите верхний предел X",font=18)
            self.label_function.grid(row=5,column=0,pady=(10,0))
            
            self.second_x = tk.StringVar()
            self.second_x_entry = tk.Entry(self.window,textvariable=self.second_x, font=18)
            self.second_x_entry.grid(row=6,column=0)
            global num_fig
            num_fig=0
            
            
            def display_newPlot_right():
                    
                global num_fig
                num_fig+=1
                global x_array
                self.interval = 0.01
                self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                    

                self.root= tk.Tk()
                

                
                self.fig = plt.figure(num_fig)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

                self.plot_widget = self.canvas.get_tk_widget()
                self.y_array=[]
                for x in self.x_array: 
                    x
                    #x*x
                    self.y_array.append(eval(self.user_function.get()))
                plt.fill_between(self.x_array, self.y_array)
                
                self.plot_widget.grid(row=0, column=0)
                
                self.area= 0
                for i in self.y_array:
                    self.area+=i*self.interval

                #label_area = tk.Label(text=("Результат:",round(area,5)))
                #label_area.grid(row=8,column=8,pady=(10,0))
                self.c='Результат: '+ str(round(self.area,40))
                plt.title(self.c)
            def display_newPlot_left():
                    
                global num_fig
                num_fig+=1
                global x_array
                self.interval = 0.01
                self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                    

                self.root= tk.Tk()
                

                
                self.fig = plt.figure(num_fig)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

                self.plot_widget = self.canvas.get_tk_widget()
                self.y_array=[]
                for x in self.x_array:
                    self.y_array.append(eval(self.user_function.get()))
                plt.fill_between(self.x_array, self.y_array)
                
                self.plot_widget.grid(row=0, column=0)
                
                self.area= 0
                for i in range (-1,len(self.y_array)-1):
                    self.area+=self.y_array[i+1]*self.interval

                #label_area = tk.Label(text=("Результат:",round(area,5)))
                #label_area.grid(row=8,column=8,pady=(10,0))
                self.c='Результат: '+ str(round(self.area,40))
                plt.title(self.c)
            def display_newPlot_middle():
                    
                global num_fig
                num_fig+=1
                global x_array
                self.interval = 0.01
                self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                    

                self.root= tk.Tk()
                

                
                self.fig = plt.figure(num_fig)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

                self.plot_widget = self.canvas.get_tk_widget()
                self.y_array=[]
                for x in self.x_array:
                    self.y_array.append(eval(self.user_function.get()))
                plt.fill_between(self.x_array, self.y_array)
                
                self.plot_widget.grid(row=0, column=0)
                
                self.area= 0
                for i in range (-1,len(self.y_array)-1):
                    self.area+=(self.y_array[i]-1/2*self.interval)*self.interval

                #label_area = tk.Label(text=("Результат:",round(area,5)))
                #label_area.grid(row=8,column=8,pady=(10,0))
                self.c='Результат: '+ str(round(self.area,40))
                plt.title(self.c)
            def display_newPlot_trapezoid():
                    
                global num_fig
                num_fig+=1
                global x_array
                self.interval = 0.01
                self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                    

                self.root= tk.Tk()
                

                
                self.fig = plt.figure(num_fig)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

                self.plot_widget = self.canvas.get_tk_widget()
                self.y_array=[]
                for x in self.x_array:
                    self.y_array.append(eval(self.user_function.get()))
                plt.fill_between(self.x_array, self.y_array)
                
                self.plot_widget.grid(row=0, column=0)
                
                self.area= 0
                for i in range (1,len(self.y_array)-1):
                    self.area+=(self.y_array[i])*self.interval+(self.y_array[i]-self.y_array[i+1])*self.interval

                #label_area = tk.Label(text=("Результат:",round(area,5)))
                #label_area.grid(row=8,column=8,pady=(10,0))
                self.c='Результат: '+ str(round(self.area,40))
                plt.title(self.c)
            def display_newPlot_simpson():
                    
                global num_fig
                num_fig+=1
                global x_array
                self.interval = 0.01
                self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                    

                self.root= tk.Tk()
                

                
                self.fig = plt.figure(num_fig)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

                self.plot_widget = self.canvas.get_tk_widget()
                self.y_array=[]
                for x in self.x_array:
                    self.y_array.append(eval(self.user_function.get()))
                plt.fill_between(self.x_array, self.y_array)
                
                self.plot_widget.grid(row=0, column=0)
                
                self.area= 0
                for i in range (0,len(self.y_array)):
                    if i%2:
                        self.area+=self.y_array[i]*4
                    else:
                        self.area+=self.y_array[i]*2
                self.area = self.area*self.interval/3
                #label_area = tk.Label(text=("Результат:",round(area,5)))
                #label_area.grid(row=8,column=8,pady=(10,0))
                self.c='Результат: '+ str(round(self.area,40))
                plt.title(self.c)

            
            def show_diff():
                global num_fig
                num_fig+=1
                global x_array
                self.interval = 0.01
                self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                self.y_array =[]
                for i in range(len(self.x_array)-1):
                    x=self.x_array[i]
                    self.first_arg=eval(self.user_function.get())
                    x=self.x_array[i+1]
                    self.second_arg=eval(self.user_function.get())
                    self.difference= self.second_arg-self.first_arg
                    self.y_array.append(self.difference*100) 
                self.y_array.append(self.difference*100)
                self.root= tk.Tk()
                    
                self.fig = plt.figure(num_fig)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
    
                self.plot_widget = self.canvas.get_tk_widget()
                plt.plot(self.x_array, self.y_array,color="green")
                    
                self.plot_widget.grid(row=0, column=0)
            
            def dot_diff():
                dot_diff_window = tk.Tk()
                label_function = tk.Label(dot_diff_window,text="Введите функцию",font=18)
                label_function.grid(row=0,column=0,pady=(10,0))
                str_function_diff = tk.StringVar()
                function_entry= tk.Entry(dot_diff_window,textvariable= str_function_diff, font=18)
                function_entry.grid(pady=40,row=1 , column=0)
                label_function = tk.Label(dot_diff_window,text="Введите точку",font=18)
                label_function.grid(row=2,column=0,pady=(10,0))
                x_dot = tk.StringVar()
                x_dot_entry= tk.Entry(dot_diff_window,textvariable= x_dot, font=18)
                x_dot_entry.grid(pady=40,row=3 , column=0)
                # global close_dot
                # close_dot = True
                def solve_diff(): 
                    # global close_dot
                    # if not close_dot:
                    #     label_function_diff.destroy()
                    #     close_dot = False
                    interval = 0.001 
                    def f(x):
                        return(eval(function_entry.get()))

                    final_dot_diff =  (f(eval(x_dot_entry.get())+interval)-f(eval(x_dot_entry.get())-interval))/2/interval
                    label_function_diff = tk.Label(dot_diff_window,text=str(round(final_dot_diff,5)),font=18)
                    label_function_diff.grid(row=7,column=0,pady=(40,0),padx=100)
                    
                but_solve_diff= tk.Button(dot_diff_window,text='Найти', command = solve_diff, width=25, height=4,font=20)
                but_solve_diff.grid(row=4 ,column=0,pady=(0,40),padx=100)
                dot_diff_window.mainloop()
            
            self.button_function_right = tk.Button(self.window,text='Интегрировать(метод правых прямоугольников)', command = display_newPlot_right, width=40, height=4,font=20)
            self.button_function_right.grid(row=7,column=0,pady=(40,0),padx=100)
            self.button_function_left = tk.Button(self.window,text='Интегрировать(метод левых прямоугольников)', command = display_newPlot_left, width=40, height=4,font=20)
            self.button_function_left.grid(row=8,column=0,pady=(40,0),padx=100)
            self.button_function_middle = tk.Button(self.window,text='Интегрировать(метод средних прямоугольников)', command = display_newPlot_middle, width=40, height=4,font=20)
            self.button_function_middle.grid(row=9,column=0,pady=(40,0),padx=100)
            self.button_function_trapezoid = tk.Button(self.window,text='Интегрировать(метод трапеций)', command = display_newPlot_trapezoid, width=40, height=4,font=20)
            self.button_function_trapezoid.grid(row=10,column=0,pady=(40,0),padx=100)
            self.button_function_simpson = tk.Button(self.window,text='Интегрировать(метод Симпсона)', command = display_newPlot_simpson, width=40, height=4,font=20)
            self.button_function_simpson.grid(row=10,column=0,pady=(40,0),padx=100)
            self.button_function_graphics = tk.Button(self.window,text='График Производной Функции', command = show_diff, width=25, height=4,font=20)
            self.button_function_graphics.grid(row=14,column=0,pady=(0,40),padx=100)
            self.button_function_diff = tk.Button(self.window,text='Найти производную в точке', command = dot_diff, width=25, height=4,font=20)
            self.button_function_diff.grid(row=24,column=0,pady=(0,40),padx=100)
            
            def on_closing():
                self.window.destroy()
                global f1close
                f1close = True
            self.window.protocol("WM_DELETE_WINDOW", on_closing)                       
    class Second_ex:
        
        global f2close
        def __init__(self) -> None:
            self.window = tk.Toplevel()
            self.label_function = tk.Label(self.window,text="Введите функцию",font=18)
            self.label_function.grid(row=1,column=0,pady=(40,0))
          
            self.user_function = tk.StringVar()
            self.user_function_entry = tk.Entry(self.window,textvariable=self.user_function, font=18)
            self.user_function_entry.grid(row=2,column=0)
                                
            #entry first x
                                
            self.label_function = tk.Label(self.window,text="Введите нижний предел X",font=18)
            self.label_function.grid(row=3,column=0,pady=(10,0))
                                
            self.first_x = tk.StringVar()
            self.first_x_entry = tk.Entry(self.window,textvariable=self.first_x, font=18)
            self.first_x_entry.grid(row=4,column=0)
                                
            #entry second x
    
            self.label_function = tk.Label(self.window,text="Введите верхний предел X",font=18)
            self.label_function.grid(row=5,column=0,pady=(10,0))
            
            self.second_x = tk.StringVar()
            self.second_x_entry = tk.Entry(self.window,textvariable=self.second_x, font=18)
            self.second_x_entry.grid(row=6,column=0)
            def display_result():
                self.result_window = tk.Tk()
                self.interval = 0.01
                try:
                    self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                except:
                    pass
                self.y_array=[]
                try:
                    for x in self.x_array:
                        self.y_array.append(eval(self.user_function.get()))
                except:
                    pass
                # self.label_result = tk.Label(self.window,text="XXXXXXXXXXXX",font=18)
                # self.label_result.grid(row=8,column=0,pady=(10,0))
                self.result_window.title('Работа с canvas')
                canvas = Canvas(self.result_window,width=800,height=800,bg="gray",cursor="pencil")
                canvas.pack()
                canvas.create_line(400,0,400,800,width=2,fill="yellow")
                canvas.create_line(0,400,800,400,width=2,fill="yellow")
                canvas.create_text(410,20,text="Y", font="Verdana 14",fill = 'white')
                canvas.create_text(780,380,text="X", font="Verdana 14",fill = 'white')
                s = 0
                for i in range(-9,10,1):
                    s+=1
                    text=i
                    canvas.create_text(800/20*s,380,text=text, font="Verdana 14",fill = 'white')
                    canvas.create_line(800/20*s,400,800/20*s,401,width=2,fill="black")

                s = 0   
                for i in range(9,-10,-1):
                    s+=1
                    text=i
                    canvas.create_text(410,800/20*s,text=text, font="Verdana 14",fill = 'white')
                    canvas.create_line(400,800/20*s,401,800/20*s,width=2,fill="black")

                def function_selfPlot(d):
                    x = d/50
                    # if (self.user_function.get()+400)<0:
                    #     f=abs(self.user_function.get())
                    # else:
                    #     f=-self.user_function.get()
                    return (50*eval(self.user_function.get()))
                # for i in range (int(800/int(self.first_x.get())),int(800/int(self.second_x.get())),1):
                solve_array=[]
                for i in range (int(self.first_x.get())*50,int(self.second_x.get())*50,2):
                    try: 
                        # sleep(0.0001)
                        canvas.create_line(400+i,400-function_selfPlot(i),400+i+2,400-function_selfPlot(i+2),width=2,fill="yellow")
                        # canvas.update()
                        if -function_selfPlot(i)>0 and -function_selfPlot(i+2)<=0:
                            solve_array.append((i+1)/50)
                        if -function_selfPlot(i)<0 and -function_selfPlot(i+2)>=0:
                            solve_array.append((i+1)/50)
                        
                    except:
                        pass
                result_string= "Корни уравнения:\n"
                count=1
                for i in solve_array: 
                    result_string+= str(count)+"."+str(i)+"\n"
                    count+=1
                self.label_function = tk.Label(self.window,text=result_string,font=18)
                self.label_function.grid(row=9,column=0,pady=(10,0))
            class create_interface_diff:
                def __init__(self) -> None:
                    
                        
                    self.window = tk.Toplevel()
                    self.label_function = tk.Label(self.window,text="Введите функцию",font=18)
                    self.label_function.grid(row=1,column=0,pady=(40,0))

                    self.user_function = tk.StringVar()
                    self.user_function_entry = tk.Entry(self.window,textvariable=self.user_function, font=18)
                    self.user_function_entry.grid(row=2,column=0)

                    #entry first x

                    self.label_function = tk.Label(self.window,text="Введите Y0",font=18)
                    self.label_function.grid(row=3,column=0,pady=(10,0))

                    self.first_y = tk.StringVar()
                    self.first_y_entry = tk.Entry(self.window,textvariable=self.first_y, font=18)
                    self.first_y_entry.grid(row=4,column=0)

                    self.label_function = tk.Label(self.window,text="Введите X0",font=18)
                    self.label_function.grid(row=5,column=0,pady=(10,0))

                    self.first_x = tk.StringVar()
                    self.first_x_entry = tk.Entry(self.window,textvariable=self.first_x, font=18)
                    self.first_x_entry.grid(row=6,column=0)

                    #entry second x

                    self.label_function = tk.Label(self.window,text="Введите X1",font=18)
                    self.label_function.grid(row=7,column=0,pady=(10,0))

                    self.second_x = tk.StringVar()
                    self.second_x_entry = tk.Entry(self.window,textvariable=self.second_x, font=18)
                    self.second_x_entry.grid(row=8,column=0)    

                    self.label_function = tk.Label(self.window,text="Введите Xi",font=18)
                    self.label_function.grid(row=9,column=0,pady=(10,0))

                    self.xi = tk.StringVar()
                    self.xi_entry = tk.Entry(self.window,textvariable=self.xi, font=18)
                    self.xi_entry.grid(row=10,column=0)    
                    def find_diff():
                        x0 = int(self.first_x.get())
                        x1 = int(self.second_x.get())
                        xi = int(self.xi.get())
                        y0 = int(self.first_y.get())
                        self.x_array=[]
                        self.interval = x1-x0
                        def diff_funtion(x,y):
                            print (eval(self.user_function.get()))
                            return eval(self.user_function.get())
                        try:
                            self.x_array = np.arange(eval(self.first_x.get()), eval(self.xi.get()),self.interval)
                        except:
                            pass
                        self.y_array=[]
                        self.xposition=0
                        self.yposition=0
                        y_coord=[self.yposition]
                        y_coord.append(y0)
                        foot=0
                        for i in range(len(self.x_array)):
                            k1=diff_funtion(self.x_array[i],y_coord[i])
                            k2=diff_funtion(self.x_array[i]+self.interval/2, y_coord[i]+self.interval*k1*0.5)
                            k3=diff_funtion(self.x_array[i]+self.interval/2, y_coord[i]+self.interval*k2*0.5)
                            k4=diff_funtion(self.x_array[i]+self.interval,   y_coord[i]+self.interval*k3)
                            foot+=1
                            dy=self.interval*(k1+2*k2+2*k3+k4)/6

    
                            y_coord.append(dy)
                        for i in y_coord:
                            i=str(i)+'\n'
                        self.final = tk.Label(self.window,text=str(y_coord),font=18)
                        self.final.grid(row=29,column=0,pady=(10,0))

                    self.button_function_diff = tk.Button(self.window,text='Решить дифференциальное уравнение', command = find_diff, width=40, height=4,font=20)
                    self.button_function_diff.grid(row=19,column=0,pady=(40,40),padx=100)

            def display_diff_window():
                interface =  create_interface_diff()
                
            def on_closing():
                self.window.destroy()
                global f2close
                f2close = True
            self.window.protocol("WM_DELETE_WINDOW", on_closing)  

            self.button_function = tk.Button(self.window,text='Найти корни уравнения', command = display_result, width=40, height=4,font=20)
            self.button_function.grid(row=7,column=0,pady=(40,10),padx=100)

            self.button_function_diff = tk.Button(self.window,text='Решить дифференциальное уравнение', command = display_diff_window, width=40, height=4,font=20)
            self.button_function_diff.grid(row=8,column=0,pady=(40,40),padx=100)
    class Third_ex:
        def __init__(self) -> None:
            self.window = tk.Toplevel()
            self.label_function = tk.Label(self.window,text="Введите функцию по x",font=18)
            self.label_function.grid(row=1,column=0,pady=(40,0))

            self.user_functionX = tk.StringVar()
            self.user_functionX_entry = tk.Entry(self.window,textvariable=self.user_functionX, font=18)
            self.user_functionX_entry.grid(row=2,column=0)

            self.label_functionY = tk.Label(self.window,text="Введите функцию по y",font=18)
            self.label_functionY.grid(row=3,column=0,pady=(40,0))
          
            self.user_functionY = tk.StringVar()
            self.user_functionY_entry = tk.Entry(self.window,textvariable=self.user_functionY, font=18)
            self.user_functionY_entry.grid(row=4,column=0,pady=(0,40))
                                

                                
            self.label_function = tk.Label(self.window,text="Введите k",font=18)
            self.label_function.grid(row=5,column=0,pady=(10,0))
                                
            self.k = tk.StringVar()
            self.k_entry = tk.Entry(self.window,textvariable=self.k, font=18)
            self.k_entry.grid(row=6,column=0)

            self.label_function = tk.Label(self.window,text="Введите r",font=18)
            self.label_function.grid(row=7,column=0,pady=(10,0))

            self.r = tk.StringVar()
            self.r_entry = tk.Entry(self.window,textvariable=self.r, font=18)
            self.r_entry.grid(row=8,column=0)

            self.label_function = tk.Label(self.window,text="Введите R",font=18)
            self.label_function.grid(row=9,column=0,pady=(10,0))
                                
            self.R = tk.StringVar()
            self.R_entry = tk.Entry(self.window,textvariable=self.R, font=18)
            self.R_entry.grid(row=10,column=0)

            self.label_function = tk.Label(self.window,text="Введите m",font=18)
            self.label_function.grid(row=11,column=0,pady=(10,0))
                                
            self.m = tk.StringVar()
            self.m_entry = tk.Entry(self.window,textvariable=self.m, font=18)
            self.m_entry.grid(row=12,column=0)

            self.label_function = tk.Label(self.window,text="Введите mas",font=18)
            self.label_function.grid(row=13,column=0,pady=(10,0))

            self.mas = tk.StringVar()
            self.mas_entry = tk.Entry(self.window,textvariable=self.mas, font=18)
            self.mas_entry.grid(row=14,column=0)
                                
            #entry second x
    
            self.label_function = tk.Label(self.window,text="Введите нижний предел t",font=18)
            self.label_function.grid(row=15,column=0,pady=(10,0))
            
            self.first_t = tk.StringVar()
            self.first_t_entry = tk.Entry(self.window,textvariable=self.first_t, font=18)
            self.first_t_entry.grid(row=16,column=0)

            self.label_function = tk.Label(self.window,text="Введите верхний предел t",font=18)
            self.label_function.grid(row=17,column=0,pady=(10,0))
            
            self.second_t = tk.StringVar()
            self.second_t_entry = tk.Entry(self.window,textvariable=self.second_t, font=18)
            self.second_t_entry.grid(row=18,column=0)

            def start_animation():
                self.t_array = []
                self.result_window = tk.Tk()
                self.interval = 0.002
                try:
                    self.t_array = np.arange(eval(self.first_t.get()), eval(self.second_t.get()),self.interval)
                except:
                    pass
                self.y_array=[]
                # try:
                #     for x in self.t_array:
                #         self.y_array.append(eval(self.user_function.get()))
                # except:
                #     pass
                # self.label_result = tk.Label(self.window,text="XXXXXXXXXXXX",font=18)
                # self.label_result.grid(row=8,column=0,pady=(10,0))
                self.result_window.title('Работа с canvas')
                canvas = Canvas(self.result_window,width=800,height=800,bg="gray",cursor="pencil")
                canvas.pack()
                canvas.create_line(400,0,400,800,width=2,fill="yellow")
                canvas.create_line(0,400,800,400,width=2,fill="yellow")
                canvas.create_text(410,20,text="Y", font="Verdana 14",fill = 'white')
                canvas.create_text(780,380,text="X", font="Verdana 14",fill = 'white')
                
                def function_selfPlotX(d):
                    string_fun=self.user_functionX.get()
                    t = d/float(self.mas.get())
                    r = self.r.get()
                    R = self.R.get()
                    k = self.k.get()
                    m = self.m.get()
                    
                    string_fun=string_fun.replace('r',r)
                    string_fun=string_fun.replace('R',R)
                    string_fun=string_fun.replace('k',k)
                    string_fun=string_fun.replace('m',m)
                    

                    return (float(self.mas.get())*eval(string_fun))
                def function_selfPlotY(d):
                    string_fun=self.user_functionY.get()
                    t = d/float(self.mas.get())
                    r = self.r.get()
                    R = self.R.get()
                    k = self.k.get()
                    m = self.m.get()
                    
                    string_fun=string_fun.replace('r',str(r))
                    string_fun=string_fun.replace('R',str(R))
                    string_fun=string_fun.replace('k',str(k))
                    string_fun=string_fun.replace('m',str(m))
                    
                    
                    return (float(self.mas.get())*eval(string_fun))
                user_functionX=self.user_functionX.get()
                user_functionY=self.user_functionY.get()
                for t in range(len(self.t_array)):
                    global COLORS
                    t=t*float(self.mas.get())
                    # canvas.create_line(0,0,400,400,width=2,fill="yellow")
                    sleep(0.0001)
                    canvas.create_line(400+function_selfPlotX(t),400-function_selfPlotY(t),400+function_selfPlotX(t+2),400-function_selfPlotY(t+2),width=2,fill=COLORS[random.randint(0,len(COLORS)-1)])
                    canvas.update()
                    
            




            def on_closing():
                self.window.destroy()
                global f3close
                f3close = True
            self.window.protocol("WM_DELETE_WINDOW", on_closing)  
            self.button_function = tk.Button(self.window,text='Начать анимацию заданных функций', command = start_animation, width=40, height=4,font=20)
            self.button_function.grid(row=19,column=0,pady=(40,10),padx=100)
    class Fourth_ex:
        def __init__(self) -> None:
            
            self.window = tk.Toplevel()
            self.label_function = tk.Label(self.window,text="Введите массив точек по X через запятую",font=18)
            self.label_function.grid(row=1,column=0,pady=(40,0))

            self.user_arrayX = tk.StringVar()
            self.user_arrayX_entry = tk.Entry(self.window,textvariable=self.user_arrayX, font=18)
            self.user_arrayX_entry.grid(row=2,column=0)


            
            self.label_function = tk.Label(self.window,text="Введите массив точек по Y через запятую",font=18)
            self.label_function.grid(row=3,column=0,pady=(40,0))

            self.user_arrayY = tk.StringVar()
            self.user_arrayY_entry = tk.Entry(self.window,textvariable=self.user_arrayY, font=18)
            self.user_arrayY_entry.grid(row=4,column=0)
            
            


            self.label_function = tk.Label(self.window,text="Введите нижний предел приближения",font=18)
            self.label_function.grid(row=5,column=0,pady=(10,0))
            self.first_x = tk.StringVar()
            self.first_x_entry = tk.Entry(self.window,textvariable=self.first_x, font=18)
            self.first_x_entry.grid(row=6,column=0)
            #entry second x
            self.label_function = tk.Label(self.window,text="Введите вверхний предел приближения",font=18)
            self.label_function.grid(row=7,column=0,pady=(10,0))
            self.second_x = tk.StringVar()
            self.second_x_entry = tk.Entry(self.window,textvariable=self.second_x, font=18)
            self.second_x_entry.grid(row=8,column=0)    
                                

                                


            self.num_fig=0
            def start_lagrange():
                self.num_fig+=1
                global x_array
                self.interval = 0.01
                # self.x_array = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                    

                self.root= tk.Tk()
                

                
                self.fig = plt.figure(self.num_fig)
                self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

                self.plot_widget = self.canvas.get_tk_widget()
                self.y_array=[]

                def l(i,x):
                    l = 1
                    for j in range (len(self.X_array)):
                        if j!=i:
                            l*=(x-self.X_array[j])/(self.X_array[i]-self.X_array[j])
                    return l
                def lagrange(x):
                    y=0
                    for i in range (len(self.X_array)):
                        y+=self.Y_array[i]*l(i,x)
                        
                    return y

                # [int(numeric_string) for numeric_string in (self.user_arrayX.get().split(','))]
                self.X_array = [int(numeric_string) for numeric_string in (self.user_arrayX.get().split(','))]
                self.Y_array = [int(numeric_string) for numeric_string in (self.user_arrayY.get().split(','))]
                # self.X_array = map(int,(self.user_arrayX.get().split(',')))
                # self.Y_array = map(int,(self.user_arrayY.get().split(',')))
                
                self.x_array_final = np.arange(eval(self.first_x.get()), eval(self.second_x.get()),self.interval)
                self.y_array_final =[]
                self.d=0
                for x in self.x_array_final:
                    self.y_array_final.append(lagrange(x))
                    self.d+=1






                plt.fill_between(self.x_array_final, self.y_array_final)
                
                self.plot_widget.grid(row=0, column=0)

                self.area= 0
                for i in self.y_array:
                    self.area+=i*self.interval

                #label_area = tk.Label(text=("Результат:",round(area,5)))
                #label_area.grid(row=8,column=8,pady=(10,0))
                self.c='Результат: '+ str(round(self.area,40))
                plt.title(self.c)
                



            def on_closing():
                self.window.destroy()
                global f4close
                f4close = True
            self.window.protocol("WM_DELETE_WINDOW", on_closing)  
            self.button_function = tk.Button(self.window,text='Приближение методом Лагранжа', command = start_lagrange, width=40, height=4,font=20)
            self.button_function.grid(row=19,column=0,pady=(40,10),padx=100)
    class MainWindow:
        def __init__(self) -> None:
            mainWindow =tkinter.Tk()
            # mainWindow.attributes("-topmost",True)
            global f1close
            f1close = True
            def set_first_ex():
                global f1close
                if f1close:
                    first_ex = First_ex()
                    f1close = False

            but_1ex=tkinter.Button(text="Первая задача", font= 18, width=25,height=5, command=set_first_ex)
            but_1ex.grid(row=0,column=0)

            global f2close
            f2close = True
            def set_Second_ex():
                global f2close
                if f2close:
                    second_ex = Second_ex()
                    f2close = False

            but_2ex=tkinter.Button(text="Вторая задача", font= 18, width=25,height=5, command=set_Second_ex)
            but_2ex.grid(row=1,column=0)

            global f3close
            f3close = True
            def set_Second_ex():
                global f3close
                if f3close:
                    second_ex = Third_ex()
                    f3close = False

            but_3ex=tkinter.Button(text="Третья задача", font= 18, width=25,height=5, command=set_Second_ex)
            but_3ex.grid(row=2,column=0)

            global f4close
            f4close = True
            def set_Second_ex():
                global f4close
                if f4close:
                    second_ex = Fourth_ex()
                    f4close = False

            but_4ex=tkinter.Button(text="четвертая задача", font= 18, width=25,height=5, command=set_Second_ex)
            but_4ex.grid(row=3,column=0)
            
            mainWindow.mainloop()
            
    Main = MainWindow() 
main()
