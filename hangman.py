import random


#global var wordbank includes words that can be used for this game in 1-P mode. 
#Initially this includes words inspired by my environment (i.e. an airplane)
#Users can append further words.
wordbank = ["Airport", "Acquitted", "Attorney", "Dancer", "Luggage", "Dream", "Coverage",
			"Sattelite", "Norwegian", "Acclaimed", "Peloton", "Shapeshifter", "Depression",
			"Slipstream", "Cloud", "Teeth", "Commander", "Prophecy", "Spaceship"]

def select_word():
	ind = random.randrange(0, len(wordbank)-1)
	return wordbank[ind]

def number_of_players():
	players = input("Enter 1 for a 1P game, 2 for a 2P game. Enter Q to quit:\n")

	if isinstance(players, int):
		if players != 1 and players != 2:
			print("unexpected value for number of players!\n")
		else:
			return players	
	# elif isinstance(players, str):
	# 	if players.upper() == "Q":
	# 		return exit

def new_game():

	players = number_of_players()

	if players == 1:
		word_to_use = select_word()
	elif players == 2:
		word_to_use = str(input("enter the word to use!\n"))



##Run game
def __main__():
	new_game()	

__main__()	