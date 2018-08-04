# Program to determine the cleanliness of toilets in the CodeTown Council area
# Author: Matt Bubb
# Date: 20th May 2017


from tkinter import *
from tkinter import ttk

averages = []  # A list of all the numbers clicked/touched by the user

"""Functions for each button that when clicked, will add that number to a list, determine the average and reconfigure
the text in the label 'rating' located in 'Frame3' to be the result"""


def click1():
    averages.append(1)
    average = float(sum(d for d in averages)) / len(averages)
    print(averages, average)
    rating.config(text="This location has an average cleanliness rating of {}".format(float("{0:.2f}".format(average))))
    return


def click2():
    averages.append(2)
    average = float(sum(d for d in averages)) / len(averages)
    print(averages, average)
    rating.config(text="This location has an average cleanliness rating of {}".format(float("{0:.2f}".format(average))))
    return


def click3():
    averages.append(3)
    average = float(sum(d for d in averages)) / len(averages)
    print(averages, average)
    rating.config(text="This location has an average cleanliness rating of {}".format(float("{0:.2f}".format(average))))
    return


def click4():
    averages.append(4)
    average = float(sum(d for d in averages)) / len(averages)
    print(averages, average)
    rating.config(text="This location has an average cleanliness rating of {}".format(float("{0:.2f}".format(average))))
    return


def click5():
    averages.append(5)
    average = float(sum(d for d in averages)) / len(averages)
    print(averages, average)
    rating.config(text="This location has an average cleanliness rating of {}".format(float("{0:.2f}".format(average))))
    return

"""
Creates a window using tkinter that will contain the content of the program
"""
root = Tk()
root.title('Cleanliness Rater')
root.minsize(400, 400)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)

style = ttk.Style()
style.configure("TButton", padding=(20, 70, 20, 70))  # re-styles tkinter button to have more space surrounding text


#  FRAME 1
frame = ttk.Frame(root, padding=20)
frame.grid(column=0, row=0, sticky=NSEW)
Grid.columnconfigure(frame, 0, weight=1)
Grid.rowconfigure(frame, 0, weight=1)

label = ttk.Label(frame, text='Rate the cleanliness of this location:')
label.grid(row=0, column=0, sticky=NS)


#  FRAME 2 which contains the buttons from 1 to 5 for the user to click(or tap)
frame2 = ttk.Frame(root, padding=20)
frame2.grid(column=0, row=1, sticky=NSEW)
Grid.columnconfigure(frame2, 0, weight=1)
Grid.rowconfigure(frame2, 0, weight=1)
Grid.columnconfigure(frame2, 1, weight=1)
Grid.rowconfigure(frame2, 1, weight=1)
Grid.columnconfigure(frame2, 2, weight=1)
Grid.columnconfigure(frame2, 3, weight=1)
Grid.columnconfigure(frame2, 4, weight=1)
Grid.columnconfigure(frame2, 5, weight=1)
Grid.columnconfigure(frame2, 6, weight=1)


#  unhappy face, positioned left so the user understands that 1 is the worst rating
unhappy = ttk.Label(frame2, text=":-(")
unhappy.grid(row=0, column=0, sticky=NS)

#  buttons 1 to 5
button1 = ttk.Button(frame2, text="1")
button1.configure(command=click1)
button1.grid(row=0, column=1, sticky=NSEW)

button2 = ttk.Button(frame2, text="2")
button2.configure(command=click2)
button2.grid(row=0, column=2, sticky=NSEW)

button3 = ttk.Button(frame2, text="3")
button3.configure(command=click3)
button3.grid(row=0, column=3, sticky=NSEW)

button4 = ttk.Button(frame2, text="4")
button4.configure(command=click4)
button4.grid(row=0, column=4, sticky=NSEW)

button5 = ttk.Button(frame2, text="5")
button5.configure(command=click5)
button5.grid(row=0, column=5, sticky=NSEW)


#  happy face, positioned right
happy = ttk.Label(frame2, text=":-)")
happy.grid(row=0, column=6, sticky=NS)

#  FRAME 3 which includes the average result of the buttons clicked using the program
frame3 = ttk.Frame(root, padding=20)
frame3.grid(column=0, row=2, sticky=NSEW)
Grid.columnconfigure(frame3, 0, weight=1)
Grid.rowconfigure(frame3, 0, weight=1)
Grid.rowconfigure(frame3, 2, weight=1)

"""This label changes depending on the user input, it is the average of the numbers pressed"""
rating = ttk.Label(frame3, text="There is no current rating available")
rating.grid(column=0, row=0, sticky=NS)


root.mainloop()
