decryptText ="";
for y in range(height):
for x in range(width):
color = pixels[x,y]
character = colorToCharacter.get(color,'')
if character is not None:
decrypText += character
else:
decryptText += ""
print("Decrypted image saved")
return decrypText
