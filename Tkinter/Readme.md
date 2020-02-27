# Tkinter Messagebox

## A basic demonstration of messagebox in Tkinter.

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
