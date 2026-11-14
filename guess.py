from tkinter import*
import tkinter.messagebox
import random


screen = Tk()
screen.title("Number guessing game")
screen.geometry("400x200")

num = random.randint(1,50)
def ok():
    Name = name_entry.get()
    tkinter.messagebox.showinfo("Guess the number","Well " + Name + " I'm guessing a number between 1-50, can you guess it?")

def guess():
    Num = guess_entry.get()
    Num = int(Num)
    if Num > num:
        tkinter.messagebox.showinfo("Guesser","The" + str(Num) + "is greater than what I'm guessing")
    elif Num < num:
        tkinter.messagebox.showinfo("Guesser","The" + str(Num) + "is lesser than what I'm guessing")
    elif Num == num:
        tkinter.messagebox.showinfo("Guesser","Yes it is " + str(Num))


label_title = Label(screen,text="Welcome to the guessing game")
label_title.place(x=150,y=5)

name_label = Label(screen,text="Whats your name")
name_label.place(x=20,y=50)
name_entry = Entry(screen,width=15)
name_entry.place(x=20,y=70)
ok_button = Button(screen,text="Ok",command=ok)
ok_button.place(x=150,y=60)

guess_label = Label(screen,text="Take a guess: ")
guess_label.place(x=20,y=140)
guess_entry = Entry(screen,width=10)
guess_entry.place(x=100,y=140)
guess_button = Button(screen,text="Guess",command=guess)
guess_button.place(x=180,y=140)

mainloop()