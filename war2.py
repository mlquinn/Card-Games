"""
			WAR!
	WAR is a simple card game where each player gets half of a deck of
	52 cards and draws from the top of the deck and compare cards. 
	The player with the highest value card wins the round and then adds 
	the other players card to their deck. The first player to collect 
	all the cards wins!
	
@author Michael Quinn
@date November 19, 2018
@version 0.2
"""
import random
import sys
import clearConsole

def createDeck():
	suites = ["spade","heart","club","diamond"]
	faces = [2,3,4,5,6,7,8,9,10,11,12,13,14]
	deck = []
	for suit in suites:
		for face in faces:
			deck.append(face)
	random.shuffle(deck)
	return deck

def printCards(card1, card2):
	if (card1 in range(11,15)):
		if (card1 == 11):
			card1 = "J"
		elif (card1 == 12):
			card1 = "Q"
		elif (card1 == 13):
			card1 = "K"
		elif (card1 == 14):
			card1 = "A"
	if card2 in range(11,15):
		if (card2 == 11):
			card2 = "J"
		elif (card2 == 12):
			card2 = "Q"
		elif (card2 == 13):
			card2 = "K"
		elif (card2 == 14):
			card2 = "A"
	print("Player 1: " + str(card1) + "\nPlayer 2: " + str(card2))
			
def play_game(deck):
	aDeck = deck[:int(len(deck)/2)]
	bDeck = deck[int(len(deck)/2):]
	aStash = []
	bStash = []
	
	round = 1
	while aDeck and bDeck:
		clearConsole.clear()
		aCard = aDeck.pop()
		bCard = bDeck.pop()
		printCards(aCard,bCard)
		
		if aCard == bCard:
			aStash.extend([aCard]+aDeck[-3:]) #Burn 3 cards to the stash pile
			aDeck = aDeck[:-3] 
			aDeck.append(aStash.pop()) #'flip' 3rd burn card for play
			print("WAR!\nBurn three cards...")
			bStash.extend([bCard]+bDeck[-3:]) #Burn 3 cards to the stash pile
			bDeck = bDeck[:-3] 
			bDeck.append(bStash.pop()) #'flip' 3rd burn card for play
		elif aCard > bCard:
			print("Player 1 wins!")
			aDeck = [aCard, bCard] + aStash + bStash + aDeck
			aStash = []
			bStash = []
		elif aCard < bCard:
			print("Player 2 wins!")
			bDeck = [aCard, bCard] + aStash + bStash + bDeck
			aStash = []
			bStash = []
		
		print("End round {}, deck 1 has {} cards and deck 2 has {} cards".format(round,len(aDeck),len(bDeck)))
		round += 1
		if round == 10000:
			print("Game ended, out of time! You are very unlucky.")
		if (input(">Enter to draw again, Q to quit.\n").strip().lower() == 'q'):
			print("You surrendered!")
			break
		
	
if __name__ == "__main__":
	play = ""
	print("Welcome to the game of WAR!")
	while True:
		try:
			while play == "":
				play = input("Ready to begin? y/n: ").strip().lower()
			if play == 'y':
				deck = createDeck()
				play_game(deck)
			elif play == 'n':
				print("Goodbye.")
				sys.exit()
			play = ""
		except IOError as e:
			e.printstackTrace()
				
