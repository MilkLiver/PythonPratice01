#m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
#for i in m:
#    print(i,m[i])

def test(num):
    for i in range(0,num):
        yield i

a=test(5)
print(next(a))
print(next(a))
print(next(a))
#for i in test(5):
#    print(i)

a_generator = (item**2 for item in range(5))
print(a_generator)
print(next(a_generator))    # 0
print(next(a_generator))    # 1
print(next(a_generator))    # 4


