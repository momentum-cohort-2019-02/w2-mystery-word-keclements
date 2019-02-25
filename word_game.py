# Import 
import string
import random

#word_to_guess = []# the word user trying to guess
#letters_guessed = a list of the letters the user has guessed
#bad_guesses = # the number of bad guesses the user has made

with open('words.txt') as file: 
    word_list = file.read().splitlines() 
   #  print(word_list) #valid test of print word_list

word_choice_list = []

#function defile difficulty
def easy_mode():
    with open('words.txt') as file: #file variable defined as words.txt
        for small_words in file:
            if len(small_words) >= 4 and len(small_words) <= 6:
               word_choice_list.append(small_words)
               return print(small_words)

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
    elif chosen_difficulty == 'hard':
        hard_mode()


difficulty_level()
#print(difficulty_level)




#def game 

#word = 
# random word generated from user choice from the the chosen difficult yay

#get_random_word(chosen_difficulty)


#get
#et_letter_from_user: 



# make random word
# from word in word_list

#assign difficulty to word
 #   if random_word = len(word_list) < 4


