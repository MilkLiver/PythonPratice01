class A(object):
    def __init__(self):
        print ('A')

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print ('C')
    def show(self):
        print("test")

#test1=C()
#test1.show()

class FooParent(object):
    def show(self):
        print("Parent's show")

class test(FooParent):
    def show(self):
        super().show()
        print("show")

test2=test()
test2.show()

class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print(p1.name) 
print(p2.name)
print(Person.name)

p2.name.append(2)
print(p1.name) 
print(p2.name)
print(Person.name)
