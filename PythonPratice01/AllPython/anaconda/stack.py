import os
import sys
import datetime as dt
import numpy as np



def main(argc,argv,envp):
    a=np.arange(1,10).reshape(3,3)
    b=a*10
    print(a,b,sep='\n')

    c=np.vstack((a,b))
    print(c)

    d=np.hstack((a,b))
    print(d)

    print("d----------------------------------------------------")

    e=np.dstack((a,b))
    print(e)
    #print(np.row_stack((a,b)))
    print("----------------------------------------------------")
    print(e.transpose())
    #print(e.T)

    print("----------------------------------------------------")

    f=a.ravel()
    g=b.ravel()
    h=g*10
    print(f,g,h,sep='\n')

    print("row------------------------------------------------------")

    i=np.row_stack((f,g,h))
    print(i)
    print(np.vstack((f,g,h)))

    
    print("column------------------------------------------------------")
    
    j=np.column_stack((f,g,h))
    print(j)

    print("------------------------------------------------------")

    k,l,m=np.vsplit(c,3)
    print(k,l,m,sep='\n')

    n,o,p=np.hsplit(d,3)
    print(n,o,p,sep='\n')

    print("------------------------------------------------------")

    q,r=np.dsplit(e,2)
    #print(q.transpose())
    q = q.transpose()[0].transpose()
    r = r.transpose()[0].transpose()
    print(q,r,sep='\n')

    return 0

if __name__=="__main__":
    #sys.exit(main(len(sys.argv),sys.argv,os.environ))
    main(len(sys.argv),sys.argv,os.environ)