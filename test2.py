import requests
import json
import webbrowser
from tkinter import *


window_1=Tk()
window_1.title('Button 1')
window_1.geometry('1000x750')
window_1.configure(bg='red')
window_1.iconbitmap('1.ico')

#commands for the buttons
def Ingredients_1():
    ingredient_label_1=Label(window_1,text=ingredients).grid(column=0,row=1,columnspan=50)
#def Instructions_1():

#making the title bar for the window
title_frame_1=Frame(window_1,bg='white',width=1000,height=100).grid(row=0,column=0,columnspan=5)

#making the buttons for the title bar
ingredients_1=Button(title_frame_1,text="Ingredients",command=Ingredients_1)
ingredients_1.grid(column=0,row=0)
instructions_1 = Button(title_frame_1, text="Instructions")
instructions_1.grid(column=1, row=0)



window_1.mainloop()