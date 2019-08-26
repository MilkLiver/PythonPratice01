from functools import wraps
class A():
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
    def say(self):
        print('hello')
def clatest(cla):
    cla.name='function reset'
    
d={}
aa='test'
h1=A(aa+'OAO')
d[aa]=h1

d[aa].show()
d['test'].say()

'''
from=A(123)
def ttest():
    c=123456
print(c)'''

users={}

ht='OwO'
ta=A(ht)
users[ht]=ta

ht='OUO'
ta=A(ht)
users[ht]=ta

itest='OwO'
users[itest].say()
users[itest].show()

itest='OUO'
users[itest].show()

clatest(users[itest])
users[itest].show()


