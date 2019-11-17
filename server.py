# import needed modules
import socket, sys, _thread, threading

message = "Hi!"

class ClientThread(threading.Thread):
    def __init__(self,clientSocket,clientAddress):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientAddress = clientAddress
        print("New connection added: ", clientAddress)

    def run(self):
        # print("Connection from :", self.clientAddress)
        global message
        msg = self.clientSocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print(self.clientAddress, ' >> ', msg)
    	#Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        self.clientSocket.send(bytes(message,'utf-8'))

# def on_new_client(clientsocket,addr):
#     while True:
#         msg = clientsocket.recv(1024)
#         #do some checks and if msg == someWeirdSignal: break:
#         print(addr, ' >> ', msg)
#         msg = input('SERVER >> ')
#         msg = bytes(msg,'utf-8')
# 		#Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
#         clientsocket.sendall(msg)
#     clientsocket.close()

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
                input('Enter any key to continue.\n')
                self.start_server()
            elif menu_option == '2':
				#play_multi()
                input('Enter any key to continue.\n')
                self.connect_to_server()
            elif menu_option == '3':
				#display_instructions()
                input('Enter any key to continue.\n')
            elif menu_option == '4':
				#print('Aww man...')
                menu_loop = False
            else:
                print('\nPlease choose a number.\n')

    def start_server(self):
        PORT = int(input("Enter port number: "))
        NUMBER_OF_PLAYERS = int(input("Enter number of players: "))
        CLIENTS = []
        while NUMBER_OF_PLAYERS <= 2:
            print("Minimum number of players is 3")
            NUMBER_OF_PLAYERS = int(input("Enter number of players: "))

        print("Waiting for "+str(NUMBER_OF_PLAYERS)+" clients on port "+str(PORT)+"...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # start connection using given port
        host = socket.gethostname()
        s.bind((host,PORT))
        # wait for client
        s.listen(5)
        for i in range(NUMBER_OF_PLAYERS):
            clientSocket, clientAddress = s.accept()
            CLIENTS.append(ClientThread(clientSocket,clientAddress))
        while True:
            global message
            message = input("Enter message: ")
            for client in CLIENTS:
                client.run()
        # accept connection and assign to addr the ip address of client
        # with conn:
        # addresses = []
        # connections = []
        # i = 0
        # while True:
        #     while i != NUMBER_OF_PLAYERS:
        #         conn, addr = s.accept()
        #         addresses.append(addr)
        #         connections.append(conn)
        #         i += 1
        #     for i in range(NUMBER_OF_PLAYERS):
        #         _thread.start_new_thread(on_new_client,(connections[i],addresses[i]))
game = Game()
game.main()
