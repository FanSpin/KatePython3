#Code Coach clock clone

from tkinter import *       #tkinter for graphics
from tkinter.ttk import *   #tkinter for graphics

from time import strftime   #time server

root = Tk()                  #tkinter tool --creates main window 
root.title("digital clock")  #adds title to main window
#functions
def time():                  #python only --works outside tkinter
    string = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label>after(1000, time)

label = label(root, font=(ds-digital,80),background="black",foreground="cyan")
label = pack(anchor="center")

time()
mainloop()
