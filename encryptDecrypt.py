import random

import PIL
from PIL import Image, ImageTk
import tkinter as tk

characterToColor = {
    'A': (255, 0, 10),
    'B': (0, 255, 0),
    'C': (0, 0, 255),
    'D': (200, 100, 20),
    'E': (255, 10, 30),
    'F': (255, 40, 50),
    'G': (130, 30, 50),
    'H': (225, 10, 60),
    'I': (5, 150, 80),
    'J': (2, 140, 90),
    'K': (55, 201, 0),
    'L': (75, 200, 1),
    'M': (155, 90, 9),
    'N': (65, 100, 54),
    'O': (95, 120, 43),
    'P': (105, 100, 32),
    'Q': (42, 90, 21),
    'R': (131, 0, 100),
    'S': (231, 20, 4),
    'T': (222, 30, 5),
    'U': (254, 30, 87),
    'V': (201, 40, 85),
    'W': (110, 70, 21),
    'X': (130, 30, 32),
    'Y': (120, 20, 10),
    'Z': (70, 10, 2),
    ' ': (133, 23, 55),
    '0': (246, 3, 5),
    '1': (32, 54, 55),
    '2': (13, 66, 55),
    '3': (53, 77, 55),
    '4': (63, 98, 55),
    '5': (103, 22, 55),
    '6': (113, 54, 55),
    '7': (123, 59, 55),
    '8': (153, 69, 55),
    '9': (173, 79, 55),
}

colorToCharacter = {v: k for k, v in characterToColor.items()};

whiteColor = (75, 75, 75);


def encryptImage(text, image):
    image = Image.open(image)

    width, height = image.size
    pixels = image.load()
    if len(text) > width * height:
        raise Exception("Text too long")

    index = 0
    encrypted_text = ''
    for y in range(height):
        for x in range(width):
            if index < len(text):
                character = text[index]
                color = characterToColor[character]
                index += 1
                encrypted_text += character
            else:
                color = (255, 255, 255)
                # color =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pixels[x, y] = color

    image.save('encrypted.png')
    print("Encrypted image saved")


def decryptImage(image):
    image = Image.open(image)
    width, height = image.size
    pixels = image.load()
    decryptText = ""
    for y in range(height):
        for x in range(width):
            color = pixels[x, y]
            character = colorToCharacter.get(color, '')
            if character is not None:
                decryptText += character
            else:
                decryptText += ""
    return decryptText

def displayImage(tkWindow,image,changeColumn):
    imageShow = Image.open(image)
    image_label = tk.Label(tkWindow ,width=300, height=300)
    if(changeColumn == True):
        image_label.grid(row=3, column=0)
    else:
        image_label.grid(row=3, column=2)
    image1 = ImageTk.PhotoImage(imageShow)
    image_label.imageShow = image1;
    image_label.config(image=image1)

def encryptGUI(text_entry, entry,tkWindow):
    text = text_entry.get().upper()
    image = entry.get()
    encryptImage(text, image)
    displayImage(tkWindow, image,True)


def decryptGUI(entry, tkWindow):
    decrypted = decryptImage(entry)
    image = Image.open(entry)

    displayImage(tkWindow,entry,False)
    print("Decrypted Text:", decrypted)


def GUI():
    root = tk.Tk()
    root.minsize(1000, 800)
    # root.geometry("500x500+0+0")

    root.title("Image Text Encryption")

    # Text input
    text_label = tk.Label(root, text="Enter text:",width=0)
    text_label.grid(row=0, column=0)

    text_entry = tk.Entry(root, width=20, font=("Helvetica", 20))
    text_entry.grid(row=0, column=1, padx=5, pady=5)

    # Image selection
    file_label = tk.Label(root, text="Select image:",width=00)
    file_label.grid(row=1, column=0)

    entry = tk.Entry(root, width=20, font=("Helvetica", 20))
    entry.grid(row=1, column=1, padx=5, pady=5)

    # Buttons for encryption and decryption

    encrypt_button = tk.Button(root, text="Encrypt" ,command=lambda: encryptGUI(text_entry, entry,root),font=("Helvetica", 15))
    encrypt_button.grid(row=2, column=0)
    imageForDecrypt = "encrypted.png"
    decrypt_button = tk.Button(root, text="Decrypt", command=lambda: decryptGUI(imageForDecrypt, root),font=("Helvetica", 15))
    decrypt_button.grid(row=2, column=1,padx=5, pady=5)
    root.mainloop()


def main():
    GUI()


if __name__ == '__main__':
    main()
