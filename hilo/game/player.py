#This follows the player, and allows them to guess
import random

class Player():

    def __init__(self):
        self.score = 300
        self.old_card = 0
        self.new_card = 0
        self.user_decision = ""
        self.end_game = True
        self.first_turn = True

    def keep_playing(self):
        if self.score < 0:
            self.end_game = False
        else:
            if not self.first_turn:
                invalid_input = True
                while invalid_input:
                    try:
                        self.user_decision = input("Would you like to keep playing(y/n)? ")
                        if self.user_decision.lower() == "y":
                            invalid_input = False
                        elif self.user_decision.lower() == "n":
                            invalid_input = False
                            self.end_game = False
                        else:
                            print("You have entered an invalid input. ")
                            invalid_input = True
                    except:
                        print("Error: Please enter a valid input.")
            else:
                self.first_turn = False
        return self.end_game
                

    def player_guess(self):
        invalid_input = True
        while invalid_input:
            try:
                user_input = input("Higher or lower(h/l)? ")
                user_input = user_input.lower()
                if user_input == "h":
                    self.user_decision = user_input
                    invalid_input = False
                    return self.user_decision
                elif user_input == "l":
                    self.user_decision = user_input
                    invalid_input = False
                    return self.user_decision
                else:
                    print("You have entered an invalid input. ")
                    invalid_input = True
            except:
                print("Error: Please enter a valid input. ")

    def calculate_score(self):
        self.old_card = self.new_card
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
        print(f"The new card is {self.new_card}")
        print(f"Your score is: {self.score}")

    def deal_card(self):
        self.new_card = random.randint(1, 14)
        print(f"The card is {self.new_card}")