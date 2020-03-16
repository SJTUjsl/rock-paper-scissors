# Write your code here
import random


def help_():
    print("""
            This is a rock-scissors-paper game simulator,
            you can write you choice in the window and the
            computer will give you its choice. If you want
            to exit the game, write "!exit". Have fun!
            """)


def convert_to_dic(rating_file):
    """
    Convert the rating txt to a dictionary,
    with name as the key and rating as the value.
    Get a file name string and return a rating dictionary

    """
    rating_list = open(rating_file, 'r')
    rating_dictionary = {}
    for rate in rating_list.readlines():
        rate = rate.strip().split()
        rating_dictionary[rate[0]] = int(rate[1])
    rating_list.close()
    return rating_dictionary


def game_start(player_choice, game_rule):
    """
    Get the game rule (rock-scissors-paper as default) and player's choice
    as arguments, index the rule, and return the win list and lost list.
    The elements whose index are between the choice (excluded) and the sum
    of the choice index and half size of the list(if greater than the length,
    then get the mode) should be stored in the win list.
    The lose list is similarly chose
    """
    win_list = []
    lose_list = []
    length = len(game_rule)
    player_index = game_rule.index(player_choice)
    for i in range(length // 2):
        i += 1
        lose_list.append(game_rule[(player_index + i) % length])
        win_list.append(game_rule[(player_index + i + length // 2) % length])

    return [win_list, lose_list]


# Set up
rating_dic = convert_to_dic('rating.txt')
name = input('Enter your name: ')
print('Hello, ' + name)
# Get the game rule customized by the player
# and convert it to a list by removing commas
rule = input()
# Get the choice list that the program can choose from
if len(rule) == 0:
    choice_list = ['rock', 'paper', 'scissors']
else:
    choice_list = rule.split(',')
print('Okay, let\'s start')

# Get the player's rating
if name in rating_dic:
    rating = rating_dic[name]
else:
    rating = 0
# Loop
while True:
    choice = input()
    # None-game choice
    if choice == '!exit':
        print('Bye!')
        break
    elif choice == '!help':
        help_()
        continue
    elif choice == '!rating':
        print('Your rating: ' + str(rating))
        continue

    # Game begin!
    # Randomly choose an answer
    answer = random.choice(choice_list)
    [win, lose] = game_start(choice, choice_list)
    if choice == answer:
        print('There is a draw ({})'.format(choice))
        rating += 50
        continue

    elif answer in win:
        print('Well done. Computer chose {} and failed'.format(answer))
        rating += 100
        continue
    elif answer in lose:
        print('Sorry, but computer chose {}'.format(answer))
        continue
