#from mm import multimethod

def foo(a, b):
    if isinstance(a, int) and isinstance(b, int):
        print("A",a,b)
    elif isinstance(a, float) and isinstance(b, float):
        print("B",a,b)
    elif isinstance(a, str) and isinstance(b, str):
        print("C",a,b)

foo(5,6)
foo(1.2,22.3)
foo("OwO","OAO")
foo(1,"QAQ")

listC = [('e', 4), ('o', 2), ('!', 5), ('v', 3), ('l', 1)]
print(sorted(listC, key=lambda x: x[1]))
#listC.sort()
print(listC)
a=listC.sort(key=lambda x:x[1])
print(a)
print(listC)
for i in map(lambda x:x if x*2>=5 else "OwO",{1,2,3,4,5}):
    print(i,end=' ')

print('-----------------------------------------------------------------------')
a=int
print(isinstance(68,a))
tl=[int,str]
