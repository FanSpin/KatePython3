#Code Coach clock clone
#tkinter for graphics
from tkinter import *
from tkinter.ttk import *
#time server
from time import strftime
#makes windo,i think
root = Tk()
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
