from functools import wraps

def dec1(cls):
    a=87
    @wraps(cls)
    def dfunc1():
        #nonlocal a
        if a==87:
            a=cls
        return cls()
    return dfunc1

@dec1
def funcc1():
    print("funcc OwO!!")

@dec1
class cls2():
    pass

#funcc1()
#cls2()
