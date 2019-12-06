# import needed modules
import os, pickle, socket, struct, sys

# initialize required variables
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

		if(self.value == "1"):
			self.value = "A"
		elif(self.value == "11"):
			self.value = "J"
		elif(self.value == "12"):
			self.value = "Q"
		elif(self.value == "13"):
			self.value = "K"

		if(self.suit == "C"):
			self.suit = '\N{BLACK CLUB SUIT}'
		elif(self.suit == "S"):
			self.suit = '\N{BLACK SPADE SUIT}'
		elif(self.suit == "H"):
			self.suit = '\N{BLACK HEART SUIT}'
		else:
			self.suit = '\N{BLACK DIAMOND SUIT}'

class Game:
	def main(self):
		menu_loop = True
		while menu_loop:
			print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Menu: \n ")
			print(" [1] Connect to a server \n [2] Tutorial Game \n [3] Instructions/Controls \n [4] About the Game \n [5] Exit \n")
			menu_option = input('\n >>> Enter: ')
			print('\n -----------------------------------------------------------')

			if menu_option == '1':
					#play_game()
					self.connect_to_server()
			elif menu_option == "2":
					#play_tutorial()
					self.tutorial_demo()
			elif menu_option == '3':
					#game instructions
					self.display_instructions()
			elif menu_option == '4':
					#about the game
					self.display_description()
			elif menu_option == '5':
					#quit game
					menu_loop = False
			else:
					print('\n Please choose a number.\n')


	def display_instructions(self):
		print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Instructions: \n Each player will be dealt with 4 cards. Players will pass \n one card to their right until one of them gets four of a \n kind. The player who first gets a four of a kind will be \n declared the winner.\n\n -----------------------------------------------------------\n")
		input(" Enter any key to continue...")

	def display_description(self):
		print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")
		input(" Enter any key to continue...")

	def tutorial_demo(self):
		tutorial_loop = True
		while tutorial_loop:
			print("-------------Welcome to the 1-2-3 Pass Tutorial-------------")
			print("1) To start, you will be given 4 random cards, like what you see below")
			DEMO_CARDS = (Card("1S"), Card("1H"), Card("1D"), Card("1C"), Card("3H"), Card("13K"))
			print("Card List: ")
			print('┌───────┐	┌───────┐	┌───────┐	┌───────┐')
			print(f'| {DEMO_CARDS[0].value:<2}    |	| {DEMO_CARDS[1].value:<2}    |	| {DEMO_CARDS[2].value:<2}    |	| {DEMO_CARDS[5].value:<2}    |')
			print('|       |	|       |	|       |	|       |')
			print(f'|   {DEMO_CARDS[0].suit}   |	|   {DEMO_CARDS[1].suit}   |	|   {DEMO_CARDS[2].suit}   |	|   {DEMO_CARDS[5].suit}   |')
			print('|       |	|       |	|       |	|       |')
			print(f'|    {DEMO_CARDS[0].value:>2} |	|    {DEMO_CARDS[1].value:>2} |	|    {DEMO_CARDS[2].value:>2} |	|    {DEMO_CARDS[5].value:>2} |')
			print('└───────┘	└───────┘	└───────┘	└───────┘')
			print('    1    	    2    	    3    	    4    ')
			tutorial_option = input('\nEnter 1 to continue, 2 to exit to menu: ')

			if tutorial_option == '1':
				print("Now we move onto passing cards! \nTo pass a card, simply type in the number corresponding said card.")
				print("Card List: ")
				print('┌───────┐	┌───────┐	┌───────┐	┌───────┐')
				print(f'| {DEMO_CARDS[0].value:<2}    |	| {DEMO_CARDS[1].value:<2}    |	| {DEMO_CARDS[2].value:<2}    |	| {DEMO_CARDS[5].value:<2}    |')
				print('|       |	|       |	|       |	|       |')
				print(f'|   {DEMO_CARDS[0].suit}   |	|   {DEMO_CARDS[1].suit}   |	|   {DEMO_CARDS[2].suit}   |	|   {DEMO_CARDS[5].suit}   |')
				print('|       |	|       |	|       |	|       |')
				print(f'|    {DEMO_CARDS[0].value:>2} |	|    {DEMO_CARDS[1].value:>2} |	|    {DEMO_CARDS[2].value:>2} |	|    {DEMO_CARDS[5].value:>2} |')
				print('└───────┘	└───────┘	└───────┘	└───────┘')
				print('    1    	    2    	    3    	    4    ')
				pass_option = input("For example, let us pass the King of Spades, so press 4 to pass: ")

				if pass_option == '4':
					print("Card List: ")
					print('┌───────┐	┌───────┐	┌───────┐	┌───────┐')
					print(f'| {DEMO_CARDS[0].value:<2}    |	| {DEMO_CARDS[1].value:<2}    |	| {DEMO_CARDS[2].value:<2}    |	| {DEMO_CARDS[4].value:<2}    |')
					print('|       |	|       |	|       |	|       |')
					print(f'|   {DEMO_CARDS[0].suit}   |	|   {DEMO_CARDS[1].suit}   |	|   {DEMO_CARDS[2].suit}   |	|   {DEMO_CARDS[4].suit}   |')
					print('|       |	|       |	|       |	|       |')
					print(f'|    {DEMO_CARDS[0].value:>2} |	|    {DEMO_CARDS[1].value:>2} |	|    {DEMO_CARDS[2].value:>2} |	|    {DEMO_CARDS[4].value:>2} |')
					print('└───────┘	└───────┘	└───────┘	└───────┘')
					print('    1    	    2    	    3    	    4    ')
					print("Great! We passed the card! And we received a different card of 3 of Hearts!")
					pass2_option = input("But we need a full suit to win the game so we shall pass a card again. Type in 4: ")

					if pass2_option == '4':
						print("Card List: ")
						print('┌───────┐	┌───────┐	┌───────┐	┌───────┐')
						print(f'| {DEMO_CARDS[0].value:<2}    |	| {DEMO_CARDS[1].value:<2}    |	| {DEMO_CARDS[2].value:<2}    |	| {DEMO_CARDS[3].value:<2}    |')
						print('|       |	|       |	|       |	|       |')
						print(f'|   {DEMO_CARDS[0].suit}   |	|   {DEMO_CARDS[1].suit}   |	|   {DEMO_CARDS[2].suit}   |	|   {DEMO_CARDS[3].suit}   |')
						print('|       |	|       |	|       |	|       |')
						print(f'|    {DEMO_CARDS[0].value:>2} |	|    {DEMO_CARDS[1].value:>2} |	|    {DEMO_CARDS[2].value:>2} |	|    {DEMO_CARDS[3].value:>2} |')
						print('└───────┘	└───────┘	└───────┘	└───────┘')
						print('    1    	    2    	    3    	    4    ')
						print("We passed the card and received a 1 of Clubs!")
						back_option = input("You have won the game! Please type in 1 to go back menu: ")

						if back_option == '1':
							break
						else:
							print("\nPlease type 1!\n")
					else:
						print("\nPlease type in 4!")
				else:
					print('\nPlease type in 4!\n')
			elif tutorial_option == '2':
				break
			else:
				print("\nPlease input an option!\n")

	def connect_to_server(self):
		HOST = input(" Enter IP address of server: ")
		# HOST = "192.168.1.20"
		PORT = int(input(" Enter port number: "))
		# PORT = 8081

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect((HOST,PORT))
		except:
			print(f"\n Server in {HOST}:{PORT} not yet started!\n")
			input(" Enter any key to return to menu...")
			return
		name = input(" Enter your name: ")
		s.send(name.encode('utf-8'))
		self.start_game(s)
	def start_game(self,s):
		global CARDS, isEND, isWIN
		CARDS = []
		isEND = False
		isWIN = False
		while True:
			buf = b''
			while len(buf) < 4:
				buf += s.recv(4-len(buf))
			length = struct.unpack('!I', buf)[0]
			data = pickle.loads(s.recv(length))
			if(isinstance(data,list)):
				CARDS = data
			else:
				if(data == "WIN"):
					isWIN = True
				elif(data == "LOSE"):
					isWIN = False
				buf = b''
				while len(buf) < 4:
					buf += s.recv(4-len(buf))
				length = struct.unpack('!I', buf)[0]
				CARDS = pickle.loads(s.recv(length))
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
						input(" You got four-of-a-kind! Enter any key quickly...")
						break
					else:
						input(" Another player has won. Enter any key to continue...")
						break
				while True:
					try:
						index = int(input("Enter number of card you wish to pass: "))
						while(index > 4):
							print("\nInput not valid!\n")
							index = int(input("Enter number of card you wish to pass: "))
						break
					except:
						print("\nInput not valid!\n")

				cardToPass = str(index-1)
				s.send(cardToPass.encode('utf-8'))
		buf = b''
		while len(buf) < 4:
			buf += s.recv(4-len(buf))
		length = struct.unpack('!I', buf)[0]
		scores = pickle.loads(s.recv(length))
		print("==============SCOREBOARD=============")
		for name, val in scores.items():
			print(f"||        {name} =  {val}	    	||")
		print("=====================================")
		while True:
			try:
				print("Do you want to play again? ")
				choice = int(input(" [1] Yes or [2] No  >>"))
				break
			except:
				print("\nInput not valid!\n")
		if(choice == 1):
			print("Waiting for other players...")
			s.send(b'Y')
			if(s.recv(1024).decode('utf-8') == 'N'):
				print("Goodbye")
			else:
				self.start_game(s)
		elif(choice == 2):
			print("Goodbye")
			s.send(b'N')
		s.close()

game = Game()
game.main()
