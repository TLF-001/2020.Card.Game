import random
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

class Card:
    """
    The Card class represents a single playing card and is initialised by passing a suit and number.
    """
    def __init__(self, suit,  number):
        self._suit =   suit
        self._number = number
        card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
        self._value =  card_order_dict.get(number)
                            
    def __repr__(self):
        return self._number + " of " + self._suit + " (" + str(self._value) + ")"
    
    @property
    def suit(self):
        """ Gets or sets the suit of the Card """
        return self._suit
        
    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit.upper()
        else:
            logger.error("Tried to set an invalid suit (" + str(suit) + ") for " + repr(self) )
    
    @property
    def number(self):
        """ Gets or sets the number of the Card """
        return self._number
    
    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number
        else:
            logger.error("Tried to set an invalid number (" + str(number) + ") for " + repr(self))
    
    @property
    def value(self):
        """ Gets or sets the value of the Card """
        return self._value
    
    @value.setter
    def value(self, value):
        if value in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
            self._value = value
        else:
            logger.error("Tried to set an invalid value (" + str(value) + ") for " + repr(self))
            
class Deck:
    """
    The Deck represents a deck of playing cards in order.
    """
    def __init__(self):
        self._cards = []
        self.populate()
            
    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        #numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]
        logger.info("Deck created (" + repr(self) + ")")
    
    def __repr__(self):
        c = len(self._cards)
        return "Deck of " + str(c) + " cards"
    
    def shuffler(self):
        """ This method shuffles the deck"""
        logger.info("Deck shuffled")
        random.shuffle(self._cards)
    
    @property
    def cards(self):
        """ Gets or sets the cards of the Deck """
        return self._cards
        
    # unfisnished - unsure how to do this. Does it even make sense to make a setter for this?
    @cards.setter
    def cards(self, cards):
        if 1 == 1 :
            self._cards = cards
        else:
            # ~ print("That's not an allowed deck")
            logger.error("Tried to set an invalid deck (" + str(cards) + ") for " + repr(self))
    
    def draw(self):
        """ Draws a card from the Deck """
        return self._cards.pop()
    
    def cfinder(self, card):
        """ Looks if a Card exist in the Deck """
        f = False
        for c in self._cards:
            if repr(c) == repr(card):
                logger.info("Card found in deck (" + str(card) + ")")
                f = True
        if f == False:
            logger.info("Card not found in deck (" + str(card) + ")")
        return f
    
class Player:
    """
    The Player represents a player with a name that can hold cards in their hand.
    """
    def __init__(self, name):
        self._name =   name
        self.p_activity = True
        self._hand =   []
        self._chips =  0
        self._bet =    0
    
    def __repr__(self):
        return str(self._hand)
    
    def drawCard(self, deck):
        c = deck.draw()
        self._hand.append(c)
        logger.info("A player drew a card (" + str(c) + ")")
        return self
    
    # unfinished - Need to discard a specfic card instead of just the first one.
    def discard(self):
        c = self._hand.pop()
        logger.info("A player discarded a card (" + str(c) + ")")
        return c
        
    def show_hand(self):
        print("Your hand: " + str(self._hand))
        
