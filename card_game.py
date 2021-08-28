import random
import logging
from guizero import App, Text, TextBox, PushButton, Picture, Combo, info
 
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
 
class Card:
    """
    The Card class represents a single playing card and is initialised by passing a suit and number.
    """
    def __init__(self, suit,  number):
        self._suit =   suit
        self._number = number
        card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J":11, "Q":12, "K":13, "A":14}
        self._value =  card_order_dict.get(number)
        image_dict = {"hearts":"❤", "clubs":"♣", "diamonds":"♦", "spades":"♠"}
        self._image = image_dict.get(suit)
 
    def __repr__(self):
        # return self._number + " of " + self._suit + " (" + str(self._value) + ")"
        return "[" + self._number + self._image + "]"
 
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
        return str(self._name)
 
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
        self.g_state    = 0
        self.g_pool     = 0
        self.g_priority = 0
        self.g_round    = 0
        self.g_players  = []
        self.g_board    = []
        self.g_discard  = []
        self.g_deck     = []
        # self.p_slot1    = []
        # self.p_slot2    = []
        # self.p_slot3    = []
        # self.p_slot4    = []
        # self.p_slot5    = []
        # self.p_slot6    = []
        # self.app = App(title="Poker Game 2021", width=600, height=400, layout="grid")
        self.g_play_state = "Starting Game"
        self.main()
 
    def game_window(self):
        """ This makes the game window """
 
        player = self.g_players[self.g_priority]
 
        def gui_setup():
            game_state.value = "Gui Loaded"
            self.g_play_state = "Gui Setup Finished"
 
        def update_player():
            player = self.g_players[self.g_priority]
 
        def quit_game():
            exit()
 
        def play_game():
            play_game.disable()
            update_gui()
            gameloop()
 
        def update_game():
            logger.info("Updating Game") #remove later
 
        def get_player_names():
            return self.g_players
 
        def get_player1_info():
            info("Player 1 Info", "Info Stuff...")
 
        def get_player2_info():
            info("Player 2 Info", "Info Stuff...")
 
        def update_game_state():
            update_gui()
            show_game_info()
            update_game_info()
 
        def end_round():
            player = self.g_players[self.g_priority]
            bhp = self.find_winner(self.g_players)
            pc = len(bhp)
            # ~ bhv = self.best_hand(player)
 
            game_info_18.visible = True
 
            if pc == 1:
                game_result1.value = "[" + bhp[0]._name + "] won the pot (" + str(self.g_pool) + ")"
                bhp[0]._chips = bhp[0]._chips + self.g_pool
                self.g_pool = 0
                # self.player_cleanup(bhp[0])
 
            if len(bhp) == 2:
                game_result1.value = "[" + bhp[0]._name + "] splits the pot (" + str(self.g_pool) + ") with [" + bhp[1]._name + "]"
                bhp[0]._chips = bhp[0]._chips + self.g_pool/2
                bhp[1]._chips = bhp[1]._chips + self.g_pool/2
                self.g_pool = 0
 
            show_winning_hand(self.best_hand(player))
 
            for player in self.g_players:
                self.player_cleanup(player)
 
        def show_winning_hand(best_hand_value):
            if best_hand_value == 0:
                logger.error("Error: No winning hand was found.")
            if 1 <= best_hand_value < 2:
                game_result2.value = "Winning hand: High card"
            if 2 <= best_hand_value < 3:
                game_result2.value = "Winning hand: Pair"
            if 3 <= best_hand_value < 4:
                game_result2.value = "Winning hand: Two pair"
            if 4 <= best_hand_value < 5:
                game_result2.value = "Winning hand: Three of a kind"
            if 5 <= best_hand_value < 6:
                game_result2.value = "Winning hand: Straight"
            if 6 <= best_hand_value < 7:
                game_result2.value = "Winning hand: Flush"
            if 7 <= best_hand_value < 8:
                game_result2.value = "Winning hand: Full House"
            if 8 <= best_hand_value < 9:
                game_result2.value = "Winning hand: Four of a kind"
            if 9 <= best_hand_value < 10:
                game_result2.value = "Winning hand: Straight Flush"
            if 10 <= best_hand_value:
                game_result2.value = "Winning hand: Royal Straight Flush"
 
        def disable_g_buttons():
            call_bet.disable()
            raise_bet.disable()
            fold_bet.disable()
 
        def enable_g_buttons():
            call_bet.enable()
            raise_bet.enable()
            fold_bet.enable()
 
        def raise_bet():
            if int(input_bet.value) < 1:
                return
            raise_bet.disable()
            max_bet = player._chips
            if int(input_bet.value) > max_bet:
                self.bet(player, int(max_bet))
            else:
                self.bet(player, int(input_bet.value))
            input_bet.clear()
            game_signal == 1
            # ~ print("Raise")
 
            # ~ update_game_info()
            if 1 <= self.g_state <= 3:
                self.g_state += 1
                gameloop()
            elif self.g_state == 4:
                self.g_state += 1
                gameloop()
                disable_g_buttons()
                end_round()
                new_game.enable()
 
            if self.g_priority == 0:
                self.g_priority += 1
                self.computer_turn()
 
        def call_bet():
            call_bet.disable()
            self.call(player)
            game_signal == 1
 
            if 1 <= self.g_state <= 3:
                self.g_state += 1
                gameloop()
            elif self.g_state == 4:
                self.g_state += 1
                gameloop()
                disable_g_buttons()
                end_round()
                new_game.enable()
 
            if self.g_priority == 0:
                self.g_priority += 1
                self.computer_turn()
 
        def fold_bet():
            fold_bet.disable()
            # ~ print("Fold")
            self.fold(player)
            new_game.enable()
 
        def new_game():
            new_game.disable()
            purge_game_results()
            self.g_state == 1
            game_info_18.visible = False
            self.new_round()
            update_gui()
            gameloop()
 
        def purge_game_results():
            game_result1.value = ""
            game_result2.value = ""
 
        def update_gui():
            raise_bet.visible   = True
            call_bet.visible    = True
            fold_bet.visible    = True
            raise_bet.enable()
            call_bet.enable()
            fold_bet.enable()
 
        def show_g_buttons():
            raise_bet.visible   = True
            call_bet.visible    = True
            fold_bet.visible    = True
 
        def hide_g_buttons():
            raise_bet.visible   = False
            call_bet.visible    = False
            fold_bet.visible    = False
 
        def show_game_result():
            game_result1.visible = True
            game_result2.visible = True
 
        def hide_game_result():
            game_result1.visible = False
            game_result2.visible = False
 
        def show_h_cards():
            game_info_18.visible = True
 
        def hide_h_cards():
            game_info_18.visible = False
 
        def display_game_area():
            print("Displaying game area")
 
        def show_game_info():
            game_info_1.visible  = True
            game_info_2.visible  = True
            game_info_3.visible  = True
            game_info_4.visible  = True
            game_info_5.visible  = True
            game_info_6.visible  = True
            game_info_7.visible  = True
            game_info_8.visible  = True
            game_info_9.visible  = True
            game_info_10.visible = True
            game_info_11.visible = True
            game_info_12.visible = True
            game_info_13.visible = True
            game_info_14.visible = True
            game_info_15.visible = True
            game_info_16.visible = True
            game_info_17.visible = True
            # ~ game_info_18.visible = True
            game_info_19.visible = True
            game_info_20.visible = True
 
        def hide_game_info():
            game_info_1.visible  = False
            game_info_2.visible  = False
            game_info_3.visible  = False
            game_info_4.visible  = False
            game_info_5.visible  = False
            game_info_6.visible  = False
            game_info_7.visible  = False
            game_info_8.visible  = False
            game_info_9.visible  = False
            game_info_10.visible = False
            game_info_11.visible = False
            game_info_12.visible = False
            game_info_13.visible = False
            game_info_14.visible = False
            game_info_15.visible = False
            game_info_16.visible = False
            game_info_17.visible = False
            # ~ game_info_18.visible = False
            game_info_19.visible = False
            game_info_20.visible = False
 
        def update_game_info():
            game_info_5.value   = str(self.g_players[0]._chips)
            game_info_10.value  = str(self.g_players[1]._chips)
            game_info_12.value  = str(self.high_bet())
            game_info_14.value  = str(self.g_pool)
            game_info_16.value  = str(self.g_players[0]._hand)
            game_info_18.value  = str(self.g_players[1]._hand)
            game_info_20.value  = str(self.g_board)
 
        def gameloop():
            # ~ print("Game state: "+ str(self.g_state))
            if self.g_state == 1:
                game_state.value = "Starting Round 1"
                self.blinds()
                game_state.value = "Placing Blinds"
                self.deal1()
                game_state.value = "Dealing Hand Cards"
                if player._chips < 25:
                    raise_bet.disable()
                else:
                    raise_bet.enable()
            if self.g_state == 2:
                game_state.value = "The flop (3 Cards)"
                logger.info("Game state :" + str(self.g_state))
                self.deal2()
                if player._chips < 1:
                    raise_bet.disable()
                else:
                    raise_bet.enable()
            if self.g_state == 3:
                game_state.value = "The Turn (1 card)"
                logger.info("Game state :" + str(self.g_state))
                self.deal3()
                if player._chips < 1:
                    raise_bet.disable()
                else:
                    raise_bet.enable()
            if self.g_state == 4:
                game_state.value = "The River (1 card)"
                logger.info("Game state :" + str(self.g_state))
                self.deal4()
                if player._chips < 1:
                    raise_bet.disable()
                else:
                    raise_bet.enable()
            if self.g_state == 5:
                game_state.value = "End of Round"
                logger.info("Game state :" + str(self.g_state))
                logger.info("Round over")
 
            update_game_state()
            update_game_info()
 
        # ~ def player_turn():
            # ~ """ player betting round """
            # ~ player = self.g_players[self.g_priority]
            # ~ update_game_state()
 
            # ~ print("Player Turn Test:" + str(self.g_state))
 
 
        app = App(title="Poker Game 2021", width=1200, height=800, layout="grid")
 
        game_options        = Text(app, text="Game Options", grid=[1,1], size=14, font="Times New Roman", color="black", align="left")
        play_game           = PushButton(app, command=play_game, text="Play Game", grid=[1,2], align="left")
        new_game            = PushButton(app, command=new_game, text="New Game", grid=[1,3], align="left", visible=True, enabled=False)
        exit_game           = PushButton(app, command=quit_game, text="Quit Game", grid=[1,4], align="left")
        # ~ poker_pic           = Picture(app, image="Suit Icons.gif", grid=[2,1], align="left")
        player_description  = Text(app, text="Players:", grid=[1,5], size=14, font="Times New Roman", color="black", align="left")
        player1             = PushButton(app, command=get_player1_info, text="Player 1", grid=[1,6], align="left")
        player2             = PushButton(app, command=get_player2_info, text="Player 2", grid=[1,7], align="left")
        Gui_options         = Text(app, text="Gui Options:", grid=[1,8], size=14, font="Times New Roman", color="black", align="left")
        update              = PushButton(app, command=update_game_state, text="Update", grid=[1,9], align="left")
        # ~ column_seperator    = Text(app, text="|   ", grid=[2,1], size=14, font="Times New Roman", color="black", align="left")
        # ~ column_seperator2   = Text(app, text="|   ", grid=[2,2], size=14, font="Times New Roman", color="black", align="left")
        # ~ column_seperator2   = Text(app, text="|   ", grid=[2,3], size=14, font="Times New Roman", color="black", align="left")
        # ~ column_seperator2   = Text(app, text="|   ", grid=[2,4], size=14, font="Times New Roman", color="black", align="left")
        game_state          = Text(app, text="Active", grid=[7,2], size=14, font="Times New Roman", color="black", align="left", visible=False)
        input_bet           = TextBox(app, grid=[2,1])
        raise_bet           = PushButton(app, command=raise_bet, text="Bet", grid=[3,1], align="left", visible=False, enabled=False)
        call_bet            = PushButton(app, command=call_bet, text="Call", grid=[4,1], align="left", visible=False, enabled=False)
        fold_bet            = PushButton(app, command=fold_bet, text="Fold", grid=[5,1], align="left", visible=False, enabled=False)
 
        show_g_buttons      = PushButton(app, command=show_g_buttons, text="Show Game Buttons", grid=[1,9], align="left")
        hide_g_buttons      = PushButton(app, command=hide_g_buttons, text="Hide Game Buttons", grid=[1,10], align="left")
        show_gi             = PushButton(app, command=show_game_info, text="Show Game Info", grid=[1,11], align="left")
        hide_gi             = PushButton(app, command=hide_game_info, text="Hide Game Info", grid=[1,12], align="left")
        show_game_result    = PushButton(app, command=show_game_result, text="Show Game Results", grid=[1,13], align="left")
        hide_game_result    = PushButton(app, command=hide_game_result, text="Hide Game Results", grid=[1,14], align="left")
        show_h_cards        = PushButton(app, command=show_h_cards, text="Show Hand Cards", grid=[1,15], align="left")
        hide_h_cards        = PushButton(app, command=hide_h_cards, text="Hide Hand Cards", grid=[1,16], align="left")
        game_state_title    = Text(app, text="Game State:", grid=[1,20], size=14, font="Times New Roman", color="black", align="left")
        game_state          = Text(app, text="", grid=[1,21], size=14, font="Times New Roman", color="black", align="left")
 
        game_info_1         = Text(app, text="P1:", grid=[8,2], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_2         = Text(app, text=self.g_players[0]._name, grid=[9,2], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_3         = Text(app, text="     ", grid=[10,2], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_4         = Text(app, text="Chips: $", grid=[11,2], size=14, font="Times New Roman", color="black", align="right", visible=False)
        game_info_5         = Text(app, text=str(self.g_players[0]._chips), grid=[12,2], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_6         = Text(app, text="P2:", grid=[8,3], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_7         = Text(app, text=self.g_players[1]._name, grid=[9,3], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_8         = Text(app, text="     ", grid=[10,3], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_9         = Text(app, text="Chips: $", grid=[11,3], size=14, font="Times New Roman", color="black", align="right", visible=False)
        game_info_10        = Text(app, text=str(self.g_players[1]._chips), grid=[12,3], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_11        = Text(app, text="Highest bet: $", grid=[8,4], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_12        = Text(app, text=str(self.high_bet()), grid=[9,4], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_13        = Text(app, text="Pot: $", grid=[11,4], size=14, font="Times New Roman", color="black", align="right", visible=False)
        game_info_14        = Text(app, text=str(self.g_pool), grid=[12,4], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_15        = Text(app, text="Player 1 Hand cards:", grid=[8,5], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_16        = Text(app, text="", grid=[9,5], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_17        = Text(app, text="Player 2 Hand cards:", grid=[8,6], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_18        = Text(app, text="", grid=[9,6], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_19        = Text(app, text="Table cards:", grid=[8,7], size=14, font="Times New Roman", color="black", align="left", visible=False)
        game_info_20        = Text(app, text="", grid=[9,7], size=14, font="Times New Roman", color="black", align="left", visible=False)
 
        game_signal         = 0
        game_result1        = Text(app, text="", grid=[9,22], size=14, font="Times New Roman", color="black", align="left")
        game_result2        = Text(app, text="", grid=[9,23], size=14, font="Times New Roman", color="black", align="left")
 
        gui_setup()
        app.display()
 
 
    def show_game_state(self):
        """ This show the game state using text """
        print("""
        +------------------------+------------------------+
        | P1: """ + self.g_players[0]._name + 
            """               | P2: """ + self.g_players[1]._name + 
                """    |
        +------------------------+------------------------+
        | Chips: $""" + str(self.g_players[0]._chips) + 
            """           | Chips: $""" + 
                str(self.g_players[1]._chips) + """            |
        +------------------------+------------------------+
        | Pot: $""" + str(self.g_pool) + 
            """ | Current bet: $""" + str(self.g_players[0]._bet) + 
                """ | Highest bet: $""" + str(self.high_bet()) + """
        +------------------------+------------------------+
        | Cards in hand: """ + str(self.g_players[0]._hand) + """
        +------------------------+------------------------+
        | Cards on board: """ + str(self.g_board) + """
        +------------------------+------------------------+
        """)
 
    def show_hand_cards(self):
        """ This reveal/show the players cards and table cards using text """
        print("""
        +------------------------+------------------------+
        | Hand cards (""" + str(self.g_players[0]._name) + """): """ + str(self.g_players[0]._hand) + """
        +------------------------+------------------------+
        | Hand cards (""" + str(self.g_players[1]._name) + """): """ + str(self.g_players[1]._hand) + """
        +------------------------+------------------------+
        | Table cards: """ + str(self.g_board) + """
        +------------------------+------------------------+
        """)
 
    def main(self):
        """ sets up the main menu """
 
        def start_game():
            main_menu.destroy()
            self.setup()
 
        def quit_game():
            exit()
 
        main_menu = App(title="Poker Game Menu", width=150, height=250)
 
        # ~ poker_pic       = Picture(main_menu, image="Suit Icons.gif", align="top")
        window_title    = Text(main_menu, text="Game Menu", size=13, font="Times New Roman", color="black", align="top")
        start_game      = PushButton(main_menu, command=start_game, text="Start Game", align="top")
        exit_game       = PushButton(main_menu, command=quit_game, text="Quit Game", align="top")
 
        main_menu.display()
 
 
        # gp = input("Do you want to play (y/n)? ")
 
        # if gp == "y":
        #     print("Starting game")
        #     self.setup()
        # if gp == "n":
        #     print("Closing game")
        #     exit()
 
    def setup(self):
        """ sets up a game vs a computer player """
        self.g_state = 0
        self.g_round = 0
        del self.g_players[:]
        del self.g_board[:]
 
        # p_name = input("What is your name?")
        self.g_players.append(Player("Player 1"))
        self.g_players.append(Player("Computer player"))
 
        for player in self.g_players:
            player._chips = 1000
            logger.info(str(player._name) + "'s chips: " + str(player._chips))
            logger.info(player._name + " joined the game")
 
        self.g_state += 1
        logger.info("Game state :" + str(self.g_state))
        self.g_round += 1
        logger.info("Round 1")
 
        self.game_window()
        # self.gameloop()
 
    def new_round(self):
        """ sets up a new round """
        self.g_state = 0
        self.g_pool = 0
        del self.g_board[:]
        for player in self.g_players:
            del player._hand[:]
            player._bet = 0
 
        self.g_state += 1
        logger.info("Game state :" + str(self.g_state))
        self.g_round += 1
        logger.info("Round " + str(self.g_round))
 
        # ~ self.gameloop()
 
 
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
 
    def deal1(self):
        """ create a deck, shuffle it, and deal 2 cards to each player """
        self.g_deck =  Deck()
        self.g_deck.shuffler()
 
        for player in self.g_players:
            player.drawCard(self.g_deck)
            player.drawCard(self.g_deck)
 
    def deal2(self):
        """ Flop - three community cards are flipped face up on the table """
        self.g_board.append(self.g_deck._cards.pop())
        self.g_board.append(self.g_deck._cards.pop())
        self.g_board.append(self.g_deck._cards.pop())
        # self.show_table()
 
        # ~ self.player_turn()
 
    def deal3(self):
        """ Turn - fourth community card is flipped face up on the table """
        self.g_board.append(self.g_deck._cards.pop())
        # self.show_table()
 
        # ~ self.player_turn()
 
    def deal4(self):
        """ River - fifth community card is flipped face up on the table """
        self.g_board.append(self.g_deck._cards.pop())
        # self.show_table()
 
        # ~ self.player_turn()
 
    # ~ def player_turn(self):
        # ~ """ player betting round """
        # ~ player = self.g_players[self.g_priority]
        # ~ self.show_game_state()
        # ~ # self.show_high_bet()
        # ~ # self.show_bet(player)
        # ~ if player._chips < 50:
            # ~ gp = input("You can now fold (f), call/check (c) or quit game (q)")
        # ~ else:
            # ~ gp = input("You can now fold (f), call/check (c), raise (r) or quit game (q)")
        # ~ if gp == "f":
            # ~ self.fold(player)
        # ~ elif gp == "c":
            # ~ self.call(player)
        # ~ elif gp == "r":
            # ~ hb = self.high_bet()
            # ~ cb = player._bet
            # ~ pc = hb - cb
            # ~ print("You call " + str(pc))
            # ~ while True:
                # ~ try:
                    # ~ bet = int(input("how much do you want to bet?"))
                    # ~ break
                # ~ except:
                    # ~ print("Please give a number")
            # ~ if isinstance(bet, int):
                # ~ self.bet(player, int(bet))
        # ~ elif gp == "q":
            # ~ exit()
 
        # ~ if gp in ["f", "c", "r", "f"]:
            # ~ if self.g_priority == 0:
                # ~ self.g_priority += 1
                # ~ self.computer_turn()
        # ~ else:
            # ~ self.player_turn()
 
    def computer_turn(self):
        """ first computer betting round """
        # unfinished
        player = self.g_players[self.g_priority]
        self.call(player)
 
        logger.info("Computer player betted, called or raised")
        self.g_priority -= 1
 
    # ~ def gameloop(self):
        # ~ self.blinds()
        # ~ self.deal1()
        # ~ self.player_turn()
        # ~ if self.g_state == 1:
            # ~ self.g_state += 1
            # ~ logger.info("Game state :" + str(self.g_state))
            # ~ self.deal2()
        # ~ if self.g_state == 2:
            # ~ self.g_state += 1
            # ~ logger.info("Game state :" + str(self.g_state))
            # ~ self.deal3()
        # ~ if self.g_state == 3:
            # ~ self.g_state += 1
            # ~ logger.info("Game state :" + str(self.g_state))
            # ~ self.deal4()
        # ~ if self.g_state == 4:
            # ~ self.g_state += 1
            # ~ logger.info("Game state :" + str(self.g_state))
            # ~ self.end_round()
            # ~ logger.info("Round over")
            # ~ gp = input("You can now quit (q) or Press enter to continue")
            # ~ if gp == "q":
                # ~ exit()
            # ~ else:
                # ~ self.new_round()
 
    def end_round(self):
        # print("End of Round Players: ")
        # print(self.g_players)
 
        self.show_hand_cards()
 
        bhp = self.find_winner(self.g_players)
        pc = len(bhp)
 
        if pc == 1:
            print("[" + bhp[0]._name + "] won the pot (" + str(self.g_pool) + ")")
            bhp[0]._chips = bhp[0]._chips + self.g_pool
            self.g_pool = 0
            # self.player_cleanup(bhp[0])
 
        if len(bhp) == 2:
            print("[" + bhp[0]._name + "] splits the pot (" + str(self.g_pool) + ") with [" + bhp[1]._name + "]")
            bhp[0]._chips = bhp[0]._chips + self.g_pool/2
            bhp[1]._chips = bhp[1]._chips + self.g_pool/2
            self.g_pool = 0
 
        for player in self.g_players:
            self.player_cleanup(player)
 
        logger.info("End of Round")
 
    def find_winner(self, players):
        winners = []
        best_hand_value = 0
        for player in players:
            a = self.best_hand(player)
            if a > best_hand_value:
                if best_hand_value != 0:
                    del winners[0]
                best_hand_value = a
                winners.append(player)
            elif self.best_hand(player) == best_hand_value:
                winners.append(player)
        # ~ self.show_winning_hand(best_hand_value)
        return winners
 
    def show_winning_hand(self, best_hand_value):
        if best_hand_value == 0:
            logger.error("Error: No winning hand was found.")
        if 1 <= best_hand_value < 2:
            print("Winning hand: High card")
        if 2 <= best_hand_value < 3:
            print("Winning hand: Pair")
        if 3 <= best_hand_value < 4:
            print("Winning hand: Two pair")
        if 4 <= best_hand_value < 5:
            print("Winning hand: Three of a kind")
        if 5 <= best_hand_value < 6:
            print("Winning hand: Straight")
        if 6 <= best_hand_value < 7:
            print("Winning hand: Flush")
        if 7 <= best_hand_value < 8:
            print("Winning hand: Full House")
        if 8 <= best_hand_value < 9:
            print("Winning hand: Four of a kind")
        if 9 <= best_hand_value < 10:
            print("Winning hand: Straight Flush")
        if 10 <= best_hand_value:
            print("Winning hand: Royal Straight Flush")
 
    def best_hand(self, player):
        egh = self.make_end_hand(player)
        rv = 0
 
        if self.r_flush(egh) != 0:
            rv = self.r_flush(egh)
        elif self.s_flush(egh) != 0:
            rv = self.s_flush(egh)
        elif self.kind4(egh) != 0:
            rv = self.kind4(egh)
        elif self.full_house(egh) != 0:
            rv = self.full_house(egh)
        elif self.flush(egh) != 0:
            rv = self.flush(egh)
        elif self.straight(egh) != 0:
            rv = self.straight(egh)
        elif self.kind3(egh) != 0:
            rv = self.kind3(egh)
        elif self.two_pair(egh) != 0:
            rv = self.two_pair(egh)
        elif self.pair(egh) != 0:
            rv = self.pair(egh)
        elif self.high_card(egh) != 0:
            rv = self.high_card(egh)
 
        return rv
 
    def score_hand(self, cards):
        egh = cards
        rv = 0
 
        if self.r_flush(egh) != 0:
            print("Royal Straight Flush")
            rv = self.r_flush(egh)
        elif self.s_flush(egh) != 0:
            print("Straight Flush")
            rv = self.s_flush(egh)
        elif self.kind4(egh) != 0:
            print("4 of a kind")
            rv = self.kind4(egh)
        elif self.full_house(egh) != 0:
            print("Full House")
            rv = self.full_house(egh)
        elif self.flush(egh) != 0:
            print("Flush")
            rv = self.flush(egh)
        elif self.straight(egh) != 0:
            print("Straight")
            rv = self.straight(egh)
        elif self.kind3(egh) != 0:
            print("3 of a kind")
            rv = self.kind3(egh)
        elif self.two_pair(egh) != 0:
            print("Two pair")
            rv = self.two_pair(egh)
        elif self.pair(egh) != 0:
            print("Pair")
            rv = self.pair(egh)
        elif self.high_card(egh) != 0:
            print("High card")
            rv = self.high_card(egh)
 
        return rv
 
    def make_end_hand(self, player):
        eh = []
        for card in player._hand:
            eh.append(card)
        for card in self.g_board[:]:
            eh.append(card)
        eh.sort(key=lambda x: x._value, reverse=False)
        # print(str(player._name) + "'s end hand: ")
        # print(eh)
        return eh
 
    def player_cleanup(self, player):
        player._bet       = 0
        player._hand      = []   # not sure if this actually empty the hand. I should test this. 
        # player.p_activity = False #  not sure if this should be implemented here or not.
 
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
        self.player_cleanup(player)
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
 
    # def card_value_finder(self, value):
    #     p_hand = self.g_board + self.g_players[0]._hand
    #     for card in p_hand:
    #         if card._value == value:
    #             return True
    #     return False
 
    def r_flush(self, hand):
        c1 = hand
        f1 = False
        h_suit = 0
        c_suit = 0
        d_suit = 0
        s_suit = 0
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = 0
        s1 = 0
        rv = 0
        t1 = []
        t2 = []
 
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
                if card._suit == "hearts":
                    t1.append(card)
        elif c_suit > 4:
            f1 = True
            for card in c1:
                if card._suit == "clubs":
                    t1.append(card)
        elif d_suit > 4:
            f1 = True
            for card in c1:
                if card._suit == "diamonds":
                    t1.append(card)
        elif s_suit > 4:
            f1 = True
            for card in c1:
                if card._suit == "spades":
                    t1.append(card)
 
        if f1:
            for card in t1:
                if card._value > 9:
                    t2.append(card)
 
            v1 = c1[0]._value
 
            for card in t2:
                if card._value == v1:
                    s1 += 1
                    if s1 == 5:
                        rv = 10
                        return rv
                    v1 = card._value + 1
                else:
                    v1 = card._value + 1
                    s1 = 1
 
        return 0
 
    def s_flush(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=False)
        t1 = []
        f1 = False
        h_suit = 0
        c_suit = 0
        d_suit = 0
        s_suit = 0
        v1 = 0
        s1 = 1
        hv1 = 0
        rv = 0
 
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
                if card._suit == "hearts":
                    t1.append(card)
        elif c_suit > 4:
            f1 = True
            for card in c1:
                if card._suit == "clubs":
                    t1.append(card)
        elif d_suit > 4:
            f1 = True
            for card in c1:
                if card._suit == "diamonds":
                    t1.append(card)
        elif s_suit > 4:
            f1 = True
            for card in c1:
                if card._suit == "spades":
                    t1.append(card)
 
        if f1:
            v1 = t1[0]._value + 1
            for card in t1:
                if card._value == v1:
                    s1 += 1
                    if s1 > 4:
                        hv1 = card._value
                    v1 = card._value + 1
                else:
                    v1 = card._value + 1
                    s1 = 1
 
        if hv1 != 0:
            rv = 9 + hv1/100
            return rv
        else:
            return 0
 
    def kind4(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=True)
        v1 = c1[0]._value
        k1 = 0
        hv1 = 0
        hv2 = 0
        rv = 0
 
        for card in c1:
            if card._value == v1:
                k1 += 1
                if k1 > 3:
                    hv1 = card._value
            else:
                v1 = card._value
                k1 = 1
 
        if hv1 != 0:
            for card in c1:
                if card._value != hv1:
                    if card._value > hv2:
                        hv2 = card._value
            rv = 8 + hv1/100 + hv2/10000
            return rv
        else:
            return 0
 
 
    def full_house(self, hand):
        c1  = hand
        c1.sort(key=lambda x: x._value, reverse=True)
        v1  = c1[0]._value
        h1  = 0
        hv1 = 0
        hv2 = 0
        rv  = 0
 
        for card in c1:
            if card._value == v1:
                h1 += 1
                if h1 == 3:
                    if hv1 < card._value:
                        hv1 = card._value
            else:
                v1 = card._value
                h1 = 1
 
        if hv1 != 0:
            v1 = c1[0]._value
            h1 = 0
            for card in c1:
                if card.value != hv1:
                    if card._value == v1:
                        h1 += 1
                        if h1 == 2:
                            if hv2 < card._value:
                                hv2 = card._value
                    else:
                        v1 = card._value
                        h1 = 1
        if hv2 != 0:
            rv = 7 + hv1/100 + hv2/10000
            return rv
        else:
            return 0
 
    def flush(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=True)
        h_suit = 0
        c_suit = 0
        d_suit = 0
        s_suit = 0
        f1 = 0
        hv1 = 0
        hv2 = 0
        hv3 = 0
        hv4 = 0
        hv5 = 0
        rv = 0
 
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
            for card in c1:
                if card._suit == "hearts":
                    f1 += 1
                    if f1 == 1:
                        hv1 = card._value
                    if f1 == 2:
                        hv2 = card._value
                    if f1 == 3:
                        hv3 = card._value
                    if f1 == 4:
                        hv4 = card._value
                    if f1 == 5:
                        hv5 = card._value
            rv = 6 + hv1/100 + hv2/10000 + hv3/1000000 + hv4/100000000 + hv5/10000000000
            return rv
        elif c_suit > 4:
            for card in c1:
                if card._suit == "clubs":
                    f1 += 1
                    if f1 == 1:
                        hv1 = card._value
                    if f1 == 2:
                        hv2 = card._value
                    if f1 == 3:
                        hv3 = card._value
                    if f1 == 4:
                        hv4 = card._value
                    if f1 == 5:
                        hv5 = card._value
            rv = 6 + hv1/100 + hv2/10000 + hv3/1000000 + hv4/100000000 + hv5/10000000000
            return rv
        elif d_suit > 4:
            for card in c1:
                if card._suit == "diamonds":
                    f1 += 1
                    if f1 == 1:
                        hv1 = card._value
                    if f1 == 2:
                        hv2 = card._value
                    if f1 == 3:
                        hv3 = card._value
                    if f1 == 4:
                        hv4 = card._value
                    if f1 == 5:
                        hv5 = card._value
            rv = 6 + hv1/100 + hv2/10000 + hv3/1000000 + hv4/100000000 + hv5/10000000000
            return rv
        elif s_suit > 4:
            for card in c1:
                if card._suit == "spades":
                    f1 += 1
                    if f1 == 1:
                        hv1 = card._value
                    if f1 == 2:
                        hv2 = card._value
                    if f1 == 3:
                        hv3 = card._value
                    if f1 == 4:
                        hv4 = card._value
                    if f1 == 5:
                        hv5 = card._value
            rv = 6 + hv1/100 + hv2/10000 + hv3/1000000 + hv4/100000000 + hv5/10000000000
            return rv
        else:
            return 0
 
    def straight(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=False)
        v1 = c1[0]._value
        s1 = 0
        hv1 = 0
        rv = 0
 
        for card in c1:
            if card._value == v1:
                s1 += 1
                if s1 > 4:
                    hv1 = card._value
                v1 = card._value + 1
            else:
                v1 = card._value + 1
                s1 = 1
 
        if c1[-1]._value == 14:
            if s1 < 5:
                s1 = 1
                v1 = 2
                for card in c1:
                    if card._value == v1:
                        s1 += 1
                        if s1 > 4:
                            if hv1 < card._value:
                                hv1 = card._value
                        v1 = card._value +1
        if hv1 != 0:
            rv = 5 + hv1/100
            return rv
        else:
            return 0
 
    def kind3(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=True)
        v1 = c1[0]._value
        k1 = 0
        hv1 = 0
        hv2 = 0
        hv3 = 0
        rv = 0
 
        for card in c1:
            if card._value == v1:
                k1 += 1
                if k1 == 3:
                    hv1 = card._value
            else:
                v1 = card._value
                k1 = 1
 
        if hv1 != 0:
            for card in c1:
                if card._value != hv1:
                    if hv2 == 0:
                        hv2 = card._value
                    elif hv3 == 0:
                        hv3 = card._value
            rv = 4 + hv1/100 + hv2/10000 + hv3/1000000
            return rv
        else:
            return rv
 
    def two_pair(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=True)
        v1 = c1[0]._value
        p1 = 0
        hv1 = 0
        hv2 = 0
        hv3 = 0
        rv = 0
 
        for card in c1:
            if card._value == v1:
                p1 += 1
                if p1 == 2:
                    if hv1 == 0:
                        hv1 = card._value
                    elif hv2 == 0:
                        hv2 = card._value
                    p1 = 0
            else:
                v1 = card._value
                p1 = 1
 
        if hv2 != 0:
            for card in c1:
                if card._value != hv1:
                    if card._value != hv2:
                        if hv3 < card._value:
                            hv3 = card._value
            rv = 3 + hv1/100 + hv2/10000 + hv3/1000000
            return rv
        else:
            return 0
 
    def pair(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=True)
        v1 = c1[0]._value
        p1 = 0
        hv1 = 0
        hv2 = 0
        hv3 = 0
        hv4 = 0
        rv = 0
 
        for card in c1:
            if card._value == v1:
                p1 += 1
                if p1 == 2:
                    hv1 = card._value
            else:
                v1 = card._value
                p1 = 1
 
        if hv1 != 0:
            for card in c1:
                if card._value != hv1:
                    if hv2 == 0:
                        hv2 = card._value
                    elif hv3 == 0:
                        hv3 = card._value
                    elif hv4 == 0:
                        hv4 = card._value
            rv = 2 + hv1/100 + hv2/10000 + hv3/1000000 + hv4/100000000
            return rv
        else:
            return 0
 
    def high_card(self, hand):
        c1 = hand
        c1.sort(key=lambda x: x._value, reverse=True)
        hv1 = c1[0]._value
        hv2 = c1[1]._value
        hv3 = c1[2]._value
        hv4 = c1[3]._value
        hv5 = c1[4]._value
        rv = 1 + hv1/100 + hv2/10000 + hv3/1000000 + hv4/100000000 + hv5/10000000000
        return rv
 
g1 = Game("Poker")