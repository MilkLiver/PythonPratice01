import random as ra
import time
class c1():
    hp=1
    atk=0
    deff=0
    age=18
    def __init__(self,name):
        self.name=name
    def getability(self):
        self.hp=ra.randint(500,1000)
        self.atk=ra.randint(70,100)
        self.deff=ra.randint(10,50)
        print('姓名:',self.name)
        print('HP:',self.hp)
        print('ATK:',self.atk)
        print('DEF',self.deff)
        print('')
    def info(self):
        print('姓名',self.name,'年齡',self.age)
    def bark(self):
        print(self.name,'say','汪汪!')
    def cdamage(player1,damage):
        if damage<=0:
            damage=0
            print(player1.name,'沒有受到傷害')
        elif damage<=10 and damage>=1:
            print('好像有受到攻擊?')
            print(player1.name,'受到',damage,'傷害')
        elif damage<=20 and damage>=11:
            print('受到點擦傷')
            print(player1.name,'受到',damage,'傷害')
        elif damage<=30 and damage>=21:
            print('有點受到傷害')
            print(player1.name,'受到',damage,'傷害')
        elif damage<=40 and damage>=31:
            print('稍微受到攻擊')
            print(player1.name,'受到',damage,'傷害')
        elif damage<=50 and damage>=41:
            print('受到攻擊')
            print(player1.name,'受到',damage,'傷害')
        elif damage<=60 and damage>=51:
            print('受到中等傷害')
            print(player1.name,'受到',damage,'傷害')
        elif damage<=70 and damage>=61:
            print('遭受重擊')
            print(player1.name,'受到',damage,'傷害')
        elif damage<=80 and damage>=71:
            print('被爆擊')
            print(player1.name,'受到',damage,'傷害')
        elif damage>=81:
            print('受到致命傷')
            print(player1.name,'受到',damage,'傷害')
        print('')
            
    def fight(self,other):
        print(self.name,'VS',other.name)
        first=ra.randint(0,1)
        rnd=first
        while True:
            time.sleep(0.5)
            if self.hp<=0:
                print(other.name,'Win')
                print("HP剩餘:",other.hp)
                break
            elif other.hp<=0:
                print(self.name,'Win')
                print("HP剩餘:",self.hp)
                break
            
            if rnd==0:
                ratk=ra.randint(self.atk//2,self.atk)
                damage=ratk-other.deff
                if damage<=0:
                    damage=0
                else:
                    other.hp-=damage
                other.cdamage(damage)
                rnd=1
                
            elif rnd==1:
                ratk=ra.randint(other.atk//2,other.atk)
                damage=ratk-self.deff
                if damage<=0:
                    damage=0
                else:
                    self.hp-=damage
                self.cdamage(damage)
                rnd=0
            

#h1=c1('宇航')
#h1.getability()

#h2=c1('東霖')
#h2.getability()

#h1.fight(h2)

while True:
    game=input('開始遊玩? y/n ')
    if game=='y':
        n1=input('輸入玩家1: ')
        n2=input('輸入玩家2: ')
        p1=c1(n1)
        p2=c1(n2)
        p1.getability()
        p2.getability()
        while True:
            sq=input('是否開始? y/n ')
            if sq=='y':
                p1.fight(p2)
                break
            elif sq=='n':
                break
                
    elif game=='n':
        print('結束遊戲')
        break
