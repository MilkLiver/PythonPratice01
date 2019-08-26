
m=1
n=1
def func1():
    a=1
    b=1
    c=1
    d=1
    e=1
    l={}
    def func2():
        nonlocal c,d
        try:
            if a:
                a="atest"
                print("a:",a)
        except:
            print("a error")
        try:
            if b:
                #b="btest"
                print("b:",b)
        except:
            print("b error")
            
        try:
            if c:
                c="ctest"
                print("c:",c)
        except:
            print("c error")
        try:
            if d:
                #d="dtest"
                print("d:",d)
        except:
            print("d error")
        try:
            e+=1
            print(e)
        except:
            print("e error")
        try:
            if m:
                m+=1
                print(m)
        except:
            print("m error")
        try:
            global n
            n+=1
            print(n)
        except:
            print("n error")
    func2()
    return print("\nafter:\na:",a,"\nb:",b,"\nc:",c,"\nd:",d,"\ne:",e,"\nm:",m
                 ,"\nn:",n)

func1()

print("-----------------------------------------------------------------------")

