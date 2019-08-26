import random as ra

gn=0
ran=10000
a=ra.randint(1,ran)
while True:
    try:
        li=ra.sample(range(1,ran+1),ran)
        while True:
            rli=li.copy()
            num=ra.sample(li,1)
            lin=num[0]
            trn=lin
            print(lin)
            if lin==a:
                print('correct!!')
                print('You guess',gn,'times')
                li.remove(lin)
                gn+=1
                break
            elif lin<a:
                print('more big')
                for nn in rli:
                    if  nn<=trn:
                        li.remove(nn)
            elif lin>a:
                print('more small')
                for nn in rli:
                    if  nn>=trn:
                        li.remove(nn)
            #li.remove(lin)
            gn+=1
        print(li)
        break
    except:
        print('Wrong!! input again!!')
        

    
