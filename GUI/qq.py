from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()

def myClick():
    myLabel = Label(root, tex=e.get())
    
buttonClick = Button(root, text="Click Here.", command=myClick).pack()
root.mainloop()