import os
import shutil

path1=os.path.dirname(__file__)+"/origin_imgs"
path2=os.path.dirname(__file__)+"/origin_imgs2"
print(path1)
pa1dir=os.listdir(path1)

newfolder = os.path.exists(path2)
if not newfolder:
    os.makedirs(path2)


for file in pa1dir:
    fpath1=path1+"/"+str(file)
    fpath2=path2+"/"+str(file)
    with open(fpath1,'rb') as fread:
        with open(fpath2,"wb") as fcopy:
            print(fpath2)
            #print(file)
            fcopy.write(fread.read())

#with open(path,"rb") as fread:
#    with open(path,"wb") as fcopy:
#        fcopy.write(fread.read())


#shutil.copyfile(path,path2)



print("finish")
