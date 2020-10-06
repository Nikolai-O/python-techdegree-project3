from game import Game


if __name__ == "__main__":
    game = Game()

game.start()

print('Would you like to play again?')
answers = ['y', 'n']
answer = input('y/n: ').lower()

while answer not in answers:
    print("Please enter y or n...")
    answer = input('y/n: ').lower()

while answer == 'y':
    game = Game()
    game.start()
    print('Would you like to play again?')
    answer = input('y/n: ').lower()
    while answer not in answers:
        print("Please enter y or n...")
        answer = input('y/n: ').lower()

print("\nThank you for playing NIKOLAI'S MOTIVATIONAL PHRASE HUNTER 2020\n")
