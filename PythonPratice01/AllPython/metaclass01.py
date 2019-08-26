class test2():
    t2='test2'

class Metaclass(type):
    def __new__(cls, name, bases, dct):
        print('cls:',cls)
        print('HAHAHA')
        dct['a'] = 1
        return type.__new__(cls, name, bases, dct)
        #return type(name, bases, dct)

class test():
    t='test'


print('before Create OBJ')

class OBJ(test,test2,metaclass=Metaclass):
    #__metaclass__ = Metaclass
    pass

class OBJ2(metaclass=Metaclass):
    pass
    
print('after Create OBJ')

if __name__ == '__main__':
    #print(OBJ.__dict__)
    print(hasattr(OBJ,'a'))
    print(OBJ.a)
    print(OBJ.__name__)
    print(OBJ.__bases__)
    print(id(OBJ2.a))
    print(id(OBJ.a))
    
    print("-----------------------------------------------------------------")
    
    testOwO1=type.__new__(type,'test1',(),{})
    print(testOwO1)
    testOwO2=type('test2',(),{})
    print(testOwO2)

