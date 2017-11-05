# Hangman
# A game by Teresa Tran
# 11/4/2017

import random

# constants
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
    ===''','''
  +---+
   0  |
      |
      |
    ===''','''
  +---+
  0   |
  |   |
      |
    ===''','''
  +---+
  0   |
 /|   |
      |
    ===''','''
  +---+
  0   |
 /|\  |
      |
    ===''','''
  +---+
  0   |
 /|\  |
 /    |
    ===''','''
  +---+
  0   |
 /|\  |
 / \  |
    ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
    ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
    ===''']

WORDS = {"animals" :'''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram
rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
toad trout turkey turtle weasel whale wolf wombat zebra'''.split() "food" : '''
fries cake cupcake chips water smoothie taco pho noodles cheese milk pepper donut
pretzel cookie burrito rice pork beef chicken popsicle bread boba squid fish burger
watermelon apple pear orange tangerine broccoli lettuce cabbage candy''' .split()

def get_random_word(wordDict):
    wordKey = random.choice(list(wordDict.key())
#Second, randomly select word from the key's list in the dictionary
    word_index = random.randint(0, len(wordDict[wordKey]) - 1)
    key_list = [wordDict{wordKey][word_index], wordKey]
    key_random = random.randint(0, len(key_list)-1) # 0, 1

    print(wordDict[wordKey][word_index], wordKey]) #prints out a list
    return key_list(key_random) #this should return a word from the list

    # show drawing and blanks to player
def print_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])  # this is where its wrong. Hangman pics at the index at 7
    print()
    print("Missed letters: ")
    for letter in missed_letters:
        print(letter, end="")
    print()
    blanks = "_" * len(secret_word)
    for i in range(0, len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter + " ", end="")
    print()

def get_guess(already_guessed):
    while True:
        print("Guess a letter:")
        guess = input().lower()
        if len(guess) != 1:
            print("Please guess a single letter at a time.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("That is not a letter. Try again.")
        else:
            return guess

def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def play():
    print("H A N G M A N")
    print("A game by Teresa Tran")
    missed_letters, correct_letters = "", ""
    secret_word = get_random_word(WORDS)
    stop_game = False
    amount_of_games = 0
    amount_of_won = 0
    amount_of_lost = 0
    while not stop_game:
        # show drawing and blanks to player
        print_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters += guess
        else:
            missed_letters += guess
        # check if player has won
        # To do so, you need to compare what they've guessed to the secret word
        # Essentially, check if all the letters in secret_word are in correct_letters
        i = 0
        match = True
        while match and i < len(secret_word):
            if secret_word[i] not in correct_letters:
                match = False
            i += 1
        if match:
            print("Yes! The secret word is " + secret_word + "! You win!")
            amount_of_won += 1
            amount_of_games += 1
            stop_game = True
        elif len(missed_letters) == len(HANGMAN_PICS) - 1: #length of Hangman Pictures = 7, missed = 7; Player loses
            print_board(missed_letters, correct_letters, secret_word)
            print("You have run out of guesses!")
            print("After " + str(len(missed_letters)) + " missed guesses and " + str(len(correct_letters))
                  + " correct guesses, the secret word was " + secret_word)
            amount_of_lost += 1
            amount_of_games += 1
            stop_game = True
        print("You have played", amount_of_games, "games.")
        print("You have won", amount_of_won, "games and have lost", amount_of_lost, "games.")
        if stop_game:
            if play_again():
                missed_letters, correct_letters = "", ""
                stop_game = False
                secret_word = get_random_word(WORDS)
            else:
                print("Goodbye!")

play()
