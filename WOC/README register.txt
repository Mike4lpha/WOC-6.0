It creates a screen of size 1900x900, titled "NEW USER REGISTRATION".
It contains a place for username input. The username cannot be kept blank.
There are 10 predefined images, out of which 9 has to be selected. Same images can be selected; it allows more combination. On selecting more than 9, it shows an error in messgaebox.  
The image data of the selected images are converted into binary and then hashed using sha256. 
On clicking register it checks for a database named "login" in localhost. If no such database is found it creates "login" and a table named "users" in the "login" database. The users table have two columns namely, "username" and "password". The Username entered in the user entry is stored under the username column and the hashed selected images are stored in the password column separated by commas.
If database is successfully connected and user is added, it shows "New User Added Succesfully".
On clicking the backbutton on upper left corner, register.py is closed and login.py is opened.

