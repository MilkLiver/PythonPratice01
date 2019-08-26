
'''
class Foo(object):
…       bar = True
         Test='type test'

Foo=Foo()
'''

Foo = type('Foo', (), {'bar':True,'test':'type test'}) #等於上面
print(Foo.bar)
print(Foo.test)

print("--------------------------------------------------------------------")

class FooParent(object):
    def show(self):
        print("Parent's show")

FooChild=type('FooChild',(FooParent,),{})
#FooChild.show()
print("test")


print("--------------------------------------------------------------------")

def __init__(self):
    pass

def show1(self):
    print("test1 show")

test1=type('test1',(object,),{'__init__':__init__,'show':show1})
t1=test1()
t1.show()
print(t1.__class__)
print("--------------------------------------------------------------------")

class OUO():
    def test(self):
        print("OUO test")

t2=OUO()
t2.test()
#OUO.test() #error!!
print(t2.__class__)
setattr(t2,'id',687)
print(t2.id)

