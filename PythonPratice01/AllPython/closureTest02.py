def test():
    a=None
    def ttest(*args):
        if args:
            a=args[0]
        print(a)
    return ttest

#t1=test()
#t1(5)
#t2=test()
#t2()


def test2():
    a={}
    def ttest2(*args):
        if args:
            a['test2']=args[0]
            #print(a['test2'])
            print(a['test2'])
            return print(a)
        else:
            return print(a)
    return ttest2

t3=test2()
t3(7)
t4=test2()
t4()
