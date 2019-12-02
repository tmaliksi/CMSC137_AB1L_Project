# import needed modules
import os, socket, sys

CARDS = []

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
		# HOST = "192.168.1.20"
		# PORT = 8080
		global CARDS

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST,PORT))
		while True:
			while len(CARDS) != 4:
				data = s.recv(1024)
				if data:
					s.send(b"OK")
				CARDS.append(data.decode("utf-8"))
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

				index = int(input("Enter number of card you wish to pass: "))
				cardToPass = CARDS.pop(index-1)
				s.send(cardToPass.encode('utf-8'))
		s.close()

game = Game()
game.main()
