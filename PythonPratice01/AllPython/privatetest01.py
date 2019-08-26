class test:
    a=10
    _b=20
    __c=30
    
    def show(self):
        return self.__c

    def show2(self):
        return self.a,self._b,self.__c

t1=test()
print(t1.a)
print(t1._b)
#print(t1.__c) error

print(t1.show())
print(t1._test__c)
#print(dir(t1))
#print(t1.__class__.__dict__)

class test2(test):
    a=11
    _b=22
    __c=33

    '''def show2(self):
        return self.a,self._b,self.__c'''
    
print(t1.show2())
t2=test2()
print(t2.show2())
