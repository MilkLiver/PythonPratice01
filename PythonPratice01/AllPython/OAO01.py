import random as ra
a=ra.randint(1,1000)
gn=0
while True:
    try:
        li=ra.sample(range(1,1001),1000)
        #print(li)
        for lin in li:
            print(lin)
            if lin==a:
                print('correct!!')
                print('You guess',gn,'times')
                gn+=1
                break
            elif lin<a:
                print('more big')
            elif lin>a:
                print('more small')
            gn+=1
        break
    except:
        print('Wrong!! input again!!')

    
