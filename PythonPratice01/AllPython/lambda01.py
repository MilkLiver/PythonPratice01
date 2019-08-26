score = int(input('請輸入分數：'))
level = score // 10

dic={
    10 : lambda: print('Perfect'),
    9  : lambda: print('A'),
    8  : lambda: print('B'),
    7  : lambda: print('C'),
    6  : lambda: print('D')
}.get(level, lambda: print('E'))()
x=6

print((lambda x:"%s > 50"%x if x>50 else "%s < 50"%x)(score))

lat=lambda x:"OAO" if x>5 else 'OwO'
print(lat(7))
