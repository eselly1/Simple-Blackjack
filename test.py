import random 
playerscore=0
housescore=0
def ace():
    print(' _____ ')
    print('|A ^  |')
    print('| / \ |')
    print('| \ / |')
    print('|  .  |')
    print('|____V|')
def two():
    print(' _____')
    print('|2    |')
    print('|  v  |')
    print('|     |')
    print('|  v  |')
    print('|____2|')
def three():
    print(' _____ ')
    print('|3    |')
    print('| v v |')
    print('|     |')
    print('|  v  |')
    print('|____3|')
def four():
    print(' _____')
    print('|4    |')
    print('| v v |')
    print('|     |')
    print('| v v |')
    print('|____4|')
def five():
    print(' _____')
    print('|5    |')
    print('| v v |')
    print('|  v  |')
    print('| v v |')
    print('|____5|')
def six():
    print(' _____')
    print('|6    |')
    print('| v v |')
    print('| v v |')
    print('| v v |')
    print('|____6|')
def seven():
    print(' _____')
    print('|7    |')
    print('| v v |')
    print('|v v v|')
    print('| v v |')
    print('|____7|')
def eight():
    print(' _____')
    print('|8    |')
    print('|v v v|')
    print('| v v |')
    print('|v v v|')
    print('|____8|')
def nine():
    print(' _____')
    print('|9    |')
    print('|v v v|')
    print('|v v v|')
    print('|v v v|')
    print('|____9|')
def jack():
    print(' _____ ')
    print('|J  ww|')
    print('|   {)|')
    print('|(v)% |')
    print('| v % |')
    print('|__%%J|')
def queen():
    print(' _____ ')
    print('|Q  ww|')
    print('|   {)|')
    print('|(v)% |')
    print('| v % |')
    print('|__%%Q|')
def king():
    print(' _____ ')
    print('|K  ww|')
    print('|   {)|')
    print('|(v)% |')
    print('| v % |')
    print('|__%%K|')
deck=['Ace','2','3','4','5','6','7','8','9','Jack','Queen','King']
def endgame(playerscore, housescore):
    if housescore==playerscore: print('draw!')
    elif housescore==21: print('you lose!')
    elif playerscore==21: print('you win!')
    elif playerscore>21 and housescore<21:print('you lose!')
    elif housescore>21 and playerscore<21: print('you win!')
    elif housescore>21 and playerscore> 21: print('draw!')
    elif playerscore<housescore<21: print('you lose!')
    elif housescore<playerscore<21: print('you win!')
    again()
def deal():
    card=deck[(random.randint(0,len(deck)-1))]
    print(f'The card is {card}.')
    if card == '2':
        two()
        return int(card)
    elif card=='3':
        three()
        return int(card)
    elif card=='4':
        four()
        return int(card)
    elif card=='5':
        five()
        return int(card)
    elif card=='6':
        six()
        return int(card)
    elif card=='7':
        seven()
        return int(card)
    elif card=='8':
        eight()
        return int(card)
    elif card=='9':
        nine()
        return int(card)
    elif card=="Ace":
        ace()
        prompt= int(input('Would you like the Ace to be worth 1 point or 11?\n'))
        while prompt!=1 and prompt!=11: prompt=int(input('Would you like the Ace to be worth 1 point or 11?\n'))
        return prompt
    elif card=='Jack':
        jack()
        return 10
    elif card=='Queen':
        queen()
        return 10
    else:
        king()
        return 10
def secdeal(playerscore, housescore,result):
    while result!='y' and result !='n': result=input('Would you like another card? Y or N:\n')
    if result=='y':
        playerscore+=deal()
        housescore+=deal()
        print(f'Your score is {playerscore}. The house\'s score is {housescore}.')
        return [playerscore, housescore]
    else:
        housescore+=deal()
        playerscore+=0
        print(f'Your score is {playerscore}. The house\'s score is {housescore}.')
        return [playerscore, housescore]
def again():
    again=input("would you like to play again? y/n\n".lower())
    while again=='y':
        playerscore=0
        housescore=0
        playerscore+=deal()
        playerscore+=deal()
        housescore+=deal()
        print(f'Your score is {playerscore}. The house\'s score is {housescore}.')
        result=input('Would you like another card? Y or N:\n')
        finalcards=secdeal(playerscore, housescore, result)
        playerscore=finalcards[0]
        housescore=finalcards[1]
        endgame(playerscore,housescore)
    else:
        print("thanks for playing")
playerscore+=deal()
playerscore+=deal()
housescore+=deal()
print(f'Your score is {playerscore}. The house\'s score is {housescore}.')
result=input('Would you like another card? Y or N:\n')
finalcards=secdeal(playerscore,housescore,result)
playerscore=finalcards[0]
housescore=finalcards[1]
endgame(playerscore, housescore)