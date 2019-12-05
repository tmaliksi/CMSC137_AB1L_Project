# import needed modules
import os, pickle, socket, sys

CARDS = []
isWIN = False
isEND = False

class Card:
	def __init__(self,card):
		if(len(card) > 2):
			self.value = card[0:2]
			self.suit = card[2]
		else:
			self.value = card[0]
			self.suit = card[1]

		if(self.suit == "C"):
			self.suit = '\N{BLACK CLUB SUIT}'
		elif(self.suit == "S"):
			self.suit = '\N{BLACK SPADE SUIT}'
		elif(self.suit == "H"):
			self.suit = '\N{BLACK HEART SUIT}'
		else:
			self.suit = '\N{BLACK DIAMOND SUIT}'

	def print(self):
		print('┌───────┐')
		print(f'| {self.value:<2}    |')
		print('|       |')
		print(f'|   {self.suit}   |')
		print('|       |')
		print(f'|    {self.value:>2} |')
		print('└───────┘')

class Game:
	def main(self):
		menu_loop = True
		while menu_loop:
			print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Menu: \n ")
			print(" [1] Connect to a server \n [2] Instructions/Controls \n [3] About the Game \n [4] Exit \n")
			menu_option = input('\n >>> Enter: ')
			print('\n -----------------------------------------------------------')

			if menu_option == '1':
					#play_game()
					self.connect_to_server()
			elif menu_option == '2':
					#game instructions
					self.display_instructions()
			elif menu_option == '3':
					#about the game
					self.display_description()
			elif menu_option == '4':
					#quit game
					menu_loop = False
			else:
					print('\n Please choose a number.\n')


	def display_instructions(self):
		print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Instructions: \n Each player will be dealt with 4 cards. Players will pass \n one card to their right until one of them gets four of a \n kind. The player who first gets a four of a kind will be \n declared the winner.\n\n -----------------------------------------------------------\n")

	def display_description(self):
	 print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")


	def connect_to_server(self):
		HOST = input(" Enter IP address of server: ")
		PORT = int(input(" Enter port number: "))
		global CARDS, isEND, isWIN

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST,PORT))
		name = input(" Enter your name: ")
		s.send(name.encode('utf-8'))
		while True:
			data = s.recv(5120)
			try:
				CARDS = pickle.loads(data)
			except pickle.UnpicklingError:
				if(data.decode('utf-8') == "WIN"):
					isWIN = True
				else:
					isWIN = False
				data = s.recv(4096)
				CARDS = pickle.loads(data)
				isEND = True

			if len(CARDS) == 4:
				try:
					os.system('clear')
				except:
					os.system('cls')

				for card in CARDS:
					card = CARDS.pop(0)
					CARDS.append(Card(card))

				print('┌───────┐	┌───────┐	┌───────┐	┌───────┐')
				print(f'| {CARDS[0].value:<2}    |	| {CARDS[1].value:<2}    |	| {CARDS[2].value:<2}    |	| {CARDS[3].value:<2}    |')
				print('|       |	|       |	|       |	|       |')
				print(f'|   {CARDS[0].suit}   |	|   {CARDS[1].suit}   |	|   {CARDS[2].suit}   |	|   {CARDS[3].suit}   |')
				print('|       |	|       |	|       |	|       |')
				print(f'|    {CARDS[0].value:>2} |	|    {CARDS[1].value:>2} |	|    {CARDS[2].value:>2} |	|    {CARDS[3].value:>2} |')
				print('└───────┘	└───────┘	└───────┘	└───────┘')
				print('    1    	    2    	    3    	    4    ')

				if(isEND):
					if(isWIN):
						print("You won!\n")
					else:
						print("You lose")
					break
				index = int(input("Enter number of card you wish to pass: "))
				cardToPass = str(index-1)
				s.send(cardToPass.encode('utf-8'))
		s.close()

game = Game()
game.main()
