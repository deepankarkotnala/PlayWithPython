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
