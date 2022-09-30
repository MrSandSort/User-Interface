
from tkinter import *
from tkinter.colorchooser import *

top= Tk()
top.title("Welcome Home")

top.geometry("300x300+200+200")
#top.geometry(widthxheight+from left+from top)

top.resizable(0,0)
#top.configure(bg="blue")

top["background"]="#33ccff"

color=askcolor()
print(color[0])

top.mainloop()
