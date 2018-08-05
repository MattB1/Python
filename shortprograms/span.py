from tkinter import *
from tkinter import ttk

root = Tk()
content = ttk.Frame(root, padding = (3, 3, 12, 12))
frame = ttk.Frame(content, borderwidth = 5, relief = "sunken", width = 200, height = 100)

namelbl = ttk.Label(content, text = "Name")
name = ttk.Entry(content)
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text = "One", variable = onevar, onvalue = True, offvalue = False)
two = ttk.Checkbutton(content, text = "Two", variable = onevar, onvalue = True, offvalue = False)
three = ttk.Checkbutton(content, text = "Three", variable = onevar, onvalue = True, offvalue = False)

ok = ttk.Button(content, text = "Okay")
cancel = ttk.Button(content, text = "Cancel")

content.grid(column = 0, row = 0, sticky = (N, S, E, W))
frame.grid(column = 0, row = 0, columnspan = 3, rowspan = 2, sticky = (N, S, E, W))
namelbl.grid(column = 3, row = 0, columnspan = 2, sticky = (N, W), padx = 5)
name.grid(column = 5, row = 0, columnspan = 2, sticky = (N, E, W), padx = 5, pady = 5)
one.grid(column = 0, row = 1)
two.grid(column = 1, row = 1)
three.grid(column = 2, row = 1)
ok.grid(column = 3, row = 1)
cancel.grid(column = 4, row = 1)


root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

content.columnconfigure(0, weight = 3)
content.columnconfigure(1, weight = 3)
content.columnconfigure(2, weight = 3)
content.columnconfigure(3, weight = 1)
content.columnconfigure(4, weight = 1)
content.rowconfigure(1, weight = 1)

root.mainloop()
