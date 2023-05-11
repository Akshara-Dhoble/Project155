# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:36:15 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import*
import random
root = Tk()
root.title("Colours")
root.geometry("400x400")

dictionary = {"Colours" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def background_color_change():
    random_color = random.randint(0 , 478)
    print(dictionary["Colours"][rendom_color])
    root.configure(background= dictionary["Colours"][rendom_color])
    
btn_1 = Button(root , text = "Click Me" , command=background_color_change) 
btn_1.place(relx=0.5 , rely=0.5 , anchor=CENTER)   
    
rrot.mainloop()