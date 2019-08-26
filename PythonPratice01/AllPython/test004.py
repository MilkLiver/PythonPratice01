'''class test(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    @staticmethod
    def add(self,a,b):
        print(a+b)
        print(self.a)


test.add(1,2)

t1=test(2,5)'''

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self,z):
        print(self.name)
        print ("%s: %s" % (self.name, self.score))

s1=Student("OAO",87)
s1.print_score("78")
