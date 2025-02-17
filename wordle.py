"""
File: wordle.py
Author: Ethan Holley
Purpose: This program plays the game wordle.
"""

import random

def read_file(file_name):
    """
    This function reads the words file and extracts only the 5-letter words from 
    the dictionary.
    Parameters:
        file_name: the file being analyzed
    Returns:
        wordle_list - list of all 5-letter words.
    """
    # gets only 5 letter words from file 
    f = open(file_name, 'r')
    wordle_list = []
    for line in f:
        word = line.strip().lower()
        if len(word) == 5:
            wordle_list.append(word)
    return wordle_list

def choose_random_word(wordle_list):
    """
    This function chooses a random word from the wordle_list of words.
    Parameters:
        wordle_list - list of all 5 letter words
    Returns:
        random_word - the random chosen 5 letter word
    """
    random_index = random.randint(0, len(wordle_list))
    random_word = wordle_list[random_index]
    return random_word

def get_user_guess():
    """
    This function prompts the user to enter a guess.
    Parameters:
        None
    Returns:
        None
    """
    # prompts user for input word
    input_word = input('\nEnter a 5 letter word to guess: ').lower()
    return input_word

def check_validity(word_list, input_word):
    """
    This function checks to make the word guessed by user is valid.
    Parameters:
        word_list - list of wordle words
        input_word - user input guess
    Returns:
        boolean T or F
    """
    # checks if user_input is a valid word
    if input_word in word_list:
        return True
    return False

def update_progress(user_word, random_word, wordle_list):
    """
    This function produces the current progress in gameplay based 
    on the user's most previous guess.
    Parameters:
        user_word - user's guessed word
        random_word - wordle's random chosen word
        wordle_list - list of all wordle words
    Returns:
        current string of the user's guess matched with correct word.
    """
    # checks user_word with random_word and matches letters accordingly
    progress_str = ''
    if check_validity(wordle_list, user_word):
        for i in range(len(random_word)):
            if user_word[i] == random_word[i]:
                progress_str += user_word[i] + ' '
            elif user_word[i] in random_word:
                progress_str += '* '
            else:
                progress_str += '_ '
        return progress_str
    else:
        return False
    
def play_wordle(user_word, random_word, word_list):
    """
    This function is the main gampeplay for wordle. It tracks the number of guesses
    and prints out the progress made by the user.
    Parameters:
        user_word - user guess
        random_word - word to be guessed
        word_list - list of all possible wordle words
    Returns:
        None
    """
    # tracks num_guesses and simulates wordle game by calling previous functions
    num_guesses = 1
    game_over = False
    while num_guesses < 6 and game_over == False:
        get_progress = update_progress(user_word, random_word, word_list)
        if get_progress == False:
            num_guesses += 1
            print("Invalid Word. Please try again.")
            user_word = get_user_guess()
            if user_word == random_word:
                game_over = True
                print(f'Congrats! You won in {num_guesses} guesses.')
        else:
            print('\nResult:\n' + get_progress)
            num_guesses += 1
            user_word = get_user_guess()
            if user_word == random_word:
                game_over = True
                if num_guesses == 1:
                    print(f'\nCongrats! You won in {num_guesses} guess.')
                else:
                    print(f'\nCongrats! You won in {num_guesses} guesses.')
        if num_guesses >= 6:
            game_over = True
            print(f'\nSorry, you\'re out of guesses. The word was {random_word}.')

def main():
    # calls functions
    print("Let's Play Wordle!")
    print("Directions: Guess a 5 letter word. If the word you guess has matching letters")
    print("in the wrong positions, a \"*\" will be printed out. If word has letters in the")
    print("correct positions as the word being guessed, the letter in be revealed.")
    print("You have 6 guesses to get the word correct. Good Luck!")
    word_list = read_file('words.txt')
    random_word = choose_random_word(word_list)
    user_word = get_user_guess()
    print(play_wordle(user_word, random_word, word_list))
main()


