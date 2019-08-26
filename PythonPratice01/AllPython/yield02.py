s=sum(i for i in range(100000000))
print(s)
#s2=sum([i for i in range(100000000)])
#print(s)

t1=[i for i in range(1,10)]
print(type(t1))
print(t1)
#print(t1[2])

t2=(i for i in range(1,10))
print(type(t2))
print(t2)
#print(t2[2])

print('-----------------------------------------------------------------------')

s1=(i for i in range(50))
print(type(s1))

print('-----------------------------------------------------------------------')

def container(start, end):
    while start < end:
        yield start
        start += 1
c = container(0, 5)
print(type(c))
print(next(c))
next(c)
for i in c:
    print(i)
