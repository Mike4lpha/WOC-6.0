This also creates a screen of size 1900x900, titled "Graphical Password Authentication System".
It has a place for user entry and 10 images which are not in the same order as in the 'NEW USER REGISTRATION PAGE'. It has a login button and a 'sign up' button.
The sign up button redirects the user to the register page (register.py).
The image data of the selected images are converted to binary and then hashed using sha256. The hashed data is stored in the form of an array.
On clicking the login button, the mysql database is connected. It compares the entered username with each row of stored username until it mathches one.
If it does not match, it shows "Invalid Username".
If it matches, it goes furthur and retrieves the stored password of the given username and compares it with the hashed password array. If both of them matches, it shows "Successfull Login" and opens welcome.py.
It counts the trial as 1.
If the stored password does not match the selected hashed password, it shows "Incorrect Password".
After 4 incorrect trials, the row corresponding to the entered Username is deleted from the users table.
