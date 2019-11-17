# import needed modules
import os, socket, sys

CARDS = []

class Game:
	def main(self):
		menu_loop = True
		while menu_loop:
			print('=======================================\n')
			print('Welcome to 1-2-3 Pass!\n')
			print('1 - Play Solo Game')
			print('2 - Play Multiplayer')
			print('3 - Instructions/Controls')
			print('4 - Game Description')
			print('5 - Quit')

			menu_option = input('\nEnter: ')

			print('\n=======================================')

			if menu_option == '1':
				#play_game()
				input('Enter any key to continue.\n')
			elif menu_option == '2':
				#play_multi()
				input('Enter any key to continue.\n')
				self.connect_to_server()
			elif menu_option == '3':
				#display_instructions()
				input('Enter any key to continue.\n')
			elif menu_option == '4':
				#display_description()
				input('Enter any key to continue.\n')
			elif menu_option == '5':
				#print('Aww man...')
				menu_loop = False
			else:
				print('\nPlease choose a number.\n')


	def display_instructions():
		print('=======================================')
		print('             INSTRUCTIONS              ')
		print('=======================================')

		print('\ninstructions here\n')

	def display_description():
		print('=======================================')
		print('             DESCRIPTION               ')
		print('=======================================')

		print('\ndescription here\n')

	def connect_to_server(self):
		HOST = input("Enter hostname: ")
		PORT = int(input("Enter port number: "))
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
				index = int(input("Enter number of card you wish to pass: "))
				cardToPass = CARDS[index-1]
				print(cardToPass)
				del CARDS[index-1]
				s.send(cardToPass.encode('utf-8'))
		s.close()

game = Game()
game.main()
