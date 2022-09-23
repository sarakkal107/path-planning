import tkinter as tk


def start_gui():
    window = tk.Tk()
    window.minsize(200, 200)
    window.title("Path Planning")
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    window.mainloop()
