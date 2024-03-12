from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(500,300)
window.config(padx = 20, pady = 20) # Thục trên thục dưới 20

#Label
my_label = Label(text="I am Label", font= ("Arial ",24,"bold"))
# This will show up the elements, or describe this elements with color, align..
# my_label.pack()
#This function will help me place element base on coordinate
# my_label.place(x = 0,y = 0)
#this function will help me place element base of grid, every element will 1 ô trong bang
my_label.grid(column=0,row=0)
#This is the way how to configue or change or update property we created
my_label["text"] = "New Text" # Cach 1
my_label.config(text = "NewText") #Cach 2:  Khai bao lai text = NewText

#Button
def button_pressed():
    new_text = input.get()
    my_label.config(text = new_text)
    # my_label["text"] = new_text

button  = Button(text = "Click me", command = button_pressed)
# button.pack() #This is very import for every elements
button.grid(column=1,row= 1)
#Entry
input = Entry(width=15)
# input.pack()
print(input.get())
input.grid(column=2,row=2)
window.mainloop()

