import random

# First we want to create/define a Card class, this will be our deck
# random has been imported as a way to ensure the deck is being randomized
# everytime
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # this function is in order to string the suit and value 
    # returning a statement 
    def __repr__(self):
        return "'' of ''".join((self.value, self.suit))


# Second we need to be able to have a deck


# Third the deck needs to be dealt


# Fourth we need to calculate the totals



# Lastly check for winners   