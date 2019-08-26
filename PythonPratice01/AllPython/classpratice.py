class test:
    a=0
    
    def __init__(self):
        test.a+=1
        print(test.a)

    
    #@staticmethod
    @classmethod
    def test(self):
        print(self.a)

te1=test()
te2=test()
print("---------------------------------------------------------------")
#print(te1.a)
#print(te2.a)
print("---------------------------------------------------------------")
print(test.a)
test.a+=1
print(test.a)
print("---------------------------------------------------------------")
te1.test()
test.test()
