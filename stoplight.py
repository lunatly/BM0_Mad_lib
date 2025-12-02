from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Three Buttons Example")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="Yellow", background='Yellow')
green_button = Button(root, text="Green", background='Green')
#Add a label


# Place widgets in window (with pack function!)
label.pack()
red_button.pack()
yellow_button.pack()
green_button.pack()

label = Label(root, text="CHANGE ME!")

# Start the GUI event loop
root.mainloop()