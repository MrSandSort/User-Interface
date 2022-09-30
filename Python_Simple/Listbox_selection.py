from tkinter import*
from functools import partial

top=Tk()

def display(answer,mylist):
    a=mylist.get(ACTIVE)
    answer.config(text=a)
    return

sb=Scrollbar(top)
sb.pack(side=RIGHT, fill=Y)

Lb=Label(top,text="Select Favourite Fruit")
mylist=Listbox(top,yscrollcommand=sb.set)
answer=Label(top)

display=partial(display,answer,mylist)
b=Button(top,text="Show",command=display)

mylist.insert(1,"Kiwi")
mylist.insert(2,"Mango")
mylist.insert(3,"Papaya")
mylist.insert(4,"Orange")
mylist.insert(5,"Apple")

Lb.pack()

mylist.pack(side=LEFT)
sb.config(command=mylist.yview)

b.pack(side=LEFT)
answer.pack(side=RIGHT)

mainloop()
