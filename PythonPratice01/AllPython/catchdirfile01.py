import numpy as np
import os
import shutil
import re

path="c:\\users\\neil_yu\\Desktop\\ZT7000\\"
newpath="c:\\users\\neil_yu\\Desktop\\ZT7000\\neww\\"



def CopyFile(dirpath,newdirpath):
    def SameFileCopy(filename):
        same_pattern=re.compile("複製")
        if re.findall(same_pattern,filename) != []:
            sameNum_pattern=re.compile("複製_\((\d+)\)")
            Copynum=re.findall(sameNum_pattern,filename)
            #print("OwO:",re.findall(sameNum_pattern,filename))
            if Copynum!=[]:
                copyname_pattern=re.compile("複製_\(*\d*\)*\s*(.*)")
                filename=re.findall(copyname_pattern,filename)[0]
                #print("OAO:",re.findall(sameNum_pattern,filename))
                return "複製_("+str(int(Copynum[0])+1)+") "+filename
            copyname_pattern=re.compile("複製_(.*)")
            filename=re.findall(copyname_pattern,filename)[0]
            #print("test2")
            return "複製_("+str(1)+") "+filename
        return "複製_"+filename
        #if newpath
        
    for i in os.listdir(dirpath):
        if os.path.isdir(dirpath+i):
            CopyFile(dirpath+i+"\\",newdirpath)
        else:
            if os.path.exists(newdirpath+i):
                shutil.copyfile(dirpath+i,newdirpath+SameFileCopy(i))
                continue
            shutil.copyfile(dirpath+i,newdirpath+i)
            

def main():
    CopyFile(path,newpath)

if __name__=="__main__":
    main()



    
