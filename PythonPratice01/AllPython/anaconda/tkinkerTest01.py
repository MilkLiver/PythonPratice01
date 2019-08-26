# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:47:07 2019

@author: NEIL_YU
"""

import tkinter as tk

window = tk.Tk()
def saveNewFile():
    global window
    window.destroy()

def saveCoverFile():
    global window
    window.destroy()

def FileExistswarning():    
    
    window.title('Warning!!')
    window.geometry('270x150')

    l=tk.Label(
            window,
            text="檔案XXX已存在\n是否要覆蓋當前檔案??",
            font=('Arial', 12),
            width=100, height=4)
    l.pack()

    YesBtn=tk.Button(window,
                     bg="white", 
                     text="是",
                     width=10, height=1,
                     command=saveCoverFile)
    
    NoBtn=tk.Button(window,
                    bg="white", 
                    text="否",
                    width=10, height=1,
                    command=saveNewFile)

    YesBtn.pack()
    NoBtn.pack()

    YesBtn.place(x=30,y=110)
    NoBtn.place(x=160,y=110)
    window.mainloop()

FileExistswarning()
print("OwO")