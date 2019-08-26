import os, sys




#sys.exit(0)
try:
    print("sys exit")
    sys.exit(0)
except BaseException as error:
    print('die')
    print(error)
finally:
    print('cleanup')
    
print("test\n\n")

try:
    print("os exit")
    os._exit(0)
except:
    print('die')
print('os.exit')#不打印直接退出了
