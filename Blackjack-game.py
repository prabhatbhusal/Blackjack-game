from art import logo
import random
decide=input("If you want to play the blackjack game type 'yes' or else type 'no': ")
name=input("Enter your name: ")
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def compare():
                if totaluser>totalcomp and totaluser<=21 :
                        print(f"{name} win")
                elif totaluser<totalcomp and totalcomp<=21 :
                        print("Dealer wins")
                elif totaluser==totalcomp:
                        print("draw")
                elif totaluser>21 and totalcomp<=21:
                        print("Dealer wins")
                elif totalcomp>21 and totaluser<=21:
                        print(f"{name} win")
                elif totalcomp==21:
                      print("!!!Blackjack!!!! Dealer wins")
                elif totaluser==21:
                      print(f"!!!Blacjack!!!!! {name} wins")

if decide=="yes":
    print(logo)
    print("!!!Welcome to Blackjack Game!!!")
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    player=random.sample(cards,2)
    comp=[]
    computer=random.choice(cards)
    comp.append(computer)
    print(f"Your cards: {player}")
    print(f"Computer's first card:{comp[0]}")
    totaluser=0
    totalcomp=0
    continuegame=True
    while  continuegame:
        user=input("Type 'y' for another card or type 'n' to pass :")
        if(user=="y"):
            player.append(random.choice(cards))
            comp.append(random.choice(cards))
            for i in range(0,len(player)):
                
                totaluser=totaluser+player[i]
                
            for i in range(0,len(comp)):
                totalcomp=totalcomp+comp[i]
            print(totaluser)
            print(totalcomp)
            print(comp)
            print(player)
            
            compare()
            if compare():
                  continuegame=False

        else:
            continuegame=False
            comp.append(random.choice(cards))
            print(f"Your final hand: {player} ")
            print(f"Computer hand:{comp}")
            compare()
            for i in range(0,len(player)): 
                totaluser=totaluser+player[i] 
            for i in range(0,len(comp)):
                totalcomp=totalcomp+comp[i]
            compare()     
else:
    print("Byee Byee")
