from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("In.png") as img:
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save("Out.png")



main()