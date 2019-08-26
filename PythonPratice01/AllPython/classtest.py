class A:
    def __init__(self):
        #super(A,self).__init__()
        print('A')

class B(A):
    def __init__(self):
        super(B,self).__init__()
        print('B')

class C(A):
    def __init__(self):
        #super(C,self).__init__()
        print('C')

class D(B):
    def __init__(self):
        super(D,self).__init__()
        print('D')

class E(C):
    def __init__(self):
        super(E,self).__init__()
        print('E')

class F(D,E):
    def __init__(self):
        super(F,self).__init__()
        print('F')
    pass

test=F()
