import os
from tkinter import *
import pandas as pd
import tkinter.scrolledtext as scrolledtext


cwd = os.getenv("HOME")

root = Tk()
root.geometry('800x500')
root.title('Application')

files_in_dir=[]

def getpath():
    global entry2
    string = entry2.get()
    files_in_dir=""
    try:
        os.remove("text.txt")
        with open("text.txt", "w"):
            pass
    except:
        with open("text.txt", "w"):
            pass

    try:
        files_in_dir = pd.Series(os.listdir(string))
        for file_name in files_in_dir:
            with open('text.txt', 'a') as f: 
                f.write("\n{}".format(file_name))
        txt.delete('1.0', END)
        with open("text.txt", "r") as f:
            txt.insert(END, f.read()) 

    except FileNotFoundError:
        print("\nException occurred!\nThe directory {} does not exist. Please check the path and try again".format(string))
    except Exception as ex:
        print("Exception occurred", str(ex))


frame = Frame(root, height=500, width=800) 

frame1 = Frame(frame)
frame1.pack(fill=X)

lbl1 = Label(frame1, text="Enter the directory path to check the contents")
lbl1['font'] = ('Monospace', '11')
lbl1.pack(side=LEFT, padx=5, pady=5)

frame2 = Frame(frame)
frame2.pack(fill=X)

lbl2 = Label(frame2, text="Directory", width=11)
lbl2['font'] = ('Monospace', '11')
lbl2.pack(side=LEFT, padx=5, pady=5)

entry2 = Entry(frame2, relief=SUNKEN, width=40)
entry2.insert(0, cwd)
entry2.pack(padx=5, ipady=3, expand=True)
entry2.focus_set()

frame3 = Frame(frame)
frame3.pack(fill=X)

txt = scrolledtext.ScrolledText(frame3)
txt['font'] = ('Monospace', '11')
txt.pack(fill=X)
txt.config(font=("Courier", 10))

frame.pack()

exitButton = Button(root,text='Exit', fg ='red', height=2, width=11, command=root.destroy)
exitButton['font'] = ('Monospace', '11')
exitButton.pack(side=RIGHT, padx=5, pady=20)
submitButton = Button(root,text='Submit', fg ='black', height=2, width=11, command=getpath)
submitButton['font'] = ('Monospace', '11')
submitButton.pack(side=RIGHT, padx=5, pady=20)


root.mainloop()