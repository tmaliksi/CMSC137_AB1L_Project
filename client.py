# import needed modules
import socket, sys

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
				input('Press enter to continue.')
			elif menu_option == '2':
				#play_multi()
				input('Press enter to continue.')
				self.connect_to_server()
			elif menu_option == '3':
				#display_instructions()
				input('Press enter to continue.')
			elif menu_option == '4':
				#display_description()
				input('Press enter to continue.')
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
		MESSAGE = str.encode(sys.argv[3])

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			# connect to user-given host and port
			s.connect((HOST,PORT))
			# send user-given message
			s.sendall(MESSAGE)
			# receive from server
			data = s.recv(1024)
			# close connection
			s.close()

		# print message from server
		print("\nMessage from server: "+data.decode("utf-8")+"\n")

game = Game()
game.main()
