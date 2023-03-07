import tkinter
import random
master = tkinter.Tk()  # Create the main window object
master.title("Kružnice")  # Set the title of the window
canvas = tkinter.Canvas(master, width=600, height=600, bg='black')  # Create a canvas inside the window
x = 0
farba = ['white','black','red','blue','green','yellow']
pocet = int(input('Zadajte počet kružníc: '))
for i in range(0,pocet):
    x = x + 10
    canvas.create_oval(300-x,300-x,x+300,x+300, width=5, outline=random.choice(farba))
canvas.pack()  # Pack the canvas into the window
tkinter.mainloop()  # Start the main event loop