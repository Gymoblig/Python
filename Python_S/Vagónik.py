import tkinter
from turtle import fillcolor
from venv import create

canvas = tkinter.Canvas(bg='silver',width=1200,height=600) 
canvas.pack()
def rusen(x,y):
    canvas.create_rectangle(x,y,x+100,y+50, fill="green")
    canvas.create_rectangle((x+70),y, (x+50)+50,y-20, fill="red")
    canvas.create_rectangle(x,y, x+20,y-30, fill="blue")
    x= x-25
    for i in range(1,5):
        x=x+25
        canvas.create_oval(x,y+50,x+25,(y+50)+25, fill="black")
def vagon(x,y):
    canvas.create_rectangle(x,y,x+100,y+50, fill="green")
    canvas.create_rectangle(x+25,y+10,x+75,y+30, fill="blue")
    canvas.create_rectangle(x,y+40,x-20,y+30, fill="black")
    x= x-25
    for i in range(1,5):
        x=x+25
        canvas.create_oval(x,y+50,x+25,(y+50)+25, fill="black")


def vagony(x):
    for i in range(1,6):
        x = x+120
        vagon(x,100) 
rusen(100,100)
vagony(100)
canvas.mainloop()