from phrase import Phrase
import random


class Game:
    def create_phrases(self):
        phrases = [Phrase("Most things that never get done never get done because they never get started"), Phrase("Discipline equals freedom"), Phrase("Do what you can with all you have wherever you are"), Phrase("Get after it"), Phrase("Up and Rock and Roll")]
        return phrases

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = []

    def welcome(self):
        print("="*60+"""
*** WELCOME TO NIKOLAI'S MOTIVATIONAL PHRASE HUNTER 2020 ***
"""+"="*60, "\nRULES ===> You've got 5 tries to guess the phrase.\nPlease enter 1 letter at a time.\n")

    def get_guess(self):
        while True:
            user_guess = (input("Please enter a letter: ")).lower()
            if not user_guess.isalpha():
                print("That's not a valid selection. Please enter a letter.")
            elif len(user_guess) != 1:
                print("Please enter one letter at a time.")
            else:
                return user_guess

    def start(self):
        self.welcome()
        self.active_phrase.display(self.guesses)

        while not self.missed >= 5:
            print(f"*** Number missed: {self.missed} *** \n")
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if self.active_phrase.check_guess(user_guess):
                print("YAY!\n")
                self.active_phrase.display(self.guesses)
                if self.active_phrase.check_complete(self.guesses):
                    print("CONGRATS! You win!\n")
                    break
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
                print("\nBummer :(\n")

        if self.missed == 5:
            print("You lost. Please play again!\n")
