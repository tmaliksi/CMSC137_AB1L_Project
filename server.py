# import needed modules
import socket, sys, _thread

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print(addr, ' >> ', msg)
        msg = input('SERVER >> ')
        msg = bytes(msg,'utf-8')
		#Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.sendall(msg)
    clientsocket.close()

class Game:
    def main(self):
        menu_loop = True
        while menu_loop:
            print('=======================================\n')
            print('Welcome to 1-2-3 Pass!\n')
            print('1 - Start Server')
            print('2 - Instructions/Controls')
            print('3 - Game Description')
            print('4 - Quit')

            menu_option = input('\nEnter: ')
            print('\n=======================================')

            if menu_option == '1':
				#play_game()
                input('Enter any key to continue.')
                self.start_server()
            elif menu_option == '2':
				#play_multi()
                input('Enter any key to continue.')
                self.connect_to_server()
            elif menu_option == '3':
				#display_instructions()
                input('Enter any key to continue.')
            elif menu_option == '4':
				#print('Aww man...')
                menu_loop = False
            else:
                print('\nPlease choose a number.\n')

    def start_server(self):
        PORT = int(input("Enter port number: "))
        NUMBER_OF_PLAYERS = input(input("Enter number of players: "))

        print("Waiting for client on port "+str(PORT)+"...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        	# start connection using given porn
        	host = socket.gethostname()
        	s.bind((host,PORT))
        	# wait for client
        	s.listen(5)
        	# accept connection and assign to addr the ip address of client
        	# with conn:
        	while True:
        		conn, addr = s.accept()
        		# while(i != NUMBER_OF_PLAYERS):
        		# 	con, add = s.accept()
        		# 	conn.append(con)
        		# 	addr.append(add)
        		# 	i = i + 1
        		_thread.start_new_thread(on_new_client,(conn,addr))
        			# data = conn.recv(1024)
        			# if data != NULL, print the message then reverse
        			# if data:
        			# 	print("Message from client: "+data.decode('utf-8')+"\n")
        			# 	data = data[::-1]
        			# # if data is NULL, break
        			# elif not data:
        			# 	break
        			# # send the reversed string to client
        			# conn.sendall(data)
        		#close connection
        	conn.close()
        		# print("Client "+str(addr)+" closed the connection.")

game = Game()
game.main()
