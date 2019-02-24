# Import 
import string
import random

with open('words.txt') as file: 
    word_list = file.read().splitlines() 
   #  print(word_list) #valid test of print word_list

easy_list = []
medium_list = []
hard_list = []

#function defile difficulty
def easy_mode():
    with open('words.txt') as file: #file variable defined as words.txt
        for small_words in file:
            if len(small_words) >= 4 and len(small_words) <= 6:
                easy_list.append(small_words)

def medium_mode():
    with open('words.txt') as file: #file variable defined as words.txt
        for medium_words in file:
            if len(medium_words)  >= 6 and len(medium_words) <=8:
                medium_list.append(medium_words)

def hard_mode():
    with open('words.txt') as file:
        for hard_words in file:
            if len(hard_words) >= 8:
                hard_list.append(hard_words)

def difficulty_level():
    chosen_difficulty = input( "Choose difficulty of the game? Levels are easy, medium, hard word. ")
    if chosen_difficulty == 'easy':
        easy_mode()
    elif chosen_difficulty == 'medium':
        medium_mode()
    else hard_mode =='hard':
        hard_mode()
    




make random word
from word in word_list


assign difficulty to word
    if random_word = len(word_list) < 4

# # nameoflist.apppend(letter)



# ####
# line 8 test to print randonm word still has \n
