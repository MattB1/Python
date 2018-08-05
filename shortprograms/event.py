from tkinter import *
from tkinter import ttk

def handleEnter(event):
    l["text"] = "Mouse moved inside"

def handleLeave(event):
    l["text"] = "Mouse moved outside"

def handleClick(event):
    l["text"] = "Clicked left button"

def handleDoubleClick(event):
    l["text"] = "Double clicked"

def handleRightDrag(event):
    l["text"] = "Right button drag to {}, {}".format(event.x, event.y)


root = Tk()
l = ttk.Label(root, text = "Starting...")
l.grid()

l.bind("<Enter>", handleEnter)
l.bind("<Leave>", handleLeave)
l.bind("<1>", handleClick)
l.bind("<Double-1>", handleDoubleClick)
l.bind("<B3-Motion>", handleRightDrag)

root.mainloop()
