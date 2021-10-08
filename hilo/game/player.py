#This follows the player, and allows them to guess
import random

class Player():

    def __init__(self):
        self.score = 300
        self.old_card = 0
        self.new_card = 0
        self.user_decision = ""
        self.end_game = True

    def keep_playing(self):
        if self.score < 0:
            self.end_game = False
        else:
            self.user_decision = input("Would you like to keep playing(y/n)? ")
            if self.user_decision == "y":
                pass
            else:
                self.end_game = False
        return self.end_game
                

    def player_guess(self):
        self.user_decision = input("Higher or lower(h/l)? ")

    def calculate_score(self):
        self.old_card = self.new_card
        self.new_card = random.randint(1,14)
        if self.user_decision.lower() == "h":
            if self.new_card > self.old_card:
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        else:
            if self.new_card < self.old_card:
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        print(f"The new card is {self.new_card}")
        print(f"Your score is: {self.score}")

    def deal_card(self):
        self.new_card = random.randint(1, 14)
        print(f"The card is {self.new_card}")