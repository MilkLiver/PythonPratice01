class SomeMeta(type):
    def __call__(definedclz, *args, **kwargs):
        print('__new__')
        instance = definedclz.__new__(definedclz, *args, **kwargs)
        print('__init__')
        definedclz.__init__(instance, *args, **kwargs)
        return instance

class Some(metaclass=SomeMeta):
    def __new__(clz):
        print('Some __new__')
        return object.__new__(clz)
    def __init__(self):
        print('Some __init__')
    '''def __call__():
        print("test")'''

#print(id(Some))
#print(id(Some()))
print(Some.__class__)
a=Some()
print(id(a))

print("-----------------------------------------------------------------------")

b=Some.__call__()
print(type(b))
print(b.__class__.__class__)
