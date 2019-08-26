import numpy as np
from PIL import Image
import skimage.io
from skimage import data, filters
import matplotlib.pyplot as plt




def imgbinary04():
    img_po = skimage.io.imread(r"D:\PyAI3\4\binaryImg\test_gray.jpg")
    img=Image.open(r"D:\PyAI3\4\binaryImg\test_gray.jpg")
    image = np.array(img)

    WHITE, BLACK = 255, 0
    thresh = filters.threshold_otsu(image)

    img = img.point(lambda x: WHITE if x > thresh else BLACK)
    img=img.convert('RGB')
    img.show()
    img.save(r"D:\PyAI3\4\binaryImg\test_binary.jpg")

def main():
    imgbinary04()


if __name__=="__main__":
    main()
