import numpy as np
import matplotlib.pyplot as plt
import collections as co

times=1000

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
        
    def get_first_cards(self,cardn):
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
    
def draw_chart(bscores):
    for i in np.arange(12,21):
        plt.bar(i,len(np.where(bscores==i)[0]))
    #plt.legend()
    plt.show()

def init_chart_Banker():
    plt.subplot(2,1,1)
    plt.title("Gameble 21Point Banker Predict",fontsize=20)
    plt.xlabel("First Cards Points",fontsize=14)
    plt.ylabel("Times",fontsize=14)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(2,22))
    plt.grid(linestyle=':')

def init_chart_My1():
    plt.subplot(2,2,3)
    plt.title("Gameble 21Point Player Predict",fontsize=20)
    plt.xlabel("First Cards Points",fontsize=14)
    plt.ylabel("Times",fontsize=14)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(2,22))
    plt.grid(linestyle=':')

def init_chart_My2():
    plt.subplot(2,2,4)
    plt.title("Gameble 21Point Player Predict",fontsize=20)
    plt.xlabel("First Cards Points",fontsize=14)
    plt.ylabel("Points Range",fontsize=14)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(2,22))
    plt.grid(linestyle=':')

def play(cards,cardn,playerNumber):
    
    pcard=np.array([],dtype=int)
    player.cards=cards
    player.cardn=0

    players={}

    for i in np.arange(1,playerNumber+1):
        if i ==1:
            playername="Banker"
        else:
            playername="Player"+str(i)
        players[i]=player(playername,cards)
        
    #p1=player("Banker",cards)
    #p2=player("Player",cards)

    for i in players:
        cardn=players[i].get_first_cards(cardn)
        players[i].get_score()
        
    #cardn=p1.get_first_cards(cards,cardn)
    #p1.get_score()
    #cardn=p2.get_first_cards(cards,cardn)
    #p2.get_score()
    
    #print(p2.name,p2.pcard,p2.score,player.cardn)

    return players
    
    #p1.startplay()
    

    
    #cardn,p1score,p1card=player1(cards,cardn,pcard)
    
    #print("\n",cardn,p1score,p1card,sep="\n",end="\n\n\n")
    

def main():
    playerNumber=0
    playerScoredict={}
    while True:
        try:
            playerNumber=int(input("Please Player Number: "))
        except:
            continue
        if playerNumber>7 or playerNumber<2:
            continue
        
        for i in np.arange(1,playerNumber+1):
            playerScoredict[i]=np.array([])
        break
    #print(playerScoredict)

    playerMe=np.random.randint(2,playerNumber+1)
    
    init_chart_Banker()
    rounds=0
    while rounds<=times:
        cards,cardn=init_cards()
        
        playersScore=play(cards,cardn,playerNumber)

        #print("Round"+str(rounds))
        for i in playerScoredict:
            playerScoredict[i]=np.append(playerScoredict[i],playersScore[i].score)
            #print(playersScore[i].name,playersScore[i].score)
        rounds+=1
    #print(playerScoredict)
    #print(player.cardn)
        
    #for i in playersScore:
    #    print(playersScore[i].name)
    playersScore[playerMe].name="Me"
        
    draw_chart(playerScoredict[1])
    
    init_chart_My1()
    init_chart_My2()
    

main()


