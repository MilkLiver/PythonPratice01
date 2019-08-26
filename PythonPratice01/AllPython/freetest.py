mylist = [x*x for x in range(3)]
mylist2 = (x*x for x in range(3))
print(mylist)
print(mylist2)

for i in mylist:
    print(i)

for i in mylist2:
    print(i)

li=range(3)
print(li)
for i in li:
    print(i)
print("------------------------------------------------")
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

print(createGenerator)
test01= createGenerator()

print(test01)
for i in test01:
    print(i)
    
print(test01)
for i in test01:
    print(i)


