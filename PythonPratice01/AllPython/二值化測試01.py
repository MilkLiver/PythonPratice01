import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import skimage.io

def imgtogray():
    img=Image.open(r"D:\test\test.png")
    img=img.convert("L")
    img.show()
    img.save(r"D:\test\test_gray.jpg")


def imgbinary01():
    img2=Image.open(r"D:\test\test_gray.jpg")
    img2=img2.convert("1")
    img2.show()


def imgbinary03(threshold = 200):
    #threshold = 200
 
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    print(table)

    img3=Image.open(r"D:\test\test_gray.jpg")
    photo = img3.point(table, '1')
    photo.show()


def imgbinary04():
    img4_po = skimage.io.imread(r"D:\test\test_gray.jpg")
    img4=Image.open(r"D:\test\test_gray.jpg")

    WHITE, BLACK = 255, 0
    img_mean=np.mean(img4_po)
    img4 = img4.point(lambda x: WHITE if x > img_mean else BLACK)

    img4.show()


def main():
    #bina=int(input(":"))
    #imgbinary03(bina)
    imgbinary04()

if __name__=="__main__":
    main()


