# AutoCor
AutoCor is developped in python, it uses some functions from the OpenCV library to automatically detect and extract the answers from a student's exam copy (MCQs), then compare it with the correct answers in order to evaluate the score.

To the left is an exam paper with all the correct answers checked, which will be compared to the student's answers in the exam paper to the right
![alt text](https://i.ibb.co/njMDqD6/Screenshot-from-2021-07-17-23-37-15.png)

![alt text](https://i.ibb.co/pnpWZR5/Screenshot-from-2021-07-17-23-38-19.png)
By clicking Get Score, the student's score is shown in the GUI, a text file coutaining the student's answers is saved in the working directory, and a tupple with the student's first name, last name and score is added to a list that can countain information of multiple students and can be later exported ( with Export List ) as a csv file.

I've added an empty copy ( blank.png ) for everyone who wants to play with and test AutoCor

# Requirements
  - opencv-python Library
  - tkinter Library

To launch AutoCor, you can execute the GUI.py file
