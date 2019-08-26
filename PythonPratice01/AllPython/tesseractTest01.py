from PIL import Image
import pytesseract

img_path=r"D:\TesseractOCR\TesseractFile"
img_Name=r"testNumber01.png"
res_path=r"D:\TesseractOCR\TesseractFile"
res_Name=r"result.txt"


def main():
    img=Image.open(img_path+"//"+img_Name)
    #img.show()
    text=pytesseract.image_to_string(img)
    print(text)


if __name__=="__main__":
    main()
