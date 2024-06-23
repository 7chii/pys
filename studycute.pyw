from tkinter import *
from datetime import date

def clicked1():
    number.set(number.get()+100)
def clicked2():
    number.set(number.get()+50)
def clicked3():
    number.set(number.get()-number.get())    
today = date.today()


window = Tk()
window.title("estudar!")
window.geometry('200x100')
number = IntVar()

label = Label(window, textvariable=number)
label.grid(column=0,row=0)

label1 = Label(window, text=today)
label1.grid(column=3,row=0)

button = Button(window, text="exercicio", command=clicked1)
button.grid(column=1, row=2)

button = Button(window, text="materia", command=clicked2)
button.grid(column=2, row=3)

button = Button(window, text="zerar", command=clicked3)
button.grid(column=3, row=4)




window.mainloop()