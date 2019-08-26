import win32api  
import win32con  
import win32gui




if __name__=="__main__":
    for i in range(10):
        win32api.MessageBox(0, "發生錯誤!!", "錯誤",win32con.MB_ICONWARNING)
