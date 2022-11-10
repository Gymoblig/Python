import tkinter
from random import *
canvas = tkinter.Canvas(bg='silver',width=600,height=600) 
canvas.pack()

def dom(x,y):
   
    canvas.create_rectangle(x,y,x+50,y+50)
    canvas.create_line(x,y,x+25,y-50,x+50,y)

x= 10
for i in range(1,7):
    x= x+ 80
    dom(x, 100)

canvas.mainloop()