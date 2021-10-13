# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:49:37 2021

@author: yatha
"""

from tkinter import *
import random

root =Tk()
root.title("Random alphabet genrator")
root.geometry("400x400")
root.configure(background = "dark green")

alpha_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
random_no1 =["7"]
random_no2 =["13"]
random_no3 =["12"]
random_no4 =["2"]
random_no5 =["17"]

random_alpha1 = alpha_list [random_no1]
random_alpha2 = alpha_list[random_no2]
random_alpha3 = alpha_list[random_no3]
random_alpha4 = alpha_list[random_no4]
random_alpha5 = alpha_list[random_no5]
print (alpha_list)
label1 = Label (root,bg = "red",fg =  "yellow")
label1.place(relx = 0.5,rely = 0.7,anchor = CENTER)

def randomnumber():
    r_no = random.randint(0,7)
    random_no1 = alpha_list[alpha_list]
    print ("the word randomly genrated is  "+ alpha_list)
    label1["text"]="your lucky friend is "+ alpha_list
    
btn1 = Button (root,text = "Who is your lucky friend?",command = randomnumber)
btn1.place(relx = 0.5, rely = 0.5,anchor = CENTER)
root.mainloop()