class Game:
    """
    The Game represent the card game
    """
    def __init__(self, name):
        self.name = name
        self.g_state =    0
        self.g_pool =     0
        self.g_priority = 0
        self.g_round =    0
        self.g_players =  []
        self.g_board =    []
        self.g_discard =  []
        self.g_deck =     []
        self.main()
        
    def main(self):
        """ sets up the main menu """
        gp = input("Do you want to play (y/n)? ")
        
        if gp == "y":
            print("Starting game")
            self.setup()
        if gp == "n":
            print("Closing game")
            exit()
    
    def setup(self):
        """ sets up a game vs a computer player """
        self.g_state = 0
        self.g_round = 0
        del self.g_players[:]
        del self.g_board[:]
        
        p_name = input("What is your name?")
        self.g_players.append(Player(p_name))
        self.g_players.append(Player("Computer player"))
        
        for player in self.g_players:
            player._chips = 1000
            print(str(player._name) + "'s chips: " + str(player._chips))
            logger.info(player._name + " joined the game")
        
        self.g_state += 1
        print("Game state :" + str(self.g_state))
        self.g_round = 1
        print("Round 1")
        
        self.blinds()
        self.deal1()
    
    def new_round(self):
        """ sets up a new round """
        self.g_state = 0
        self.g_pool = 0
        del self.g_board[:]
        # ~ del self.g_deck[:]
        for player in self.g_players:
            del player._hand[:]
            player._bet = 0
        
        self.g_state += 1
        print("Game state :" + str(self.g_state))
        self.g_round += 1
        print("Round " + str(self.g_round))
        
        self.blinds()
        self.deal1()
        
    
    def blinds(self):
        """ adds blinds(forced bets) """
        c1 = self.g_players[0]._chips
        b1 = self.g_players[0]._bet
        c2 = self.g_players[1]._chips
        b2 = self.g_players[1]._bet
        
        if self.g_priority == 0:
            c1 -= 25
            b1 += 25
            c2 -= 50
            b2 += 50
        if self.g_priority == 1:
            c1 -= 50
            b1 += 50
            c2 -= 25
            b2 += 25
        
        # this section should be removed (or redone) at some point.
        self.g_players[0]._chips = c1
        self.g_players[0]._bet = b1
        self.g_players[1]._chips = c2
        self.g_players[1]._bet = b2
        
        self.g_pool = 75
        
        print(str(self.g_players[0]._name) + "'s bet: " + str(self.g_players[0]._bet))
        print(str(self.g_players[0]._name) + "'s chips: " + str(self.g_players[0]._chips))
        print(str(self.g_players[1]._name) + "'s bet: " + str(self.g_players[1]._bet))
        print(str(self.g_players[1]._name) + "'s chips: " + str(self.g_players[1]._chips))
        
    def deal1(self):
        """ create a deck, shuffle it, and deal 2 cards to each player """
        self.g_deck =  Deck()
        self.g_deck.shuffler()
        
        for player in self.g_players:
            player.drawCard(self.g_deck)
            player.drawCard(self.g_deck)
        
        self.g_players[self.g_priority].show_hand()
        
        self.betting1()
    
    def deal2(self):
        """ Flop - three community cards are flipped face up on the table """
        self.g_board.append(self.g_deck._cards.pop())
        self.g_board.append(self.g_deck._cards.pop())
        self.g_board.append(self.g_deck._cards.pop())
        self.show_table()
        
        self.betting1()
        
    def deal3(self):
        """ Turn - fourth community card is flipped face up on the table """
        self.g_board.append(self.g_deck._cards.pop())
        self.show_table()
        
        self.betting1()
    
    def deal4(self):
        """ River - fifth community card is flipped face up on the table """
        self.g_board.append(self.g_deck._cards.pop())
        self.show_table()
        
        self.betting1()
        
    def betting1(self):
        """ player betting round """
        player = self.g_players[self.g_priority]
        self.show_high_bet()
        self.show_bet(player)
        
        gp = input("You can now fold (f), call/check (c) or raise (r)")
        if gp == "f":
            self.fold(player)
            # this should be changed/redone at some point
            exit()
        if gp == "c":
            self.call(player)
        if gp == "r":
            hb = self.high_bet()
            cb = player._bet
            pc = hb - cb
            print("You call " + str(pc))
            bet = int(input("how much do you want to bet?"))
            self.bet(player, bet)
        
        if self.g_priority == 0:
            self.g_priority += 1
            self.cbetting1()
    
    def cbetting1(self):
        """ first computer betting round """
        # Not finished. May move some of this code to a separate method
        logger.info("Computer player betted, called or raised")
        self.g_priority -= 1
        
        if self.g_state == 1:
            self.g_state += 1
            print("Game state :" + str(self.g_state))
            self.deal2()
        if self.g_state == 2:
            self.g_state += 1
            print("Game state :" + str(self.g_state))
            self.deal3()
        if self.g_state == 3:
            self.g_state += 1
            print("Game state :" + str(self.g_state))
            self.deal4()
        if self.g_state == 4:
            self.g_state += 1
            print("Game state :" + str(self.g_state))
            print("Round over")
            self.new_round()
        
    def show_table(self):
        print("Cards on table: " + str(self.g_board))
    
    def show_pool(self):
        print("Current pool: " + str(self.g_pool))
    
    def show_high_bet(self):
        print("Highest bet: " + str(self.high_bet()))
    
    def show_bet(self, player):
        print("Your current bet: " + str(player._bet))
    
    def high_bet(self):
        b = 0
        for player in self.g_players:
            if b < player._bet:
                b = player._bet
        return b
    
    def call(self, player):
        hb = self.high_bet()
        cb = player._bet
        pc = hb - cb
        
        if cb < hb:
            player._chips -= pc
            player._bet   += pc
            self.g_pool   += pc
            
        logger.info("Player called/checked")
    
    def fold(self, player):
        player._bet = 0
        player.p_activity = False
        logger.info("Player folded")
    
    def bet(self, player, bet):
        hb = self.high_bet()
        cb = player._bet
        pc = hb - cb
        
        if cb < hb:
            player._chips -= pc
            player._bet   += pc
            self.g_pool   += pc
        
        player._chips -= bet
        player._bet   += bet
        self.g_pool   += bet
        
        logger.info("Player raised")
        
    def card_value_finder(self, value):
        p_hand = self.g_board + self.g_players[0]._hand
        for card in p_hand:
            if card._value == value:
                return True
        return False



    # def gameloop(self):
    #     self.g_state = 3
    #     active = True


