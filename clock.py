#Code Coach clock clone

from tkinter import *              #tkinter for graphics
from tkinter.ttk import *          #tkinter for graphics

from time import strftime          #time server

root = Tk()                        #tkinter tool --creates main window
root.title("digital clock")        #adds title to main window

def time():                        #python only --works outside tkinter
    now = strftime('%H:%M:%S:%p')  #the time right now in a string
    label.config(text=now)
    label.after(1000, time)

label = Label(root, font=("ds-digital",80,"bold"),background="black",foreground="cyan")
label.pack(anchor="center")   #remove label.pack

time()                              # run once
mainloop()                          # dont close window, yet
                                    #try root.mainloop
