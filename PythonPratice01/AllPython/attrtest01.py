class test():
    a=10
    b=20
    c=30

t1=test()
print(getattr(t1,'a'))
setattr(t1,'d',87)
print(getattr(t1,'d'))
t1.b=22
print('------------------------------------------------------------')
print(t1.__class__.__dict__)
print('------------------------------------------------------------')
print(t1.__dict__)
print('------------------------------------------------------------')
print(t1.__class__.__dict__['b'])
print(t1.b)
print(t1.d)
