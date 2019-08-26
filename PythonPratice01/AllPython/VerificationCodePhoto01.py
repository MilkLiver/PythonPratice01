import random
import urllib.request
from urllib.request import urlretrieve
import os

url = 'http://www.moguproxy.com/proxy/validateCode/createCode?time={}'
path = os.path.dirname(__file__) + '/origin_imgs/' #将下载的图片保存到当前目录下的origin_imgs文件夹中

folder = os.path.exists(path)
if not folder:
    os.makedirs(path)

for i in range(1531878600001,1531878600501):
    req=urllib.request.Request(url.format(i))
    response=urllib.request.urlopen(req)

    #print(path)

    with open(path+str(i)+".jpg","wb") as sp:
        sp.write(response.read())
        sp.close

#for i in range(1531878604000,1531878604300):
#    urlretrieve(url.format(i), path + str(i)[-3:] + '.jpg')
#    print('成功下载 {} 张图片'.format(str(i)[-3:]))
