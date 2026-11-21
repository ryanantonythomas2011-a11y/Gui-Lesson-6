from tkinter import*
import random
import tkinter.messagebox

screen = Tk()
screen.geometry("300x500")
screen.title("Even Or Odd")

evenodd_label = Label(screen,text="I have picked a number is it even or odd")
evenodd_label.place(x=80,y=50)
comp_num = random.randint(1,100)


def guess_even():
    if comp_num % 2 == 0:
        tkinter.messagebox.showinfo("Result", "Correct! The number was even.")
    else:
        tkinter.messagebox.showinfo("Result", "Incorrect! The number was odd.")

def guess_odd():
    if comp_num % 2 != 0:
        tkinter.messagebox.showinfo("Result", "Correct! The number was odd.")
    else:
        tkinter.messagebox.showinfo("Result", "Incorrect! The number was even.")

odd_button = Button(screen,text="Odd",command=guess_odd)
odd_button.place(x=10,y=200)
even_button = Button(screen,text="Even",command=guess_even)
even_button.place(x=10,y=100)
mainloop()
