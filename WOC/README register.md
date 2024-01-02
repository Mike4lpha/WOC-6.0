It creates a screen of size 1900x900, titled "NEW USER REGISTRATION".
It contains a place for username input. The username cannot be kept blank.
There are 10 predefined images, out of which 9 has to be selected. Same images can be selected; it allows more combination. On selecting more than 9, it shows an error in messgaebox. (## I DID MENTION IN THE PROPOSAL THAT I WOULD BE ADDING 15 IMAGES, BUT IT DID NOT FIT ON SCREEN. INSTEAD I MADE USING 10 IMAGES. IT IS THE SAME CONCEPT. 15 IMAGES CAN BE ADDED BY RESIZING THE IMAGES; BUT THEN EACH IMAGE WILL BECOME TOO SMALL.##) 
The image data of the selected images are converted into binary and then hashed using sha256. 
On clicking register it checks for a database named "login". If it is not created it 

