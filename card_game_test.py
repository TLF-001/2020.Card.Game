from card_game import Card
from card_game import Deck
from card_game import Player
from card_game import Game
import logging

logging.basicConfig(level=logging.DEBUG)

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

g1 = Game("Poker")
