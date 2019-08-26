from functools import wraps


def func1(n1):
    a=100
    def func2():
        a=200
        def func3():
            #nonlocal a
            a=300
            print("fff",a)
        func3()
        return print("ff",a)
    func2()
    return print("f",a)

func1(88)


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
class cls1():
    a=687
    def func1(self):
        a=100
        print("cls",a)

@dec1
class cls2():
    pass

@dec1
def funcc1():
    print("funcc OwO!!")

#funcc1()
#cls1().func1()
#cls2()

print("-----------------------------------------------------------------------")

def test1(cls):
    a=87
    c={}
    def te1():
        if a==87:
            pass
            #a=cls
            #c['test']="test"
        return print("OwO")
    return te1

@test1
class cls2():
    pass

cls2()
