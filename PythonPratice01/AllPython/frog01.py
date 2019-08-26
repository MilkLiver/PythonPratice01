def fun(n):
    if(n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return fun(n-1)+fun(n-2)

print(fun(int(input("stairs: "))))
