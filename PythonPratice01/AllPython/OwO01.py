import random as ra
a=ra.randint(1,1000)
gn=0
while True:
    try:
        i=int(input('Please guess a number: '))
        if i==a:
            print('correct!!')
            print('You guess',gn,'times')
            gn+=1
            break
        elif i<a:
            print('more big')
        elif i>a:
            print('more small')
        gn+=1
    except:
        print('Wrong!! input again!!')

    
