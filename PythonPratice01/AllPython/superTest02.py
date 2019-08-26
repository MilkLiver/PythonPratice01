class E():
    En1=0
    def __init__(self):
        self.n = 66
        E.En1+=100
        print("E init")
        
    def add(self, m):
        print('self is {0} @E.add'.format(self))
        #super().add(m)
        self.n += 17
        self.n += E.En1
        print("E:",self.n)

class A():
    def __init__(self):
        self.n = 2
        print("A init")
        
    def add(self, m):
        print('self is {0} @A.add'.format(self))
        print("selfA1:",self.n)
        self.n += m
        print("selfA2:",self.n)

class B(A):
    def __init__(self):
        self.n = 3
        print("B init")

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        print("test",m)
        self.n += 3

class C(E,A):
    def __init__(self):
        self.n = 4
        print("C init")
        
    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4

class D(B, C):
    def __init__(self):
        self.n = 5
        print("D init")

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        #print('D',D.mro())
        #print('')
        super(C,self).add(m)
        self.n += 5
        
E()
E()
print("----------------------------------------------------------------------")
d = D()
print("----------------------------------------------------------------------")
print(D.mro())
d.add(10)
print(d.n)

print("----------------------------------------------------------------------")
etest=E()
print("----------------------------------------------------------------------")
print(etest.n)
print()
