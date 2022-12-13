# Import statements: DO NOT delete these! DO NOT write code above this!
import random
from random import randrange
from string import *

# Start of helper code
# -----------------------------------

# Import words file
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")

    ####### YOUR CODE HERE ######
    wordlist = []
    with open(WORDLIST_FILENAME, "r") as word_file:
        while True:
            line = word_file.readline()
            if not line:
                break
            wordlist.extend(line.split())

    print("  ", len(wordlist), "words loaded.")
    word_file.close()
    return wordlist

    pass  # This tells your code to skip this function; delete it when you
    # start working on this function


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()


def get_word():
    """
    Returns a random word from the word list
    """
    ####### YOUR CODE HERE ######
    rand_num = random.randrange(0, len(words_dict))
    word = words_dict[rand_num]
    return word


# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()

# end of helper code
# -----------------------------------

# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = get_word()
letters_guessed = ['a', 'b', 'p', 'r', 't', 'g']


# From part 2, 3 and, 4:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    letters_correct = {}
    for i in letters_guessed:
        for j in range(0, len(secret_word)):
            if i == secret_word[j]:
                letters_correct[j] = secret_word[j]

    if len(letters_correct) == len(secret_word):
        return True
    else:
        return False


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    letters_correct = {}
    string_to_print = ""
    for i in letters_guessed:
        for j in range(0, len(secret_word)):
            if i == secret_word[j]:
                letters_correct[j] = secret_word[j]

    for i in range(0, len(secret_word)):
        if i in letters_correct:
            string_to_print += secret_word[i]
        else:
            string_to_print += "-"

    return string_to_print


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
    print('Starting game ... ')
    # Update secret_word. Don't uncomment this line until you get to Step 6 (Second part).
    secret_word = get_word()
    ####### YOUR CODE HERE ######

    return None


if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    play_hangman()
