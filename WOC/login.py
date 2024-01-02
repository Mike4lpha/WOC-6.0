import tkinter as tk
from tkinter import messagebox, Entry, Button, Frame, Label
import mysql.connector
from PIL import Image, ImageTk
import os
import base64
import hashlib

trial_no = 0

class GraphicalPasswordAuthenticationSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Graphical Password Authentication System")
        self.master.geometry("1900x900")
        self.master.resizable(False, False)

        self.image_paths = [
            "/home/kali/WOC/tmnt.gif",
            "/home/kali/WOC/ben10.gif",
            "/home/kali/WOC/pokemon.gif",
            "/home/kali/WOC/taj.gif",
            "/home/kali/WOC/ram.gif",
            "/home/kali/WOC/beyblade.gif",
            "/home/kali/WOC/rn21.gif",
            "/home/kali/WOC/nh.gif",
            "/home/kali/WOC/paf.gif",
            "/home/kali/WOC/shinchan.gif"
        ]

        self.selected_images = []
        self.current_image_index = 0

        for i, path in enumerate(self.image_paths):
            try:
                abs_path = os.path.abspath(path)
                image = ImageTk.PhotoImage(file=abs_path)
            except tk.TclError as e:
                messagebox.showerror("Image Error", f"Error loading image '{path}': {e}")
                self.master.destroy()
                return

            button = tk.Button(master, image=image, command=lambda p=abs_path: self.select_image(p))
            button.image = image
            button.pack(side=tk.LEFT, padx=5, pady=5)

        # User entry
        def user_enter(e):
            self.user.delete(0, "end")

        def user_leave(e):
            name = self.user.get()
            if name == "":
                self.user.insert(0, "UserID")

        self.user = Entry(master, width=16, fg="#fff", border=0, bg="#375174", font=("Arial Bold", 24))
        self.user.bind("<FocusIn>", user_enter)
        self.user.bind("<FocusOut>", user_leave)
        self.user.place(x=800, y=100)
        self.user.insert(0, 'UserID')

        # Login button
        login_button = Button(master, text="LOGIN", fg="white", bg="#1f5675", width=10, height=1, font=('arial', 16, 'bold'), bd=0, command=self.login)
        login_button.place(x=900, y=650)

        # Register button
        register_label = Label(master, text="Don't have an account?", fg='#fff', bg="#00264d", font=("Microsoft YaHei UI Light", 9))
        register_label.place(x=850, y=700)

        register_button = Button(master, width=10, text="Sign Up", border=0, bg="#00264d", fg="#57a1f8", command=self.register)
        register_button.place(x=1000, y=695)

    def select_image(self, path):
        if self.current_image_index < 9:
            # Open the image file and read binary data
            with open(path, "rb") as image_file:
                # Encode the binary data as base64
                image_data = base64.b64encode(image_file.read())
                # Hash the binary data using SHA-256
                hashed_image = hashlib.sha256(image_data).hexdigest()
                # Append the hashed data to the selected images list
                self.selected_images.append(hashed_image)
            
            self.current_image_index += 1
            if self.current_image_index == 9:
                self.login()
        else:
            messagebox.showwarning("Selection Complete", "You have already selected 5 images.")

    def login(self):
        username = self.user.get()

        if username == "" or username == "UserID":
            messagebox.showerror("Entry error", "Type username!!")
            return

        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='kali', database='login')
            mycursor = mydb.cursor()
            print("Connected to Database!!")

        except mysql.connector.Error as e:
            messagebox.showerror("Connection Failed!!", f"Error: {e}")
            return

        command = "USE login"
        mycursor.execute(command)

        command = "SELECT * FROM users WHERE Username = %s"
        mycursor.execute(command, (username,))
        myresult = mycursor.fetchone()

        if myresult is None:
            messagebox.showinfo("Invalid", "Invalid Username!!")
            self.trial()
        else:
            # Retrieve the stored password
            stored_password = myresult[2]
            #print("Selected Images:", self.selected_images)
            stored_images = stored_password.split(',')
            #print("Stored Images:", stored_images)

            # Check if the selected images match the stored images
            if self.selected_images == stored_images:
                messagebox.showinfo("Login", "Successfully Login!!")
                self.master.destroy()
                import sys
                sys.path.append('/home/kali/WOC')
                import welcome
            else:
                messagebox.showinfo("Invalid", "Invalid Password!!")
                self.trial()

            # Reset
            self.selected_images = []
            self.current_image_index = 0

    def trial(self):
        global trial_no
        trial_no += 1
        print("Trial no is ", trial_no)
        if trial_no == 4:
            mydb = mysql.connector.connect(host='localhost', user='root', password='kali', database='login')
            mycursor = mydb.cursor()
            mycursor.execute("USE login")
            username = self.user.get()
            mycursor.execute("DELETE FROM users WHERE Username = %s", (username,))
            mydb.commit()
            messagebox.showwarning("Warning", "You have tried more than the limit!!")
            root.destroy()

    def register(self):
        self.master.destroy()
        import sys
        sys.path.append('/home/kali/WOC')
        import register

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicalPasswordAuthenticationSystem(root)
    root.mainloop()
