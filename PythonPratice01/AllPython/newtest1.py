class Singleton(object):
    
    def __new__(cls):
        print("OwO",cls)
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        '''if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)'''
        return cls
    
    def __init__(self):
        print("OAO",self)

    def test():
        print('test')

    
obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value1'
print (obj1.attr1, obj2.attr1)
print (obj1 is obj2)
obj1.test()

