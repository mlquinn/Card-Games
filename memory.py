"""
			Memory!
	Choose hidden cards to find pairs to score points.
	Player with the most points wins!
@author Michael Quinn
@date  Novemver 21, 2018
@version 0.1
"""

import random
import clearConsole
import array
import time

def generateDeck():
	deck = []
	suits = ["H","D","C","S"]
	faces = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
	for suit in suits:
		for face in faces:
			deck.append((face))
	random.shuffle(deck)
	return deck
def displayCards(deck):
	x = 1
	for x in range(1,len(deck) + 1):
		if str(deck[x-1]) == "X ":
			print("{:2s}".format(str(deck[x-1])),end="")
		else:
			print("{:2d} ".format(x), end="")
		if x % 13 == 0:
			print()

def winGraphic():
	i=0
	for i in range(0,3): 
		clearConsole.clear()
		time.sleep(0.5)
		print("""
		@     @   @@    @      @    @         @         @  @  @@     @  @@@@@@@  @@@@@@@  @@@@@@@
		 @   @   @  @   @      @     @       @ @       @      @ @    @   @   @    @   @    @   @
		  @ @   @    @  @      @      @     @   @     @    @  @  @   @    @ @      @ @      @ @
		   @    @    @   @    @        @   @     @   @     @  @   @  @     @        @        @
		   @     @  @     @  @          @ @       @ @      @  @    @ @  
		   @      @@       @@            @         @       @  @     @@     @        @        @""")
		time.sleep(0.5)
	print("Nice job!")

def play_Memory(deck, mode):
	matchedPairs = 0
	clearConsole.clear()
	while True:
		displayCards(deck)
		print("Current score: {:d}".format(matchedPairs))
		try:
			card1 = int(input("Please enter first card position: ").strip())
			card2 = int(input("Please enter second card position: ").strip())
			if mode == 'h' or mode == 'hard':
				clearConsole.clear()
			print("Card at position {} is {}.\nCard at position {} is {}.".format(str(card1),str(deck[card1 -1]),str(card2),str(deck[card2-1])))
			if ((card1 and card2 < 53 ) and (card1 and card2 > 0)):
				if deck[int(card1) - 1] == deck[int(card2) - 1]:
					deck[card1-1] ="X "
					deck[card2-1] = "X "
					matchedPairs += 1
					print("Card match!")
					if matchedPairs >= 26:
						winGraphic()
						break;
				else:
					print("No match.")
			else:
				raise ValueError
		except ValueError:
			print("\tERROR: Please enter an integer between 1 and 52.")
if __name__ == "__main__":
	while True:
		play = ""
		while play =="":
			play = input("Ready to play Memory?(y/n) ").strip().lower()
		if play == "y":
			mode = ""
			while mode == "":
				mode = input("Select dificulty: {E}asy or {H}ard? ").strip().lower()
			deck = generateDeck()
			play_Memory(deck, mode)
		elif play == "n":
			print("Goodbye.")
			break;
		else:
			print("Please enter 'y' or 'n'.")
