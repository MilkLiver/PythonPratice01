import hashlib


m=hashlib.md5()
s='123'
m.update(s.encode("utf8"))
h=m.hexdigest()
print(h)


s2='123'
m2=hashlib.md5(s2.encode('utf8'))
h2=m2.hexdigest()
print(h)
