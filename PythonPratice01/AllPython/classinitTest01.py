class D():
    def __init__(self):
        self.n = 5
        print("D init")

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        self.n += 5
        print(self.n)

d=D()
d.add(1)
