from os import name
from numpy.core.fromnumeric import size
import numpy as np
import Algo
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd

import cv2 as cv
font_tuple = ("Gothic", 10)
score_font = ("Gothic", 25, "bold")

d = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 0:'no answer'}
global list
list = {"name":[], "last name":[], "score": []}

def uploadCopy():
    global copy_path
    copy_path = askopenfilename(filetypes=[('Image Files', '*png')])
    successufuly = Label(text="Check",background="white", foreground="green", font=("Gothic", 8))
    successufuly.place(x=410,y=100)

def uploadSolution():
    global solution_path
    solution_path = askopenfilename(filetypes=[('Image Files', '*png')])
    successufuly = Label(text="Check",background="white", foreground="green", font=("Gothic", 8))
    successufuly.place(x=410,y=135)


def do():
    img = cv.imread(solution_path)
    solution = Algo.answers_from_image(img)

    img = cv.imread(copy_path)
    answers = Algo.answers_from_image(img)

    score = Algo.get_score(img,solution)

    list["name"].append(EName.get())
    list["last name"].append(ElastName.get())
    list["score"].append(score)

    #f=open("/home/ayoub/Desktop/CorConc/"+EName.get()+"_"+ElastName.get()+"_answers.txt", "a+")
    f=open(EName.get()+'_'+ElastName.get()+'_answers.txt', "a+")
    for i in range(64):
        f.write("Q"+str(i+1)+": "+str(answers[i])+" | ")


    number_of_students = Label(text = "number of students: "+str(len(list["name"])),background="white", foreground="green", font=("Gothic", 8))
    number_of_students.place(x=375,y=317)

    sc_label = Label(text=str(score)+" / 64",background="white", font=score_font)
    sc_label.place(x=100,y=260)

def export():
    to_export = pd.DataFrame(list)

    #to_export.to_csv("/home/ayoub/Desktop/CorConc/list_"+str(datetime.now().strftime("%H_%M_%S"))+".csv")
    to_export.to_csv(str(datetime.now().strftime("%H_%M_%S"))+'.csv')
    exported = Label(text = "exported",background="white", foreground="green", font=("Gothic", 8))
    exported.place(x=290, y=245)

root = Tk()
# This is the section of code which creates the main window
root.geometry('500x350')
root.configure(background="white")
root.title('Auto Correct')

#get score
button = Button(text = 'Get Score', command = do, height=1, width=10)
button.place(x=100, y=210)

#export
button = Button(text = 'Export list', command = export, height=1, width=10)
button.place(x=290, y=210)

# first name
EName=Entry(root)
EName.place(x=230, y=20)
labelName = Label(text="First Name",background="white", font=font_tuple)
labelName.place(x=100,y=47)

# last name
ElastName=Entry(root)
ElastName.place(x=230, y=50)
labelLastName = Label(text="Last Name",background="white", font=font_tuple)
labelLastName.place(x=100,y=17)

#upload exam copy
up = Label(text="Upload the exam copy",background="white", font=font_tuple)
up.place(x=100,y=100)

#upload
button = Button(text = 'Upload', command = uploadCopy, height=1, width=8)
button.place(x=300, y=95)

#solution
sol = Label(text="Upload the solution",background="white", font=font_tuple)
sol.place(x=100,y=133)
button = Button(text = 'Upload', command = uploadSolution, height=1, width=8)
button.place(x=300, y=130)

root.mainloop()