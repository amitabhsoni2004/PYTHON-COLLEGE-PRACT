# Import everything from tkinter module
from tkinter import *

# Create the main window
root = Tk()

# Create a StringVar to hold the message text
var = StringVar()

# Create a Message widget with the textvariable set to var and a raised relief
label = Message(root, textvariable=var, relief=RAISED)

# Set the text of the StringVar
var.set("Hey!? How are you doing?")

# Pack the Message widget into the window
label.pack()

# Run the main event loop
root.mainloop()