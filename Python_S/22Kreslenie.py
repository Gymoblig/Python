import tkinter

master = tkinter.Tk()  # Create the main window object
master.title("My Canvas")  # Set the title of the window
canvas = tkinter.Canvas(master, width=600, height=600, bg='white')  # Create a canvas inside the window
canvas.create_rectangle(20,20,580,370)
canvas.create_text(300,35, text='Gymnázium v Ružomberku, Š. Moyzesa 21, 034 13 Ružomberok', font='arial 12')
canvas.create_line(30,50,570,50)
canvas.create_oval(150-50,200-50,50+150,50+200, width=5, outline='blue')
canvas.create_line(150,100,150,350, width=5, fill='magenta' )
canvas.create_line(60,200,570,200, width=5, fill='magenta' )
canvas.create_text(350,250, text='Janko Hraško', fill='magenta', font='arial 32 bold')





canvas.pack()  # Pack the canvas into the window

tkinter.mainloop()  # Start the main event loop
