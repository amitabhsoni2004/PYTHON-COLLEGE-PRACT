# Import the tkinter module
import tkinter as tk

# Import the messagebox module from tkinter
from tkinter import messagebox

# Create the main window
top = tk.Tk()

# Define the callback function for the button
def helloCallBack():
    # Show a message box with a message
    messagebox.showinfo("Hello World", "Hello Python")

# Create a button widget with text "Hello" and attach the callback function
B = tk.Button(top, text="Hello", command=helloCallBack)
# Pack the button into the window
B.pack()

# Start the main event loop
top.mainloop()