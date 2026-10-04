#Code Coach clock clone

from tkinter import *       #tkinter for graphics
from tkinter.ttk import *   #tkinter for graphics

from time import strftime   #time server

root = Tk()                  #makes window?
root.title("digital clock")
#functions
def time():
    string = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label>after(1000, time)

label = label(root, font=(ds-digital,80),background="black",foreground="cyan")
label = pack(anchor="center")

time()
mainloop()
