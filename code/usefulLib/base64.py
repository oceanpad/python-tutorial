import base64

with open("./profile.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    with open("./ttt.txt", "w") as ttt:
        ttt.write(str(encoded_string))
