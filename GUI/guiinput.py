from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    myLabel = Label(root, text="Your Name is: " + e.get()).pack()
    
buttonClick = Button(root, text="Click Here.", command=myClick).pack()
root.mainloop()

