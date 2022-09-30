from tkinter import*
from tkinter.colorchooser import*

top=Tk()

top.title("Login Box")
top.geometry("300x200+200+200")
top.configure(bg="green")

#Creating label for Username 
Uname=Label(top,text="Username",fg="yellow",bg="green").place(x=30,y=50)

#Creating label for password

Password=Label(top,text="Password",fg="yellow",bg="green").place(x=30,y=90)

#Creating Button to submit the username and password
submitbtn=Button(top,text="Submit",bg="yellow",fg="green").place(x=100,y=120)

e1= Entry(top,width=20).place(x=100,y=50)
e2=Entry(top,width=20).place(x=100,y=90)


top.mainloop()
