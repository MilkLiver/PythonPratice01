import os


#dir01=os.listdir("D:/OwO")
dir01="D:/OwO"
newfolder = os.path.exists(dir01)

if not newfolder:
    os.makedirs(dir01)
