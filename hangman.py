# Import statements: DO NOT delete these! DO NOT write code above this!
import random
from random import randrange
from string import *
# from hangman_lib import *

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
secret_word = ""
letters_guessed = []

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
    letters_unused = []
    for i in range(ord('a'), ord('z')+1):
        letters_unused.append(chr(i))

    string_to_print = ""
    for i in letters_guessed:
        letters_unused.remove(i)
        for j in range(0, len(secret_word)):
            if i == secret_word[j]:
                letters_correct[j] = secret_word[j]

    for i in range(0, len(secret_word)):
        if i in letters_correct:
            string_to_print += secret_word[i]
        else:
            string_to_print += "-"

    print(string_to_print)
    print("Letters that hasn't been used:", letters_unused)
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
    mode_difficulty = input("Select the difficulty(easy, medium, hard): ")
    if mode_difficulty.lower() == "easy":
        MAX_GUESSES = 12
        while not 1 < len(secret_word) < 4:
            secret_word = get_word()
    elif mode_difficulty.lower() == "medium":
        MAX_GUESSES = 6
        while not 4 <= len(secret_word) <= 8:
            secret_word = get_word()
    elif mode_difficulty.lower() == "hard":
        MAX_GUESSES = 5
        while not len(secret_word) > 8:
            secret_word = get_word()
    else:
        print("You have inputted the incorrect difficulty!")
        exit()

    mode_player = int(input("Select the player mode(Single->1, 2-player->2): "))
    if mode_player == 1:
        while (mistakes_made < MAX_GUESSES) and (not word_guessed()):
            select_num = int(input("Select what you want to guess(letter->1, word->2), : "))
            match select_num:
                case 1:
                    guess_bool = False
                    print(MAX_GUESSES - mistakes_made, "guesses left")
                    while True:
                        dupli = False
                        letter = input("Input a letter you guess: ")
                        letter.lower()
                        for i in letters_guessed:
                            if i == letter:
                                dupli = True
                                print("It is already used!")
                                break
                        if not dupli:
                            break
                    letters_guessed.append(letter)
                    for i in range(0, len(secret_word)):
                        if letter == secret_word[i]:
                            guess_bool = True
                            break
                    if guess_bool:
                        print("You guessed right!")
                        print_guessed()
                    else:
                        print("You guessed wrong!")
                        print_guessed()
                        mistakes_made += 1
                case 2:
                    guess_bool = False
                    print(MAX_GUESSES - mistakes_made, "guesses left")
                    word = input("Input a word you guess: ")
                    word.lower()
                    if word == secret_word:
                        print("You guessed right!")
                        break
                    else:
                        print("You guessed wrong!")
                        print_guessed()
                        mistakes_made += 2
                case _:
                    print("Input the correct number!")

        if word_guessed():
            print("You won!!!")
        else:
            print("You lost...")

    elif mode_player == 2:
        attempt = 1
        while (mistakes_made < MAX_GUESSES) and (not word_guessed()):
            if attempt % 2 == 1:
                print("Player1's turn!")
            else:
                print("Player2's turn!")

            select_num = int(input("Select what you want to guess(letter->1, word->2), : "))
            match select_num:
                case 1:
                    guess_bool = False
                    print(MAX_GUESSES - mistakes_made, "guesses left")
                    while True:
                        dupli = False
                        letter = input("Input a letter you guess: ")
                        letter.lower()
                        for i in letters_guessed:
                            if i == letter:
                                dupli = True
                                print("It is already used!")
                                break
                        if not dupli:
                            break
                    letters_guessed.append(letter)
                    for i in range(0, len(secret_word)):
                        if letter == secret_word[i]:
                            guess_bool = True
                            break
                    if guess_bool:
                        print("You guessed right!")
                        print_guessed()
                    else:
                        print("You guessed wrong!")
                        print_guessed()
                        mistakes_made += 1
                        attempt += 1
                case 2:
                    guess_bool = False
                    print(MAX_GUESSES - mistakes_made, "guesses left")
                    word = input("Input a word you guess: ")
                    word.lower()
                    if word == secret_word:
                        print("You guessed right!")
                        break
                    else:
                        print("You guessed wrong!")
                        print_guessed()
                        attempt += 1
                        mistakes_made += 2

        if word_guessed():
            if attempt % 2 == 1:
                print("Player1 won!")
            else:
                print("Player2 won!")
        else:
            print("Try again!")
    else:
        print("You have inputted incorrect mode!")
        exit()

    return None


if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    play_hangman()
