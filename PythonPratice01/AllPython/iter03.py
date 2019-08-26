class String(object):
    a=10
    def __init__(self, val):
        self.val = val

    def __str__(self):
        print('__str__')
        return self.val

    def __repr__(self):
        print("__repr__")
        return "__repr__2"
    
    def __call__(self):
        print('__call__')

    def __getitem__(self,num):
        print("__getitem__",num)
    
    def __iter__(self):
        print("This is __iter__ method of String class")
        return iter(self.val)  #self.val is python string so iter() will return it's iterator

st = String('Sample String')
print(st)
print(st())
print(iter(st))
print(st['a'])
print("----------------------------------------------------------------------")
print(st)
print(repr(st))
#print(next(st))
