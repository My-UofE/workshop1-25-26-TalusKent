import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    middle_items = []
    n = len(poss_values) 
    middle_items.append(poss_values[n//2])
    if n%2 == 0:
        middle_items.append(poss_values[(n+1)//2])
    return middle_items[0]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    return (next_val > current_val and user_input == "h") or (next_val < current_val and user_input == "l")

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    result = False
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            result = True
        
    return result
