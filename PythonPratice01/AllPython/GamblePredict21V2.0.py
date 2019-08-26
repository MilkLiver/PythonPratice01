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
            
    def get_score2(self):
        return sum(self.pcard)
    
def draw_chart(scores):
    for i in np.arange(12,21):
        plt.bar(i,len(np.where(scores==i)[0]))
    #plt.legend()

def draw_chart2(scores):
    for i in np.arange(12,21):
        cut=int(len(scores[i])/3)
        negative=np.sort(scores[i])[1:cut+1]
        positive=np.sort(scores[i])[-1:-cut-1:-1]
        plt.bar(i,np.mean(positive)-np.mean(negative),bottom=np.mean(negative),color="orange")
        plt.plot(i,np.mean(scores[i]),'o',color="red",markersize=2)
        plt.text(i,np.mean(scores[i])+0.3, r'%d'%(np.mean(scores[i])),fontdict={'size': 8, 'color': 'black'})
        #print(np.mean(negative))
        #print(np.around(np.mean(negative),0))
        plt.text(i,np.mean(positive), r'%d'%(np.around(np.mean(positive),0)),fontdict={'size': 8, 'color': 'r'})
        plt.text(i,np.mean(negative), r'%d'%(np.around(np.mean(negative),0)),fontdict={'size': 8, 'color': 'g'})
    
def draw_chart3(scores):
    col_labels = ['Broken','col2','col3']
    row_labels = list(np.arange(12,21))
    table_vals = []
    for i in np.arange(12,21):
        broken_Chance=np.around((len(np.where(scores[i]>21)[0])/len(scores[i]))*100,1)
        table_vals.append([str(broken_Chance)+"%",2,3])
        
    plt.table(cellText=table_vals,cellLoc='center', colWidths=[0.31]*3,
              rowLabels=row_labels, colLabels=col_labels,
              loc='best')

    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

def draw_chart4(scores,fscores):
    #print(fscores)
    for i in np.arange(1,11):
        cut=int(len(scores[i])/3)
        negative=np.sort(scores[i])[1:cut+1]
        positive=np.sort(scores[i])[-1:-cut-1:-1]
        plt.bar(i,np.mean(positive)-np.mean(negative),bottom=np.mean(negative),alpha=0.7,color="orange")
        plt.plot(i,np.mean(scores[i]),'o',color="red",markersize=2)
        plt.text(i,np.mean(scores[i])+0.3, r'%d'%(np.mean(scores[i])),fontdict={'size': 8, 'color': 'black'})
        plt.text(i,np.mean(positive), r'%d'%(np.around(np.mean(positive),0)),fontdict={'size': 8, 'color': 'r'})
        plt.text(i,np.mean(negative), r'%d'%(np.around(np.mean(negative),0)),fontdict={'size': 8, 'color': 'g'})
    for i in np.arange(1,11):
        cut=int(len(fscores[i])/3)
        negative=np.sort(fscores[i])[1:cut+1]
        positive=np.sort(fscores[i])[-1:-cut-1:-1]
        plt.bar(i,np.mean(positive)-np.mean(negative),bottom=np.mean(negative),edgecolor="yellow",alpha=0.5,color='yellow',width=0.3)
        plt.plot(i,np.mean(fscores[i]),'o',color="blue",markersize=2)
        plt.text(i+0.2,np.mean(fscores[i])+0.3, r'%d'%(np.mean(fscores[i])),fontdict={'size': 8, 'color': 'black'})
        plt.text(i+0.2,np.mean(positive), r'%d'%(np.around(np.mean(positive),0)),fontdict={'size': 8, 'color': 'r'})
        plt.text(i+0.2,np.mean(negative), r'%d'%(np.around(np.mean(negative),0)),fontdict={'size': 8, 'color': 'g'})
    #plt.legend()

def init_chart_Banker():
    plt.subplot(2,1,1)
    plt.title("Gameble 21Point Banker Predict",fontsize=14)
    plt.xlabel("First Cards Points",fontsize=12)
    plt.ylabel("Times",fontsize=12)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(2,22))
    plt.grid(linestyle=':')

def init_chart_Banker2():
    plt.subplot(2,1,1)
    plt.title("Gameble 21Point Banker Predict",fontsize=14)
    plt.xlabel("Show Card Points",fontsize=12)
    plt.ylabel("Average",fontsize=12)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(1,22))
    plt.yticks(np.arange(4,30))
    plt.grid(linestyle=':')

