# Import 
import string
import random

#word_to_guess = []# the word user trying to guess
#letters_guessed = a list of the letters the user has guessed
#bad_guesses = # the number of bad guesses the user has made

with open('words.txt') as file: 
    word_list = file.read().splitlines() 
   #  print(word_list) #valid test of print word_list

# Variables used 

word_choice_list = []
word_to_guess = []
letters

#function defile difficulty
def easy_mode():
    with open('words.txt') as file: #file variable defined as words.txt
        for small_words in file:
            if len(small_words) >= 4 and len(small_words) <= 6:
               word_choice_list.append(small_words)

def medium_mode():
    with open('words.txt') as file: #file variable defined as words.txt
        for medium_words in file:
            if len(medium_words)  >= 6 and len(medium_words) <=8:
                word_choice_list.append(medium_words)

def hard_mode():
    with open('words.txt') as file:
        for hard_words in file:
            if len(hard_words) >= 8:
                word_choice_list.append(hard_words)

def difficulty_level():
    chosen_difficulty = input( "Choose difficulty of the game? Levels are easy, medium, hard word. ")
    if chosen_difficulty == 'easy':
        easy_mode()
    elif chosen_difficulty == 'medium':
        medium_mode()
	else hard_mode =='hard':
        hard_mode()


def letter_in_word (letter, random_generated_word):
    letter = input("Guess a letter for this word?") # renamed from user input and named in letter variable
    used_letters.append(letter)
    if letter in random_generated_word:
        return letter #return closes if statement above 
    else:
        return "_"

def letter_not_in_word(letter, random_generated_word):
    letter = input("Guess a letter for this word?")
    used_letters.append(letter)
    if letter not in random_generated_word:
        allowed_guess -= 1
        print("You have " + allowed_guess + " left")
        return letter
    else:

def game