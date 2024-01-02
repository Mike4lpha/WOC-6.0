import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage, Button, Frame, Label, Entry
from PIL import Image, ImageTk
import os

framebg = "#EDEDED"
framefg = "#06283D"

root = tk.Tk()
root.title("WELCOME!!")
root.geometry("1900x900")
root.resizable(False, False)

frame = Frame(root, bg=framebg)
frame.pack(fill=tk.Y)
mycursor = None

welcome_label = Label(root, text="Welcome", fg='#fff', bg="#00264d", font=("Microsoft YaHei UI Light", 32))
welcome_label.place(x=850, y=500)

root.mainloop()
