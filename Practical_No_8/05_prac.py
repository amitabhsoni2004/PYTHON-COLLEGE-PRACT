# Program to create Radio button widget

from tkinter import *  # Import all classes and functions from tkinter module

def sel():
    # Function to update label with the selected radio button option
    selection = "You selected the option " + str(var.get())
    Label.config(text=selection)

root = Tk()  # Create the main window
root.minsize(400, 400)  # Set the minimum size of the window
var = IntVar()  # Create an integer variable to store the selected radio button value

# Create the first radio button
r1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
r1.pack(anchor=W)  # Pack the radio button to the window, aligned to the west (left)

# Create the second radio button
r2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
r2.pack(anchor=W)  # Pack the radio button to the window, aligned to the west (left)

# Create the third radio button
r3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
r3.pack(anchor=W)  # Pack the radio button to the window, aligned to the west (left)

label = Label(root)  # Create a label widget
label.pack()  # Pack the label to the window

root.mainloop()  # Start the main event loop