def maxtest(a,b,c=None):
    if isinstance(a,int) and isinstance (b,int) and isinstance (c,int):
        print(max(a,b,c))

    elif isinstance(a,int) and isinstance (b,int):
        print(max(a,b))
        
maxtest(-1,-2)
maxtest(1,2,3)
