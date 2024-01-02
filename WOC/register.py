import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage, Button, Frame, Label, Entry
import mysql.connector
from PIL import Image, ImageTk
import os
import base64
import hashlib

framebg = "#EDEDED"
framefg = "#06283D"

root = tk.Tk()
root.title("NEW USER REGISTRATION")
root.geometry("1900x900")
root.resizable(False, False)

frame = Frame(root, bg=framebg)
frame.pack(fill=tk.Y)
mycursor = None

selected_images = []
predefined_images = [
    "/home/kali/WOC/Images/tmnt.gif",
    "/home/kali/WOC/Images/taj.gif", 
    "/home/kali/WOC/Images/ben10.gif",
    "/home/kali/WOC/Images/pokemon.gif",
    "/home/kali/WOC/Images/shinchan.gif",
    "/home/kali/WOC/Images/ram.gif",
    "/home/kali/WOC/Images/paf.gif",
    "/home/kali/WOC/Images/beyblade.gif",
    "/home/kali/WOC/Images/nh.gif",
    "/home/kali/WOC/Images/rn21.gif"
]

def select_image(image_path):
    global selected_images
    if len(selected_images) < 9:
        selected_images.append(image_path)
        update_selection_button()
    else:
        messagebox.showwarning("Selection Complete", "You have already selected 9 images.")

def update_selection_button():
    remaining_images = 9 - len(selected_images)
    selectImagesButton.config(text=f"Select {remaining_images} Images")

for i, path in enumerate(predefined_images):
    abs_path = os.path.abspath(path)
    image = Image.open(abs_path)
    photo = ImageTk.PhotoImage(image)

    button = Button(root, image=photo, command=lambda p=abs_path: select_image(p))
    button.image = photo
    button.pack(side=tk.LEFT, padx=5, pady=5)

#Image data to binary to sha256
def encode_image_to_hash(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        hashed_image = hashlib.sha256(encoded_image).hexdigest()
    return hashed_image


def register():
    username = user.get()

    global mycursor
    if username == "" or username == "UserID" or len(selected_images) != 9:
        messagebox.showerror("Entry error!", "Type username and select exactly 9 images for the password!!")
        return

    try:
        mydb = mysql.connector.connect(host='localhost', user='root', password='kali')
        mycursor = mydb.cursor()
        print("Connected to Database!!")

    except:
        messagebox.showerror("Connection", "Database connection not established!!")
        return

    try:
        mycursor.execute("SHOW DATABASES LIKE 'login'")
        result = mycursor.fetchone()

        if not result:
            mycursor.execute("CREATE DATABASE login")

        mycursor.execute("USE login")

        mycursor.execute("SHOW TABLES LIKE 'users'")
        result = mycursor.fetchone()

        if not result:
            mycursor.execute("CREATE TABLE users (user int auto_increment key not null, Username varchar(50), Password LONGTEXT)")

        # Store hashed images individually
        hashed_images = [encode_image_to_hash(image_path) for image_path in selected_images]

        command = "INSERT INTO users(Username, Password) VALUES (%s, %s)"
        mycursor.execute(command, (username, ','.join(hashed_images)))

        mydb.commit()
        mydb.close()

        messagebox.showinfo("Register", "New User added Successfully!!")

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")


def login():
    root.destroy()
    import sys
    sys.path.append('/home/kali/WOC')
    import login

def user_enter(e):
    user.delete(0, "end")

def user_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "UserID")
        
#User Entry
user = Entry(root, width=16, fg="#fff", border=0, bg="#375174", font=("Arial Bold", 24))
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=800, y=100)
user.insert(0, 'UserID')

selectImagesButton = Button(root, text="Select 9 Images", fg="white", bg="#1f5675", width=15, height=1, font=('arial', 16, 'bold'), bd=0, command=register)
selectImagesButton.place(x=870, y=200)

registerButton = Button(root, text="REGISTER", fg="white", bg="#1f5675", width=10, height=1, font=('arial', 16, 'bold'), bd=0, command=register)
registerButton.place(x=900, y=650)

backbuttonimage = PhotoImage(file="/home/kali/WOC/backbutton.png")
Backbutton = Button(root, image=backbuttonimage, fg="#deeefb", command=login)
Backbutton.place(x=20, y=15)

root.mainloop()
