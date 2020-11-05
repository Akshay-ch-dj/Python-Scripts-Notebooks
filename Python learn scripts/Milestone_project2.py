import random     #random module needed to shuffle cards

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True    #Global variable

class Card:
    def __init__(self,suit, rank):  #meant to display what card from given suit and rank data ie the deck class creates shuffled list of 52 card classes
        self.suit = suit
        self.rank = rank  # Arguments in card class or properties of card
    def __str__(self):
        return (f"{self.rank} of {self.suit}") # To show or return the card as string

class Deck:
    # To create a deck of 52 shuffled card classes
    def __init__(self):
        self.deck = []         # start with an empty list
        for suit in suits:     #suits and ranks decleared global
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_Compos = ''  #Empty String
        for card in self.deck:
            deck_Compos += '\n' + card.__str__()
        return ("The Deck has: "+ deck_Compos)      # returns the deck as a string
    def shuffle(self):
        random.shuffle(self.deck)  # shuffles the deck
    def deal(self):
        d = self.deck[0]  #deal(return) one card out to player, the top one remains 51 cards
        self.deck.pop(0)
        return (d)

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]  # values is the global dictionary
        #To track Aces
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):    #SOmething like a clever code
        while self.value >21 and self.aces: #Truthfullness of an integer '0' is treated false other integer True
            self.value -= 10
            self.aces -= 1
    def __str__(self):
        hand_Compos = ''  #Empty String
        for card in self.cards:
            hand_Compos += '\n' + card.__str__()
        return (f"The Hand has: {hand_Compos}\nNet value:{self.value}\nAces:{self.aces}\")      # returns the deck as a string

class Chips:
        def __init__(self, total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
    def win_bet(self):
        self.total += bet
    def lose_bet(self):
        self.total -= bet

### FUNCTIONS NEEDED FOR GAMEPLAY

#To take betting amount add to chip class and to check its valid
def take_bet(chips):
    while True: #Classic try except block
        try:
            chips.bet = int(input("Enter a betting amount: ")) #Chips is the object name and chips is instance of that object
        except:
            print ("Amount Unspecified! Please Try Again..")
        else: #This else gonnna execute only if try executed with no error
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips, you got {}".format(chips.total))
            else:
                print("Amount Accepted")
                break

#To take a card from deck and add it to hand also chec
def hit(deck,hand): # Instances of deck and hand class
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    print("Done")  #for testing purpose only

#To take hit or stand command from player and do as it
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        arg = input("Enter 'H' for HIT and 'S' for STAND:\t")
        if arg[0].upper() == 'H':
            hit(test_deck,hand_test)
        elif arg[0].upper() == 'S':
            print ("Player stands, Dealer's turn")
            playing = False
        else:
            print ("Sorry, I didn't understand, please enter h or s only")
            continue  #Otherwise break gonna execute
        break
