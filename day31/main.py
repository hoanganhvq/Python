from tkinter import  *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card= {}
to_learn= {}
try:
    data= pandas.read_csv("data/words_to_learn.csv")#Doc du lieu va chuyen vao dic data
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")  # Chuyen doi dic thanh kieu khac
else:
    to_learn = data.to_dict(orient="records") #Chuyen doi dic thanh kieu khac


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")# Renew lai title thanh French
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text ="English", fill="white")
    canvas.itemconfig(card_word, text = current_card["English"],fill="white")
    canvas.itemconfig(card_background,image= card_back_img)

def is_know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)# Tao ra mot khung du lieu luu nhung tu chua duoc bo qua
    #Neu khong co no thi sau khi moi lan chay thi se reset ve 100 tu
    data.to_csv("data/words_to_learn", index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx =50,pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Canvas use to create the Image....
canvas = Canvas(width=800, height= 526)
card_front_img = PhotoImage(file="images/card_front.png") #Create the path to image
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)#Vi tri dat cua hinh anh 400,263
card_title = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0) #Lam cho mau nen hinh anh trung va mat vien
canvas.grid(row=0,column = 0, columnspan=2)

cross_image= PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness= 0, command=next_card)
unknown_button.grid(row=1, column =0)

check_button = PhotoImage(file= "images/right.png")
known_button = Button(image=check_button,highlightthickness=0,command=is_know)
known_button.grid(row=1,column =1)

next_card()

window.mainloop()
