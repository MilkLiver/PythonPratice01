import os
import sys
import datetime as dt
import numpy as np



def main(argc,argv,envp):
    a=np.arange(1,7)
    print("a",a)

    b=a.reshape(2,3)
    print("b",b)

    b[0][0]+=10
    print("b",b)
    print("a",a)

    print('-'*80)#-------------------------------------------------------
    
    c=b.reshape(6)
    c[2]*=10
    print("c",c)
    print("b",b)

    d=b.ravel()
    d[3]*=10
    print("d",d)
    print("b",b)

    e=b.flatten()
    e[0]-=10
    print("e",e)
    print("b",b)

    print('-'*80)#-------------------------------------------------------
    
    a.shape=(2,3)
    print('a',a)
    print('c',c)
    
    a.resize((3,2))
    print('a',a)

    '''
    f=a.transpose()
    print(f)
    print(a)

    g=e.transpose()
    print(g)

    h=np.array([e]).transpose()
    print(h)

    i=e.reshape(-1,1)
    print(i)'''

    return 0

if __name__=="__main__":
    sys.exit(main(len(sys.argv),sys.argv,os.environ))
