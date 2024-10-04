# Import all classes from tkinter module
from tkinter import *

# Create the main window
top = Tk()

# Create a label widget with text "User Name"
L1 = Label(top, text="User Name ")
# Pack the label widget to the left side of the window
L1.pack(side=LEFT)

# Create an entry widget with a border width of 5
E1 = Entry(top, bd=2)
# Pack the entry widget to the right side of the window
E1.pack(side=RIGHT)

# Run the main event loop
top.mainloop()