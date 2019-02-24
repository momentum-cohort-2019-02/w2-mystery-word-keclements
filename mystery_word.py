#load words from words.txt

with open("words.txt") as word_file:
    word_list = word_file.readlines()
    print(word_list)

# Import library
import 

# def getRandomWord(wordList):
#  41.     # This function returns a random string from the passed list of
#            strings.
#  42.     wordIndex = random.randint(0, len(wordList) - 1)
#  43.     return wordList[wordIndex]
# Let the user choose a level of difficulty at the beginning of the program. Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.

# # User intreaction
#     # tell user levels of difficituly
#     # ask user what level of difficulty to play
#     # user input level difficulty based on scale of 1-3
#     # (code thing) take user input 
#     # given user input choose random word
#     # take random word and start game (MORE DETAIL & Steps here for the program code 
#      # if user puts in more than 1 letter program tells them how invalid (print choose one

# # Python things this program will use
#     # variables
#     # modules 
#     # methods
#     # loops (for loops, while loops)
#     # functions
#     # compairsons
#     # other shit

# # Program Code Actions  - Python FUNCTIONS are used for created ACTIONS
#     # import file of words from (word.txt)
#     # break down levels of difficulty based on word length 
#         # use if then to define short to long words
#             # create list of short words, medium, long words
#                 # list names defined with variables
#     # -- User intreaction
#         # tell user levels of difficituly (print command)
#         # ask user what level of difficulty to play
#             # user input level difficulty based on scale of 1-3
#         # Take user input from choice of 1 (easy,) 2, medium and 3 hard 
#     # GEnerate random word based on scael
#     # Program take input chooses random word from list of difficulty 
#     # -- User intreaction tell user how letters the word has referencing random word
#     # Program asks user to chooose single letter  (print)
#         # if user chooses 2 letter (PRINT - INvalid in put, choose one word, ask for another choice)
#         # take new letter and run code for that (IF ELSE CODE)
#     # Program - take user input of letter and evaluate if letter is in word
#         # Choosen letter not in word
#             #  IF LETTER IS NOT IN THE WORD the user  has lost a guess  *GUESS LOST*
#                 #  (PROGRAM will need to KEEPS TRACK of guess COUNT, use function maybe do this or list)
#             # LETTER ELIMINATED - letter no longer used - may need create LIST USED for that
#                      # create list of used elimated used letters
#              # PRINT take GUESS COUNT LIST and tell user how many guess so far (print) & 
#         # CHOOSEN LETTER IS IN WORD 
#             # Letter is in word -- no guess lost (do not add to count list)
#             # letter is in word  - # put letter in LETTER USED LIST
#             # TELL USER LETTER IS IN THE WORD (print)
#                 # --- CODE 
#                     # use underscore in place of letter would be
#                     # fill in letter for space it occupies in the word (USE FUNCTION)
#                         # function take letter guessed and return or else letter 
#                             # if user letter guess in word then RETURN in function created
#                             # ELSE if now letter not in word RETURN underscore
#         # take GUESS COUNT LIST and tell user how many guess so far (print) (include how many guesses left)

#         # ASK LETTER

guessed_letters = [] #just defined variable and will refence it later, can be empty
used_letters = []
allowed_guess = 8
 
# # Letter in word FUNCTION code thoughts
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
        return
        

# nameoflist.apppend(letter)


# #######
# # -- User intreaction
#         # tell user levels of difficituly (print command)
#         # ask user what level of difficulty to play
#             # user input level difficulty based on scale of 1-3
#         # Take user input from choice of 1 (easy,) 2, medium and 3 hard 


# ####

# #########
# #### FUTURE TO DO 
#     # tell user they have 8 guesses
#     # If a user enters more than one letter, tell them the input is invalid and let them try again.
        
 
#     # import file of letters 
# ##########################


# #1. At the start of the game, let the user know how many letters the computer's word contains.

# # 2. Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.

# # 3.Let the user know if their guess appears in the computer's word.

# # 4. Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen should display:

# # 5. B _ _ B A _ D
# # 6. A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.

# A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.

# If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.

# The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.

# When a game ends, ask the user if they want to play again. The game begins again if they reply positively.


# import random  #important is command

# alphabit = ["a","b","c"]  #define variable
# random_letter = random.choice(alphabit) 
 
