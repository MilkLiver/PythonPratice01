import numpy as np


def init_cards():
    cards=np.arange(1,11)
    cards=np.append(cards,[10,10,10])
    cards=np.append(np.append(np.append(cards,cards),cards),cards)
    np.random.shuffle(cards)
    #print(cards)
    print(np.sum(cards==13))
    cardn=0
    return cards,cardn

def player1(cards,cardn,pcard):
    while len(pcard)<2:
        pcard=np.append(pcard,cards[cardn])
        cardn+=1
    
    while True:
        p1score=pcard.sum()
        if 1 in pcard:
            if pcard.sum()==11:
                print("BJ")
                print(pcard)
                break
            elif pcard.sum()+10<21:
                p1score=pcard.sum()+10
            else:
                p1score=pcard.sum()
        print("player1 score:",p1score)
        print(pcard)

                
        if pcard.sum()==21:
            print("BJ")
            print(pcard)
            break
        elif pcard.sum()>21:
            print("game over")
            print("score:",p1score)
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

def play(cards,cardn):
    
    p1card=np.array([],dtype=int)
    p2card=np.array([],dtype=int)
    
    player1(cards,cardn,p1card)
    

def main():
    cards,cardn=init_cards()
    play(cards,cardn)


while True:
    main()
    print("\n\n")
