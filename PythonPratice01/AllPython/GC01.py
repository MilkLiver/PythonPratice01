from sys import getrefcount
import gc


collected = gc.collect()

a = [1,2,3]
a.append(4)
print(getrefcount(a))
b=a
print(getrefcount(a))
print(getrefcount(b))
print('----------------------------------------------------------------------')

print("Garbage collector: collected %d objects." % (collected))
print(getrefcount(a))
print(getrefcount(b))
print('----------------------------------------------------------------------')

