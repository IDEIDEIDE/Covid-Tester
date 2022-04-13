#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:21:30 2022

@author: clockshield
"""
from tkinter import *
import random
from PIL import ImageTk, Image
import os
from tkinter import filedialog
root=Tk()
root.title("lol")
root.minsize(650, 650)
root.maxsize(650, 650)

question1_radiobutton = StringVar(value = "0")
question1_label = Label(root, text="Do you not want to go school because school sucks")
question1_label.pack()
question1_r1 = Radiobutton(root, text = "Yes", variable = question1_radiobutton, value = "yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "No", variable = question1_radiobutton, value = "no")
question1_r2.pack()

question2_radiobutton = StringVar(value = "0")
question2_label = Label(root, text="Do you have symptoms of covid")
question2_label.pack()
question2_r1 = Radiobutton(root, text = "Yes", variable = question2_radiobutton, value = "yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "No", variable = question2_radiobutton, value = "no")
question2_r2.pack()

question3_radiobutton = StringVar(value = "0")
question3_label = Label(root, text="Do u feel like u have covid")
question3_label.pack()
question3_r1 = Radiobutton(root, text = "Yes", variable = question3_radiobutton, value = "yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "No", variable = question3_radiobutton, value = "no")
question3_r2.pack()

def results():
    score = 0
    if question1_radiobutton.get() == "yes":
        score = score+20
        
    if question2_radiobutton.get() == "yes":
        score = score+20
        
    if question3_radiobutton.get() == "yes":
        score = score+20
        
    if score <= 20:
        test_results["text"] = "Results : You don't have covid"
rr     elif score > 20 and score < 60:
        test_results["text"] = "Results : You might have covid so be cautious"
    else:
       test_results["text"] = "Results : You have covid so don't go to school"
       
    
btn = Button(root, text = "Test!", command=results)
btn.pack()
test_results = Label(root)
test_results.pack()
        
      
root.mainloop()
      
      
      
      
      
      