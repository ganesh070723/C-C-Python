import tkinter as t
window = t.Tk()
window.minsize(width=300,height=200)
window.config(padx=30,pady=30)

label1= t.Label(text="Miles TO Km",font=("Times New Roman",12,"normal"))
label1.grid(column=3,row=3)
label1.config(padx=70,pady=10)

input= t.Entry()
input.grid(column=3,row=4)
lablentr=t.Label(text="IN MILES",font=("Times New Roman",8,"normal"))
lablentr.grid(column=2,row=4)
lable2=t.Label(text=f"Is equal to :  ")
lable2.grid(column=2,row=5)
lableresult1 = t.Label(text= f"0",font=("Times New Roman",14,"normal") )
lableresult1.grid(column=3, row=5)
def ans():
    lableresult=round(float(input.get()) * 1.60934, 2)
    return lableresult
def result():
    lableresult1.config(text=ans())

lablekm = t.Label(text= "KM",font=("Times New Roman",10,"normal") )
lablekm.grid(column=4, row=5)

button = t.Button(text="Calculate",command=result)
button.grid(column=3,row=6)
button.config(padx=10,pady=5)













window.mainloop()