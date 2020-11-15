from card_game import Card
from card_game import Deck
from card_game import Player
from card_game import Game
from card_game import Evaluator
import logging

logging.basicConfig(level=logging.DEBUG)


""" Card and Deck tests """

# ~ card1 = Card("hearts", "2")
# ~ card2 = Card("hearts", "K")
# ~ card3 = Card("clubs", "2")
# ~ card4 = Card("diamonds", "5")

# ~ assert card1._number == "2"
# ~ assert card2._number == "K"
# ~ assert card3._number == "2"
# ~ assert card4._number == "5"

# ~ assert card3._suit == "clubs"
# ~ assert card4._suit == "diamonds"

# ~ assert repr(card1) == "2 of hearts (0)"
# ~ assert repr(card2) == "K of hearts (0)"

# ~ assert card1._number != card2._number
# ~ assert card1._number == card3._number

# ~ assert card1._suit == card2._suit
# ~ assert card1._suit != card3._suit

# ~ card1.suit = "CLUBS"
# ~ assert card1._suit != "CLUBS"
# ~ card1.suit = "1"
# ~ assert card1._suit != "1"

# ~ card1.number = "44"
# ~ assert card1._number != "44"
# ~ card1.number = "hearts"
# ~ assert card1._number != "hearts"

# ~ card1.value = 532
# ~ assert card1._value != 532
# ~ card1.value = "hearts"
# ~ assert card1._value != "hearts"

# ~ deck1 = Deck()
# ~ deck2 = Deck()

# ~ deck1.shuffler()
# ~ player1 = Player("Bob")
# ~ my_cards1 = player1.drawCard(deck1).drawCard(deck1)
# ~ assert repr(deck1) == "Deck of 50 cards"
# ~ cardcount1 = len(player1._hand)
# ~ assert cardcount1 == 2
# ~ d1 = player1.discard()
# ~ cardcount1 = len(player1._hand)
# ~ assert cardcount1 == 1

# ~ assert deck1.cfinder(d1) == False



""" Evaluator tests """

""" 3 of a kind test"""
# hc1 = []
# c1 = Card("hearts", "2")
# c2 = Card("hearts", "K")
# c3 = Card("clubs", "2")
# c4 = Card("diamonds", "5")
# c5 = Card("spades", "7")
# c6 = Card("clubs", "9")
# c7 = Card("diamonds", "2")
# c8 = Card("diamonds", "A")
# hc1.append(c1)
# hc1.append(c2)
# hc1.append(c3)
# hc1.append(c4)
# hc1.append(c5)
# hc1.append(c6)
# hc1.append(c7)

# hc1.sort(key=lambda x: x._value)
# print("Cards: " + str(hc1))
# e1 = Evaluator(hc1)
# print(e1)

""" 4 of a kind test """
# hc2 = []
# c1 = Card("hearts", "2")
# c2 = Card("spades", "2")
# c3 = Card("clubs", "2")
# c4 = Card("diamonds", "10")
# c5 = Card("hearts", "A")
# c6 = Card("spades", "5")
# c7 = Card("clubs", "8")
# hc2.append(c1)
# hc2.append(c2)
# hc2.append(c3)
# hc2.append(c4)
# hc2.append(c5)
# hc2.append(c6)
# hc2.append(c7)

# hc2.sort(key=lambda x: x._value)
# print("Cards: " + str(hc2))

# e2 = Evaluator(hc2)
# print(e2)

""" Test - Royal straight flush """
hc3 = []
c1 = Card("hearts", "9")
c2 = Card("hearts", "K")
c3 = Card("hearts", "Q")
c4 = Card("hearts", "J")
c5 = Card("hearts", "10")
c6 = Card("spades", "5")
c7 = Card("clubs", "8")
hc3.append(c1)
hc3.append(c2)
hc3.append(c3)
hc3.append(c4)
hc3.append(c5)
hc3.append(c6)
hc3.append(c7)

hc3.sort(key=lambda x: x._value)
print("Cards: " + str(hc3))

e3 = Evaluator(hc3)
print(e3)

# g1 = Game("Poker")
