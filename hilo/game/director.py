#This file manages and directs the other classes
#imports the class Player into our program.
from game.player import Player

class Director():

    def __init__(self):
        self.player = Player()
   
    def start_game(self):
        '''
        Game loop
        '''
        while self.player.keep_playing():
            self.do_input()
            self.do_updates()
            self.do_outputs()

    def do_input(self):
        '''
        Deals card and gets players guess.
        '''
        self.player.deal_card()
        self.player.player_guess()

    def do_updates(self):
        '''
        Calculates score
        '''
        self.player.calculate_score()

    def do_outputs(self):
        '''
        Displays the new card and their new score.
        '''
        print(f"The new card is {self.player.new_card}")
        print(f"Your score is: {self.player.score}")
        print()
        print()