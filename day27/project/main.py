from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,200)
window.config(padx= 20, pady= 20)

#Entry
input = Entry(width=10)
input.grid(column=1,row=0)
input.insert(END, "0")
input.get()

#Lable "Mile"
miles = Label(text="Miles", font=("Arial", 15 , "normal"))
miles.grid(column=2,row=0)

#Lable "is equal to"
is_equal_to = Label(text="is equal to", font=("Arial", 15 , "normal"))
is_equal_to.grid(column =0,row=1)

#Lable "km"
km = Label(text=" km", font=("Arial", 15 , "normal"))
km.grid(column = 2,row =1)

#Lable result
result = Label(text="0", font=("Arial", 15 , "normal"))
result.grid(column = 1, row =1)

def button_pressed():
    data = float(input.get())
    rs = data * 1.609
    result.config(text = rs)
#Button
button  = Button(text="Caculate", command=button_pressed)
button.grid(column = 1, row = 2)
window.mainloop()