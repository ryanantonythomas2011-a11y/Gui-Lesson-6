from tkinter import*
from time import strftime

screen = Tk()
screen.geometry("500x200")
screen.title("Clock")

lbl = Label(screen,font=("Calibri",30))
lbl.place(x=250,y=100)

def time():
    Time = strftime("%H:%M:%S,%p")
    lbl.config(text=Time)
    lbl.after(1000,time)

time()

mainloop()




