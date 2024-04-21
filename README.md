# Encrypting and decrypting the text in the photo, where the characters are mapped in different colors (the mapping represents the key). The rest of the photo can be filled with any color.

_*University Of Prishtina - Faculty of Electrical and Computer Engineering/Department of Computer and Software Engineering*_

### Name of Supervisor
This is the second project in Data Security supervised by PhD candidate Mergim Hoti


# Description of the project

In this project we have implemented a technique called steganography which involves hiding information in other information.

Encryption:

We achieve this by mapping each character to a distinct color.

For example, we can assign a character to a color A = (0, 0, 0) then we open the image and get the width and height and we load the pixels of the image into a variable which allows direct access to tbhe idividual pixels  at the specified pixels the color changes to the corresponding color of the character that is used in which case it is black.The rest of the image, that doesn't contain any text we mapped using the white color (255,255,255).


Decryption:

We achieve decryption by first reversing the dictionary so changing the key and value pairs when we encrypt the character is the key and the color is the value, when we decrypt we just change this so the color is the key and the character is the value.

Then we iterate using loops to go to a specified pixel retrieve the color, search for that color in the dictionary, and retrieve the character at the specified color.   



The rest of the code consists of a simple GUI just to demonstrate that hiding information inside an information is quite effective beacuse it's difficult to discern the pixels until you zoom in on the image. 


This program is entirely written using python.      



## Contributors
Albin Arifaj 

Alfred Palokaj

Albjon Tahirsylaj

Albion Ahmeti
