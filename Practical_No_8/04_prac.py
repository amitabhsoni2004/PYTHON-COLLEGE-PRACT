# Program to create checkButton widget

from tkinter import *  # Import all classes and functions from tkinter module

top = Tk()  # Create the main window
top.minsize(400, 400)  # Set the minimum size of the window

checkVar1 = IntVar()  # Create an integer variable for the first checkbutton
checkVar2 = IntVar()  # Create an integer variable for the second checkbutton

# Create the first checkbutton with text "Music"
c1 = Checkbutton(top, text="Music", variable=checkVar1, onvalue=1, offvalue=0, height=5, width=20)
# Create the second checkbutton with text "Video"
c2 = Checkbutton(top, text="Video", variable=checkVar2, onvalue=1, offvalue=0, height=5, width=20)

c1.pack()  # Pack the first checkbutton into the window
c2.pack()  # Pack the second checkbutton into the window

top.mainloop()  # Start the main event loop