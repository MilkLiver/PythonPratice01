import numpy as np
import matplotlib.pyplot as plt
import collections as co

times=50000

def init_cards():
    cards=np.arange(1,11)
    cards=np.append(cards,[10,10,10])
    cards=np.append(np.append(np.append(cards,cards),cards),cards)
    np.random.shuffle(cards)
    #print(cards)
    #print(np.sum(cards==13))
    cardn=0
    return cards,cardn

def getcard(cards,cardn,pcard):
    while True:
        pscore=pcard.sum()
        if 1 in pcard:
            if pcard.sum()==11:
                print("BJ")
                break
            elif pcard.sum()+10<21:
                pscore=pcard.sum()+10
            else:
                pscore=pcard.sum()
        print("player1 score:",pscore)
        print(pcard)

                
        if pcard.sum()==21:
            print("BJ")
            break
        elif pcard.sum()>21:
            print("game over")
            print("score:",pscore)
            break
        
        det=input("get or pass: ")
        if det=="pass" or det=='p':
            break
        elif det=='get' or det=='g':
            pcard=np.append(pcard,cards[cardn])
            cardn+=1
            continue
        continue
    print(pcard)
    
    return cardn,pscore,pcard

def player1(cards,cardn,pcard):
    while len(pcard)<2:
        pcard=np.append(pcard,cards[cardn])
        cardn+=1
        
    return getcard(cards,cardn,pcard)

class player(object):
    cards=None
    cardn=0
    @classmethod
    def CardsandRound(cls):
        cls.cardn+=1
        
    def __init__(self,name,cards):
        self.name=name
        self.pcard=np.array([],dtype=int)
        self.score=0
        
    def get_first_cards(self,cards,cardn):
        #print(self.__class__.cardn)
        #self.CardsandRound()
        #print(self.__class__.cardn)
        #print(self.__class__.cards)
        
        while len(self.pcard)<2:
            self.pcard=np.append(self.pcard,self.__class__.cards[self.__class__.cardn])
            self.__class__.cardn+=1
    
    def startplay(self):
        self.__class__.cards,self.score,self.pcard=getcard(self.__class__.cards,self.__class__.cardn,self.pcard)

    def get_score(self):
        if 1 in self.pcard:
            if not sum(self.pcard)>11:
                self.score=sum(self.pcard)+10
        else:
            self.score=sum(self.pcard)
    
def draw_chart(bscores,pscores):
    for i in np.arange(2,22):
        plt.bar(i,len(np.where(bscores==i)[0]))
    plt.legend()
    plt.show()

def init_chart():
    plt.title("Gameble 21Point Predict",fontsize=20)
    plt.xlabel("First Cards Points",fontsize=14)
    plt.ylabel("Times",fontsize=14)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(2,22))
    plt.grid(linestyle=':')

def play(cards,cardn):
    
    pcard=np.array([],dtype=int)
    player.cards=cards
    player.cardn=0
    
    p1=player("Banker",cards)
    p2=player("OAO",cards)
    
    cardn=p1.get_first_cards(cards,cardn)
    p1.get_score()
    #print(p1.name,p1.pcard,p1.score,player.cardn)
    cardn=p2.get_first_cards(cards,cardn)
    p2.get_score()
    #print(p2.name,p2.pcard,p2.score,player.cardn)

    return p1.score,p2.score
    
    #p1.startplay()
    

    
    #cardn,p1score,p1card=player1(cards,cardn,pcard)
    
    #print("\n",cardn,p1score,p1card,sep="\n",end="\n\n\n")
    

def main():
    bankerscore=np.array([])
    playerscore=np.array([])
    init_chart()
    rounds=0
    while rounds<=times:
        cards,cardn=init_cards()
        bscore,pscore=play(cards,cardn)
        #playerscore=np.append(playerscore,pscore)
        bankerscore=np.append(bankerscore,bscore)
        rounds+=1
    #print(playerscore)
    print(bankerscore)
    draw_chart(bankerscore,playerscore)
    


main()


