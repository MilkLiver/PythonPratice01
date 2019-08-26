def fib(end = 1000):
    prev,curr=0,1
    while curr < end:
        yield curr
        prev,curr=curr,curr+prev


#print(list(fib()))
'''for i in fib():
    print(i)'''

f1=fib()
print(type(fib()))
print(list(f1))

'''print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))'''
