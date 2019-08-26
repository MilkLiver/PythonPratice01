import os
import shutil

path1=os.path.dirname(__file__)+"/origin_imgs"
path2=os.path.dirname(__file__)+"/origin_imgs2"
print(path1)
pa1dir=os.listdir(path1)



shutil.copytree(path1, path2,symlinks=False, ignore=None)


print("finish")
