from Tkinter import *   # don't pollute namespace like this except for Tkinter
import PIL    
from PIL import ImageTk # a subpackage that must be imported explicitly
import os.path              


root = Tk() # create main window; must be done before using ImageTk

canvas = Canvas(root, height=800, width=800, background='#FFFFFF')
canvas.grid()

__dir__ = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(__dir__, 'home.jpg')

img = PIL.Image.open(filename)

tkimg = PIL.ImageTk.PhotoImage(img)

canvas.create_image(0, 0, image=tkimg)

root.mainloop()