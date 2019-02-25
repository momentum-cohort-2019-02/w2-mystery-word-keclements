word_to_guess = "racecar"
letters_guessed = []

def word_guessed(word_to_guess, letters_guessed):
	"""
	Given a word to guess and a list of of a if e letters currently guessed, return True ife all the letters in the word in the word have been guessed already.
	"""
	for letter in word_to_guess:
		if letter in letters_guessed: # if anything fails it fails the test
			return False
	return True


while not word_guessed(word_to_guess, letters_guessed)
	pass #doesn't do anything

# assert - doesn't do anything unless what comes after it is not true
# aert doe sthinking if it is trtue

if __name__ == ""__main__""