#This follows the player, and allows them to guess
import random

class Player():

    def __init__(self):
        self.score = 300
        self.old_card = 0
        self.new_card = 0
        self.user_decision = ""
        self.play = True
        self.first_turn = True

    def keep_playing(self):
        '''
        Returns False if score is below 0 or player enters n
        '''

        # If score drops below 0 it is game over.
        if self.score < 0:
            return False
        else:

            # Prompt if they'd like to keep playing each turn after the first.
            if not self.first_turn:
                invalid_input = True
                while invalid_input:
                    user_input = input("Would you like to keep playing(y/n)? ")
                    user_input = user_input.lower()
                    if user_input == "y":
                        invalid_input = False
                    elif user_input == "n":
                        invalid_input = False
                        self.play = False
                    else:
                        print("You have entered an invalid input. ")
            else:
                self.first_turn = False
        return self.play
                

    def player_guess(self):
        '''
        Gets valid input from the user.
        '''
        invalid_input = True
        while invalid_input:
            user_input = input("Higher or lower(h/l)? ")
            user_input = user_input.lower()
            if user_input == "h":
                self.user_decision = user_input
                invalid_input = False

            elif user_input == "l":
                self.user_decision = user_input
                invalid_input = False

            else:
                print("You have entered an invalid input. ")
                invalid_input = True


    def calculate_score(self):
        '''
        Deals a new card and then calculates the score.
        '''
        self.old_card = self.new_card

        # Make sure that the new card isn't a copy
        copy = True
        while copy:
            self.new_card = random.randint(1,14)
            if self.new_card != self.old_card:
                copy = False
        if self.user_decision == "h":
            if self.new_card > self.old_card:
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        elif self.user_decision == "l":
            if self.new_card < self.old_card:
                self.score = self.score + 100
            else:
                self.score = self.score - 75

    def deal_card(self):
        '''
        Deals a new card to start the next round.
        '''
        self.new_card = random.randint(1, 14)
        print(f"The card is {self.new_card}")