class Evaluator:
    """
    The Evaluator class is used to evaluate cards and return the best possible hand.
    """
    def __init__(self, cards):
        self.cards = cards
        self.hand_value = 0
        self.find_hand()
        
    def __repr__(self):
        return str(self.hand_value)
    
    def find_hand(self):
        if self.r_flush():
            self.hand_value = 10
            # print("10")
        elif self.s_flush():
            self.hand_value = 9
            # print("9")
        elif self.kind4():
            self.hand_value = 8
            # print("8")
        elif self.full_house():
            self.hand_value = 7
            # print("7")
        elif self.flush():
            self.hand_value = 6
            # print("6")
        elif self.straight():
            self.hand_value = 5
            # print("5")
        elif self.kind3():
            self.hand_value = 4
            # print("4")
        elif self.two_pair():
            self.hand_value = 3
            # print("3")
        elif self.pair():
            self.hand_value = 2
            # print("2")
        elif self.high_card():
            self.hand_value = 1
            # print("1")

    def r_flush(self):
        c1 = self.cards[:]
        f1 = False
        h_suit = 0
        c_suit = 0
        d_suit = 0
        s_suit = 0
                
        for card in c1:
            if card._suit == "hearts":
                h_suit += 1
            if card._suit == "clubs":
                c_suit += 1
            if card._suit == "diamonds":
                d_suit += 1
            if card._suit == "spades":
                s_suit += 1
        
        if h_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "hearts":
                    del card
        elif c_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "clubs":
                    del card
        elif d_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "diamonds":
                    del card
        elif s_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "spades":
                    del card
        
        if f1:
            for card in c1:
                if card._value < 10:
                    del card
            c1.sort(key=lambda x: x._value, reverse=False)
            v1 = c1[0]._value + 1
            s1 = 1
            v2 = 2
            s2 = 1

            for card in c1:
                if card._value == v1:
                    s1 += 1
                    v1 = card._value + 1
                else:
                    v1 = card._value + 1
        
            if s1 > 4:
                return True
            elif s1 == 4:
                if c1[-1]._value == 14:
                    for card in c1:
                        if card._value == v2:
                            s2 += 1
                            v2 = card._value + 1
                    if s2 == 5:
                        return True
                return False
            else:
                return False
            
        else:
            return False
        
    def s_flush(self):
        c1 = self.cards[:]
        f1 = False
        h_suit = 0
        c_suit = 0
        d_suit = 0
        s_suit = 0
                
        for card in c1:
            if card._suit == "hearts":
                h_suit += 1
            if card._suit == "clubs":
                c_suit += 1
            if card._suit == "diamonds":
                d_suit += 1
            if card._suit == "spades":
                s_suit += 1
        
        if h_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "hearts":
                    del card
        elif c_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "clubs":
                    del card
        elif d_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "diamonds":
                    del card
        elif s_suit > 4:
            f1 = True
            for card in c1:
                if card._suit != "spades":
                    del card
        
        if f1:
            c1.sort(key=lambda x: x._value, reverse=False)
            v1 = c1[0]._value + 1
            s1 = 1
            v2 = 2
            s2 = 1

            for card in c1:
                if card._value == v1:
                    s1 += 1
                    v1 = card._value + 1
                else:
                    v1 = card._value + 1
        
            if s1 > 4:
                return True
            elif s1 == 4:
                if c1[-1]._value == 14:
                    for card in c1:
                        if card._value == v2:
                            s2 += 1
                            v2 = card._value + 1
                    if s2 == 5:
                        return True
                return False
            else:
                return False
            
        else:
            return False

    def kind4(self):
        c1 = self.cards[:]
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = c1[0]._value
        k1 = 0

        for card in c1:
            if card._value == v1:
                k1 += 1
                if k1 > 3:
                    return True
            else:
                v1 = card._value
                k1 = 1
        return False

    
    def full_house(self):
        c1 = self.cards[:]
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = c1[0]._value
        k1 = 0
        k2 = 0
        k3 = 0

        for card in c1:
            if card._value == v1:
                k1 += 1
                if k1 == 2:
                    k2 += 1
                if k1 == 3:
                    k3 += 1
                if k3 == 1:
                    if k2 > 1:
                        return True
            else:
                v1 = card._value
                k1 = 1
        return False

    def flush(self):
        c1 = self.cards[:]
        h_suit = 0
        c_suit = 0
        d_suit = 0
        s_suit = 0
        
        for card in c1:
            if card._suit == "hearts":
                h_suit += 1
            if card._suit == "clubs":
                c_suit += 1
            if card._suit == "diamonds":
                d_suit += 1
            if card._suit == "spades":
                s_suit += 1
        
        if h_suit > 4:
            return True
        elif c_suit > 4:
            return True
        elif d_suit > 4:
            return True
        elif s_suit > 4:
            return True
        else:
            return False

        
    def straight(self):
        c1 = self.cards[:]
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = c1[0]._value + 1
        s1 = 1
        v2 = 2
        s2 = 1

        for card in c1:
            if card._value == v1:
                s1 += 1
                v1 = card._value + 1
            else:
                v1 = card._value + 1
        
        if s1 > 4:
            return True
        elif s1 == 4:
            if c1[-1]._value == 14:
                for card in c1:
                    if card._value == v2:
                        s2 += 1
                        v2 = card._value + 1
                if s2 == 5:
                    return True
            return False
        else:
            return False

    def kind3(self):
        c1 = self.cards[:]
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = c1[0]._value
        k1 = 0
        
        for card in c1:
            if card._value == v1:
                k1 += 1
                if k1 > 2:
                    return True
            else:
                v1 = card._value
                k1 = 1
        return False

    def two_pair(self):
        c1 = self.cards[:]
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = c1[0]._value
        k1 = 0
        k2 = 0

        for card in c1:
            if card._value == v1:
                k1 += 1
                if k1 == 2:
                    k2 += 1
                if k2 == 2:
                    return True
            else:
                v1 = card._value
                k1 = 1
        return False

    def pair(self):
        c1 = self.cards[:]
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = c1[0]._value
        k1 = 0

        for card in c1:
            if card._value == v1:
                k1 += 1
                if k1 > 1:
                    return True
            else:
                v1 = card._value
                k1 = 1
        return False
        
    def high_card(self):
        return True

