import tkinter as tk
import random

def display_text():
    # create a random gray color
    farba = random.randint(0,7)
    
    # display the text at a random location on the canvas
    x = random.randint(100, 500)
    y = random.randint(100, 500)
    canvas.delete("text") # remove any existing text
    canvas.create_text(x, y, text="Maturita 2019", fill='#'+str(farba)+str(farba)+str(farba), font=("Arial", 30, "bold"), tag="text")
    
    # schedule the text to disappear after one second
    root.after(1000, remove_text)
    
def remove_text():
    # remove the text from the canvas
    canvas.delete("text")
    
    # loop the display_text function
    if running:
        display_text()
        
def key_pressed(event):
    # stop the program when a key is pressed
    global running
    running = False
    root.destroy()

# create the GUI window
root = tk.Tk()
root.geometry("600x600")
root.title("Maturita 2019")

# create a canvas to display the text
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# set up the event bindings
running = True
root.bind("<Key>", key_pressed)

# start the program
display_text()
root.mainloop()
