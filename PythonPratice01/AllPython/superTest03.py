class A(object):
    pass

class B(object):
    pass

class C(A):
    pass

class D(A):
    pass

class E(C,D):
    pass

class F(C,B):
    pass

class G(E,F):
    pass

test=G()
print(G.mro())
