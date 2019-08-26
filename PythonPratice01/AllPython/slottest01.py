

class test1():
    a=5
    __slots__=['b']
    def __init__(self):
        self.b=55
    def show(self):
        print("OwO")

test1().show()
print(test1().a)

t1=test1()
print(t1.b)
