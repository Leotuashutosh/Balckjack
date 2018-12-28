import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
class Card:
    
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        suit.value= value
        pass
    
    def __str__(self):
        for suit1 in suits:
            for rank1 in ranks:
                if self.suit==suit1 and self.rank==rank1:
                    print(f" {rank1} of {suit1}")
                    break
        pass
                    
                          
                
            
        
    pass
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(f"{rank} of {suit}")
        pass
    
    def shuffle(self):
        random.shuffle(self.deck)
        
        pass
    
    def __str__(self):
        for deck in self.deck:
            return f"{deck} is here"
        pass
    def __len__(self):
        return len(self.deck)
        pass
    

    
        
    def deal(self):
        self.k = self.deck[0]
        self.deck.pop(0)
        return self.k
        pass
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        word = card.split()[0]
        self.value = self.value + values[word]
        pass
    
    def adjust_for_ace(self):
        self.value = self.value-10
        
        pass
    def __str__(self):
        return f" This person has {self.cards}"
        pass
class Chips:
    
    def __init__(self,bet = 0,total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = bet
        
    def win_bet(self):
        self.total = self.total + self.bet
        pass
    
    def lose_bet(self):
        self.total = self.total-self.bet
        pass
    
    def __str__(self):
        return f" You have {self.total} chips"
        pass
def take_bet(avail_chips):
    while True:
        try:
            bet = int(input("Enter your bet"))
        except:
            print("That isnt an integer you stupid fudge")
            continue
        else:
            if bet>avail_chips:
                print("Greater than your chips you stupid fudge")
                continue
            else:
                return bet
    
    pass
def hit(deck,hand):
    hand.add_card(deck.deal())
    if hand.value>21 and "Ace" in hand.cards :
        hand.adjust_for_ace()
    pass
def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    while playing:
        n= int(input("Enter 1 to hit and 2 to stand"))
        if n==1 and hand.value<21:
            hit(deck,hand)
        else:
            playing = False
    
    pass
def show_some(player,dealer):
    print("The player cards are as follows")
    print(player)
    print(f"The Dealer cards with one card hiddden are {dealer.cards[1:]} ")
    pass
    
def show_all(player,dealer):
	print(f"The Player cards are {player}")
	print(f"The dealer cards are {dealer}")
	pass
def player_busts(player_chips):
    print("The Dealer wins")
    player_chips.lose_bet()
    pass

def player_wins(player_chips):
    print("The player wins")
    player_chips.win_bet()
    pass

def dealer_busts(player_chips):
    print("The player wins")
    player_chips.win_bet()
    pass
    
def dealer_wins(player_chips):
    print("The dealer wins")
    player_chips.lose_bet()
    pass
    
def push():
    pass
i=0
while True:
    print("Welcome to Blackjack! You start with 100 coins. Place your bets and enjoy")
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    
    if i==0:
        
        player_chips = Chips(0,100)
    
    player_chips.bet = take_bet(player_chips.total)

    
        
    # Set up the Player's chips
    
    
    # Prompt the Player for their bet

    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    playing = True
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value>21:
            player_busts(player_chips)

        pass

    if player.value<=21:
        while dealer.value<= 17:
            dealer.add_card(deck.deal())
        show_all(player,dealer)
        if player.value>dealer.value or player.value == 21:
            player_wins(player_chips)
        elif dealer.value>21:
            dealer_busts(player_chips)
        else:
            dealer_wins(player_chips)
    
    print(player_chips)
    i+=1
    y = input("Wanna try your luck again ?Press Y for yes and literally anything else for no ")
    if y.lower()=='y':
        print("Alright Alright Alright! Burn the dealer")
    else:
        break
