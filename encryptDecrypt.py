from PIL import Image

characterToColor={
    'A':(255,0,10),
    'B':(0,255,0),
    'C':(0,0,255),
    'D':(200,100,20),
    'E':(255,10,30),
    'F':(255,40,50),
    'G':(130,30,50),
    'H':(225,10,60),
    'I':(5,150,80),
    'J':(2,140,90),
    'K':(55,201,0),
    'L':(75,200,1),
    'M':(155,90,9),
    'N':(65,100,54),
    'O':(95,120,43),
    'P':(105,100,32),
    'Q':(42,90,21),
    'R':(131,0,100),
    'S':(231,20,4),
    'T':(222,30,5),
    'U':(254,30,87),
    'V':(201,40,85),
    'W':(110,70,21),
    'X':(130,30,32),
    'Y':(120,20,10),
    'Z':(70,10,2),
    ' ':(133,23,55),
    '0':(246,3,5),
    '1':(32,54,55),
    '2':(13,66,55),
    '3':(53,77,55),
    '4':(63,98,55),
    '5':(103,22,55),
    '6':(113,54,55),
    '7':(123,59,55),
    '8':(153,69,55),
    '9':(173,79,55),
}

colorToCharacter = {v: k for k, v in characterToColor.items()};
def encryptImage(text,image):
    text.upper()
    image=Image.open(image)
    width, height= image.size
    pixels=image.load()
    if len(text) >width *height:
        print("Text too long")

    index = 0;
    encrypted_text =''
    for x in range(height):
     for y in range(width):
        if index <len(text):
            character = text[index]
            color = characterToColor[character]
            pixels[x, y] = color
            index += 1
            encrypted_text += character;

        else:
           index = 0
        break

     else:
         continue
     break;

     print("Encrypted text:", encrypted_text)
     image.save('encrypted.png')
     print("Encrypted image saved")

     def decryptImage(image):
        image = Image.open(image)
        width, height = image.size
        pixels = image.load()
        decryptText = "";
for y in range(height):
    for x in range(width):
        color = pixels[x, y]
        character = colorToCharacter.get(color,'')
        if character is not None:
            decryptText += character
        else:
            decryptText +=""


print("Decrypted image saved")
return decryptText
    def main():
        textEncrypt = "pls1 go somewhere"
        textEncryptedUppercase = textEncrypt.upper()
        image = "5LYzTBVoS196gvYvw3zjwBljwV2tMj4gpWc8vE-5S20.jpg"

        encryptImage(textEncryptedUppercase, image);
