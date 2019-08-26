class A():
    pass

class B(A):
    pass

class C(A):
    pass

class D():
    pass

class E(B,C,D):
    pass


t1=E()
print(E.mro())
