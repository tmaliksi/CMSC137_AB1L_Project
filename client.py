# import needed modules
import os, pickle, socket, sys

CARDS = []
isEND = False

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

	def display_description(self):
		print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")

	def tutorial_demo(self):
		tutorial_loop = True
		while tutorial_loop:
			print("-------------Welcome to the 1-2-3 Pass Tutorial-------------")
			print("1) To start, you will be given 4 random cards, like what you see below")
			DEMO_CARDS = ("1 of Spades", "1 of Hearts", "1 of Diamonds", "1 of Clubs", "3 of Hearts", "King of Spades")
			print("Card List: \n", 
				"1 : ", DEMO_CARDS[0], "\n",
				"2 : ", DEMO_CARDS[1], "\n",
				"3 : ", DEMO_CARDS[2], "\n",
				"4 : ", DEMO_CARDS[5], "\n")
			tutorial_option = input('\nEnter 1 to continue, 2 to exit to menu: ')

			if tutorial_option == '1':
				print("Now we move onto passing cards! \nTo pass a card, simply type in the number corresponding said card.")
				print("Card List: \n", 
				"1 : ", DEMO_CARDS[0], "\n",
				"2 : ", DEMO_CARDS[1], "\n",
				"3 : ", DEMO_CARDS[2], "\n",
				"4 : ", DEMO_CARDS[5], "\n")
				pass_option = input("For example, let us pass the King of Spades, so press 4 to pass: ") 
				
				if pass_option == '4':
					print("Card List: \n", 
					"1 : ", DEMO_CARDS[0], "\n",
					"2 : ", DEMO_CARDS[1], "\n",
					"3 : ", DEMO_CARDS[2], "\n",
					"4 : ", DEMO_CARDS[4], "\n")
					print("Great! We passed the card! And we received a different card of 3 of Hearts!")
					pass2_option = input("But we need a full suit to win the game so we shall pass a card again. Type in 4: ")

					if pass2_option == '4':
						print("Card List: \n", 
						"1 : ", DEMO_CARDS[0], "\n",
						"2 : ", DEMO_CARDS[1], "\n",
						"3 : ", DEMO_CARDS[2], "\n",
						"4 : ", DEMO_CARDS[3], "\n")
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
		# HOST = input(" Enter IP address of server: ")
		# PORT = int(input(" Enter port number: "))
		HOST = socket.gethostbyname(socket.gethostname())
		PORT = 8081
		global CARDS, isEND

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST,PORT))
		while True:
			data = s.recv(4096)
			# if data:
			# 	s.send(b"OK")
			try:
				CARDS = pickle.loads(data)
			except pickle.UnpicklingError:
				if(data.decode('utf-8') == "WIN"):
					print("You won!")
				else:
					print("You lose")
				data = s.recv(4096)
				CARDS = pickle.loads(data)
				isEND = True
			# CARDS.append(data.decode("utf-8"))

			if len(CARDS) == 4:
				os.system('clear')
				for i in range(4):
					if(len(CARDS[i]) > 2):
						if(CARDS[i][0:1] == "10"):
							print(str(i+1), ": ", CARDS[i][0:1], end="")
						elif(CARDS[i][0:1] == "11"):
							print(str(i+1), ": Jack", end="")
						elif(CARDS[i][0:1] == "12"):
							print(str(i+1), ": Queen", end="")
						elif(CARDS[i][0:1] == "13"):
							print(str(i+1), ": King", end="")
					elif(CARDS[i][0] == "1"):
						print(str(i+1), ": Ace", end="")
					else:
						print(str(i+1), ": ", CARDS[i][0], end="")
					suit = CARDS[i][len(CARDS[i])-1]
					if suit == "C":
						print(" of Clubs")
					elif suit == "S":
						print(" of Spades")
					elif suit == "H":
						print(" of Hearts")
					else:
						print(" of Diamonds")

				if(len(CARDS[0]) > 2):
					kind = CARDS[0][0:1]
				else:
					kind = CARDS[0][0]
				if(isEND):
					break
				index = int(input("Enter number of card you wish to pass: "))
				cardToPass = str(index-1)
				s.send(cardToPass.encode('utf-8'))
		s.close()

game = Game()
game.main()
