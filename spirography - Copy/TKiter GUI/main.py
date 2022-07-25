from tkinter import *

window = Tk()
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

my_lable = Label(text="GUI",font=("Arial",12,"bold"))
my_lable.grid(column=0,row=0)
window.title("MY First GUI")
input = Entry()
input.grid(column=5,row=4)


def butt():
    my_lable.config(text=input.get())
button = Button(text="Click Me",command=butt)
button.grid(column=3,row=2)
button2= Button(text="Button 2")
button2.grid(column=4,row=0)



















window.mainloop()