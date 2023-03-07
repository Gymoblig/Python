import tkinter
import random
master = tkinter.Tk()  # Create the main window object
master.title("Text")  # Set the title of the window
canvas = tkinter.Canvas(master, width=600, height=600, bg='white')  # Create a canvas inside the window
y = 30
text = str(input('Zadajte text: '))
font = 20

for i in range(0,4):
    font = font + 5
    y = y + 50
    canvas.create_text(300,y, text=text, font=f'arial {font}')




canvas.pack()  # Pack the canvas into the window
tkinter.mainloop()  # Start the main event loop