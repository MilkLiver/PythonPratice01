import numpy as np
from PIL import Image
from skimage import data, filters
import matplotlib.pyplot as plt




def imgtogray():
    img=Image.open(r"D:\PyAI3\4\selectedImg\SCH_20190109164623_168_plate_1.png")
    img=img.convert("L")
    img.show()
    img.save(r"D:\PyAI3\4\binaryImg\test01.jpg")

def main():
    img=Image.open(r"D:\PyAI3\4\binaryImg\test01.jpg")
    image = np.array(img)

    thresh = filters.threshold_otsu(image)
    print(thresh)
    dst = (image >= thresh)*1.0
    print(dst)

    plt.imshow(dst, plt.cm.gray)
    #plt.show()

    im = Image.fromarray(dst*255)
    im=im.convert('RGB')
    im.save(r"D:\PyAI3\4\binaryImg\test01_binary.jpg")
    

    
if __name__=="__main__":
    imgtogray()
    main()
