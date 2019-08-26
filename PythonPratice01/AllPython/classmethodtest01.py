class test():
    n1=0
    
    @classmethod
    def __init__(self):
        self.n2=0
        
    @classmethod
    def numAdd1(self):
        self.n1+=1
        
    @classmethod
    def numAdd2(self):
        self.n2+=1

#print(test.n1,test.n2)
OwO=test()
print(OwO.n1,OwO.n2)
OwO.numAdd1()
OwO.numAdd2()
print(OwO.n1,OwO.n2)
test.n1+=1
test.n2+=1
print(OwO.n1,OwO.n2)
