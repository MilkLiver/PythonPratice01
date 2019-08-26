class Hello:
    def show(self):
        print("hello!!")

Hello             # 這是 class object 自己本身
a=Hello()           # 這是 class object 建立出來的 class instance
b=Hello.__call__()  # 這行實際的作用跟上一行完全相同
a.show()
b.show()
print("a:",a.__class__,"b:",b.__class__)

class Hello2:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("hello!!",self.a,self.b)

a2=Hello2(1,2)
b2=Hello2.__call__(3,4)
a2.show()
b2.show()
