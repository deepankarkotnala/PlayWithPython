# Play with Tkinter

## Find IP and MAC Address of your Device

```python

import tkinter as tk
from tkinter.messagebox import showinfo
import socket
from getmac import getmac

win = tk.Tk()
win.config(bg="#e3e3e3")
win.title("Find IP and MAC Address")
win.geometry('450x200')

T = tk.Text(win, height=2, width=60)
T.pack()
T.insert(tk.END, "Find the IP Address and MAC address of your device")


# To find IP Address
def ip():
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)
    showinfo("IP Address",f"IP Address : {ip_add}")

# To find MAC Address
def mac():
    mac_add = getmac.get_mac_address()
    showinfo("MAC Address",f"MAC Address : {mac_add}")

# To create buttons
ip_button = tk.Button(win, text = "Show IP Address", bg="#000000", fg="#e3e3e3", height = 1, width = 18,
	font = ("calibri", 16, "bold"), command=ip)
ip_button.pack()

mac_button = tk.Button(win, text = "Show MAC Address", bg="#000000", fg="#e3e3e3", height = 1, width = 18,
	font = ("calibri", 16, "bold"), command=mac)
mac_button.pack()

win.mainloop()

```

## Tkinter Messagebox

```python

from tkinter import *
from tkinter import messagebox
import tkinter as tk

parent = tk.Tk()
parent.title("Message Box Demo")
parent.geometry('600x300')

T = tk.Text(parent, height=80, width=80)
T.pack()
T.insert(tk.END, "There are the terms and conditions.\nAll your data is mine. Please accept these in order to use this software.\nJust Kidding! Blah Blah Blah .. Noone will ever read this. Ok Bye!")

result1 = messagebox.askokcancel("Title ", "Do you accept the terms and conditions?")
print(result1) # Yes = True, No = False

result2 = messagebox.askyesno("Title2","Are you sure?")
print(result2) # Yes = True, No = False

result3 = messagebox.askyesnocancel("Title3",'Pakka na?')
print(result3) # Yes = True, no = False, cancel = None

messagebox.showinfo("Title","Tkinter messagebox looks like this")
messagebox.showwarning("warning", "This is a tkinter warning box")
messagebox.showerror("error", "And here is an error! OOPS!")

parent.mainloop()

```

## Get List of Files in a Folder (In Windows)

```python

import os
from tkinter import *
import pandas as pd
import tkinter.scrolledtext as scrolledtext


#cwd = os.getenv("HOME")

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
entry2.pack(padx=5, ipady=3, expand=True)
entry2.focus_set()

frame3 = Frame(frame)
frame3.pack(fill=X)

txt = scrolledtext.ScrolledText(frame3)
txt['font'] = ('Monospace', '11')
txt.pack(fill=X)
txt.insert(END, 'List of files present in the directory will be shown here')
txt.config(font=("Courier", 11))

frame.pack()

exitButton = Button(root,text='Exit', fg ='red', height=2, width=11, command=root.destroy)
exitButton['font'] = ('Monospace', '11')
exitButton.pack(side=RIGHT, padx=5, pady=20)
submitButton = Button(root,text='Submit', fg ='black', height=2, width=11, command=getpath)
submitButton['font'] = ('Monospace', '11')
submitButton.pack(side=RIGHT, padx=5, pady=20)


root.mainloop()

```
## Check out the linux version as well. It's just slightly different.
