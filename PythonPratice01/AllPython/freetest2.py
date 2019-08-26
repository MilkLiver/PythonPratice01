def func():
    x = 10
    def getX():
        print(x)
        return x
    def setX(n):
        x = n
        print(n)
    return (getX,setX)

getX, setX = func()
    
getX()
setX(66)
getX()

print("------------------------------------------------------------------------")

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)

b=[[1,3],[4,2]]
b.sort(key=lambda OwO:OwO[1])
print(b)

print("------------------------------------------------------------------------")





