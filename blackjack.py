import random
player = True
dealer = True
#first we need to create the cards
deck = [
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    'J', 'Q', 'K', 'A',
    'J', 'Q', 'K', 'A',
    'J', 'Q', 'K', 'A',
    'J', 'Q', 'K', 'A'
        ]
player_hand = []
dealer_hand = []

#next we need to create a function that deals our cards
def shuffleCards(turn):
    #this is how we get a random card out of the deck
    card = random.choice(deck)
    #this will add it to the hand
    turn.append(card)
    #we want to take that card out the deck
    deck.remove(card)

# we then need to calculate the hands 
def total(turn):
    total = 0
    faceCards = ['J', 'Q', 'K',]
    for card in turn:
        if card in range (1, 11):
            total += card
        elif  card in faceCards:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total +=11
    return total 

# we now need to check for the winner 
def showDealerHand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]


# now we need to create the game loop
for game in range(2):
    shuffleCards(dealer_hand)
    shuffleCards(player_hand)

while player or dealer:
    print(f'Dealer had {showDealerHand()} and X')
    print(f'You have {player_hand} for a total of {total(player_hand)}')

    if player:
       chooseOption = input("1: Stand or 2: Hit")
    if total(dealer_hand) > 16:
         dealer = False
    else:
        shuffleCards(dealer_hand)
    if chooseOption == '1':
        player = False
    else:
        shuffleCards(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break


# now we need to determine the winner

if total(player_hand) == 21:
    print(f'You have {player_hand} with a score of {total(player_hand)}')
    print('You win! Blackjack!')
elif total(dealer_hand) == 21:
    print(f'The dealer {dealer_hand} has a score of {total(dealer_hand)}')
    print ('You lost. Deal won Blackjack!')
elif total(player_hand) > 21:
    print('You bust! Dealer Wins!')
elif total(dealer_hand) > 21:
    print('You won! Dealer bust!')
elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print('Dealer Wins!')
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print ('You win!')


