def h():
    print('OwO')
    a=yield 5
    print(a)
    print('OAO')
    b=yield 87
    print('OUO')
    yield 687
    print("QQQ")
    yield "the end"
#
print('test')

c = h()
print(c.__next__())
print('------------------------------')
print(c.__next__())
print('------------------------------')
c.send("QAQ")
print(c.__next__())
