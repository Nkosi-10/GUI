from tkinter import *

root = Tk()

myLabel = Label(root, text=("Sawubona")).pack()
myLabela= Label(root, text=("What's your name?")).pack()
myButton = Button(root, text="Click me!!").pack()
# when we decide to add (state=Disable) we are desabling the button from being clicked

# when adding the padx snd pady we are fixing the size of the button, padx is responsible for the x- axis and y for the  y-axis


# myLabel.grid(row=1,  column=2)
# myLabela.grid(row=0, column=2)


# when we say pack we simply directing the program nor the window to  have the size of its content that is found nor written
# myLabel.pack()


root.mainloop()