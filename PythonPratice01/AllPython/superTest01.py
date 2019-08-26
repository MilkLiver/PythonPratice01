class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        print("A1.m",m)
        print("A1.self.n",self.n)
        self.n += m
        print("A2.m",m)
        print("A2.self.n",self.n)


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        print("B2.m",m)
        print("B2.self.n",self.n)
        super().add(m)
        self.n += 3

b = B()
b.add(2)
print(b.n)

class A(object):pass
class B(object):pass
class C(object):pass
class E(A,B):pass
class F(B,C):pass
class G(E,F):pass

print(G.mro())
