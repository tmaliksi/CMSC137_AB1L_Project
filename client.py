# import needed modules
import os, socket, sys

CARDS = []

class Game:
	def main(self):
		menu_loop = True
		while menu_loop:
			print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Menu: \n ")
			print(" [1] Start Server \n [2] Instructions/Controls \n [3] About the Game \n [4] Exit \n")
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
		HOST = input(" Enter hostname: ")
		PORT = int(input(" Enter port number: "))
		global CARDS

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST,PORT))
		while True:
			# connect to user-given host and port
			# receive from server
			while len(CARDS) != 4:
				data = s.recv(1024)
				CARDS.append(data.decode("utf-8"))
			if len(CARDS) == 4:
				os.system('clear')
				for i in range(4):
					print(str(i+1)," ",CARDS[i])
				index = int(input(" Enter number of card you wish to pass: "))
				cardToPass = CARDS[index-1]
				print(cardToPass)
				del CARDS[index-1]
				s.send(cardToPass.encode('utf-8'))
		s.close()

game = Game()
game.main()
