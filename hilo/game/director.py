#This file manages and directs the other classes
#imports the class Player into our program.
from game.player import Player

class Director():

    def __init__(self):
        self.card = 0
        self.previouse_card = 0
        self.keep_playing = ""
        self.player = Player()

        
    #A function to start the game.
    def start_game(self):
        while self.player.keep_playing():
            self.do_input()
            self.do_updates()
            self.do_outputs()
            print()
            print()

    def do_input(self):
        self.player.deal_card()
        self.player.player_guess()

    def do_updates(self):
        self.player.calculate_score()

    def do_outputs(self):
        pass