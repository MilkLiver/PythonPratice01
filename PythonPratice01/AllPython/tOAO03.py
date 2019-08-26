import random as ra

gn=0
ran=10000
a=ra.randint(1,ran)
pround='human'
while True:
    try:
        li=ra.sample(range(1,ran+1),ran)
        while True:
            rli=li.copy()
            if pround=='computer':
                num=ra.sample(li,1)
                lin=num[0]
                print('computer guess:',lin)
            elif pround=='human':
                lin=int(input('guess a number: '))
                #print('')
                #print('human guess:',lin)

            
            if lin==a:
                print('correct!!')
                print(pround,'Win')
                print('Rounds:',gn)
                li.remove(lin)
                gn+=1
                break
            
            elif lin<a:
                print('more big')
                print('')
                if lin in li:
                    for nn in rli:
                        if  nn<=lin:
                            li.remove(nn)
                        
            elif lin>a:
                print('more small')
                print('')
                if lin in li:
                    for nn in rli:
                        if  nn>=lin:
                            li.remove(nn)

            if pround=='human':
                pround='computer'

            elif pround=='computer':
                pround='human'
                            
            gn+=1
        print(li)
        break
    except:
        print('Input Wrong!!Please input again')
        

    
