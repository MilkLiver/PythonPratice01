class parents(object):
    __n1=1
    _n2=2
    n3=3
    def pn1(self):
        print(__n1)
        
    def pn2(self):
        print(__n1)
        
    def pn3(self):
        print(__n1)

class child1(parents):
    __n1=11
    _n2=22
    n3=33

print(child1)