def init_chart_My1():
    plt.subplot(2,3,4)
    plt.title("Gameble 21Point Player Predict",fontsize=14)
    plt.xlabel("First Cards Points",fontsize=12)
    plt.ylabel("Times",fontsize=12)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(2,22))
    plt.grid(linestyle=':')

def init_chart_My2():
    plt.subplot(2,3,5)
    plt.title("Gameble 21Point Follow Point Range",fontsize=14)
    plt.xlabel("First Cards Points",fontsize=12)
    plt.ylabel("Points Range",fontsize=12)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    plt.xticks(np.arange(2,22))
    plt.yticks(np.arange(1,31))

    #plt.xlim(2,22)
    #plt.ylim(1,31)
    
    plt.grid(linestyle=':')

def init_chart_My_Chance():
    plt.subplot(2,3,6)
    plt.title("Gameble Follow Status Chance",fontsize=14)
    plt.xlabel("First Cards Points",fontsize=12)
    plt.ylabel("Points Range",fontsize=12)
    plt.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    #plt.xticks(np.arange(2,22))
    #plt.yticks(np.arange(1,31))

    #plt.xlim(2,22)
    #plt.ylim(1,31)
    
    #plt.grid(linestyle=':')

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
    playerFollow1Scoredict={}
    bankFollow1Scoredict={}
    bankShowScoredict={}
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
    for i in np.arange(12,21):
            playerFollow1Scoredict[i]=np.array([])

    for i in np.arange(1,11):
            bankShowScoredict[i]=np.array([])
            bankFollow1Scoredict[i]=np.array([])
    
    rounds=0
    while rounds<=times:
        cards,cardn=init_cards()
        
        playersScore=play(cards,cardn,playerNumber)

        #print("Round"+str(rounds))
        for i in playerScoredict:
            if i==playerMe and playersScore[i].score>11 and playersScore[i].score<21:
                playerFollow1Scoredict[playersScore[i].score]=np.append(playerFollow1Scoredict[playersScore[i].score],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+1])
                playerFollow1Scoredict[playersScore[i].score]=np.append(playerFollow1Scoredict[playersScore[i].score],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+2])
                playerFollow1Scoredict[playersScore[i].score]=np.append(playerFollow1Scoredict[playersScore[i].score],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+3])
            if i==1:
                #print(playersScore[i].pcard[0])
                bankShowScoredict[playersScore[i].pcard[0]]=np.append(bankShowScoredict[playersScore[i].pcard[0]],playersScore[i].score)
                if playersScore[i].score>11 and playersScore[i].score<21:
                    if 1 in playersScore[i].pcard:
                        scor1=playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+1]
                        scor2=playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+2]
                        scor3=playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+3]
                        if scor1>21:
                            bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].get_score2()+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+1])
                        else:
                            bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+1])
                        if scor2>21:
                            bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].get_score2()+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+2])
                        else:
                            bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+2])
                        if scor3>21:
                            bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].get_score2()+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+3])
                        else:
                            bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+3])
                    else:
                        #print(playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+1])
                        bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+1])
                        bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+2])
                        bankFollow1Scoredict[playersScore[i].pcard[0]]=np.append(bankFollow1Scoredict[playersScore[i].pcard[0]],playersScore[i].score+playersScore[i].__class__.cards[playersScore[i].__class__.cardn+3])
                
                
            playerScoredict[i]=np.append(playerScoredict[i],playersScore[i].score)
                
        rounds+=1
    #print(playerScoredict)
    #print(player.cardn)
        
    #for i in playersScore:
    #    print(playersScore[i].name)
    playersScore[playerMe].name="Me"

    init_chart_Banker()
    draw_chart(playerScoredict[1])
    
    init_chart_My1()
    draw_chart(playerScoredict[playerMe])
    
    init_chart_My2()
    #print(playerFollow1Scoredict)
    draw_chart2(playerFollow1Scoredict)

    init_chart_My_Chance()
    draw_chart3(playerFollow1Scoredict)

    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.95, wspace=0.3, hspace=0.3)
    plt.show()


    init_chart_Banker2()
    draw_chart4(bankShowScoredict,bankFollow1Scoredict)

    init_chart_My2()
    draw_chart2(playerFollow1Scoredict)

    init_chart_My_Chance()
    draw_chart3(playerFollow1Scoredict)
    
    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.95, wspace=0.3, hspace=0.3)
    plt.show()
    

main()


