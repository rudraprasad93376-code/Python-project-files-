import tkinter as tk
import time

root = tk.Tk()
root.title("😊Countdown Timer")
root.geometry("800x400")
root.configure(bg="black")

lbl = tk.Label(root, font=("Arial", 80, "bold"), bg="black", fg="white")
lbl.pack(pady=100)  # Pack the label into the window

seconds = 10

def countdown():
    global seconds
    if seconds >= 0:
        lbl.config(text=f"{seconds} sec left")
        seconds -= 1
        root.after(1000, countdown)  # Schedule the next call after 1000ms (1 second)
    else:
        lbl.config(text="💕 Time's Up !")

countdown()  # Start the countdown
root.mainloop()