from tkinter import*
from functools import partial
'''Partial functions allow us to fix a certain number
of arguments of a function and generate a new function.'''

def addi(answer,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result= int(num1)+int(num2)
    answer.config(text="Result=%d"%result)
    return

def multi(answer,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result= int(num1)*int(num2)
    answer.config(text="Result=%d"%result)
    return

root=Tk()

root.geometry("400x200+100+200")
root.title("Calculator")

number1=StringVar()
number2=StringVar()

labelNum1=Label(root,text="A").grid(row=1,column=0)
labelNum2=Label(root,text="B").grid(row=2,column=0)

answer=Label(root)
answer.grid(row=7,column=2)

entryNum1=Entry(root,textvariable=number1).grid(row=1,column=2)
entryNum2=Entry(root,textvariable=number2).grid(row=2,column=2)

addi=partial(addi,answer,number1,number2)
multi=partial(multi,answer,number1,number2)

buttonAdd=Button(root,text="Add",command=addi).grid(row=3,column=0)
buttonMulti=Button(root,text="Multiply",command=multi).grid(row=3,column=10)

root.mainloop()










