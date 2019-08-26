import collections
#from collections import Iterator

def isiter(obj):
    return (hasattr(obj,'__iter__'))and(hasattr(obj,'__next__'))

it1=iter([1,2,3])
print(it1)

#for i in it1:
#    print(i)

print(next(it1))
print(next(it1))
print(next(it1))

print(it1)

#print(isinstance(fib,collections.Iterator))
print((hasattr(it1,'__iter__'))and(hasattr(it1,'__next__')))
print(isiter(it1))
print(isiter([]))
print("-----------------------------------------------------------------------")

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 返回迭代器对象本身
    def __iter__(self):
        print('iter test')
        return self

    # 返回容器下一个元素
    def __next__(self):
        print('next test')
        self.a, self.b = self.b, self.a + self.b
        return self.a

def main():
    fib = Fib()    # fib 是一个迭代器
    #print('isinstance(fib, Iterator): ', isinstance(fib,collections.Iterator))

    '''for i in fib:
        if i > 10:
            break
        print(i)
    '''
    print(next(fib))
    print(next(fib))
    print(next(fib))
    
main()

