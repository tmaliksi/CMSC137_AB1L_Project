# import needed modules
import random, socket, sys, threading

SUITS = ["C","S","H","D"]
CARDS = []
CLIENTS = []

class ClientThread(threading.Thread):
    def __init__(self,clientSocket,clientAddress):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientAddress = clientAddress
        print("New connection added: ", clientAddress)

    def giveCards(self, card):
        # print("Connection from :", self.clientAddress)
        # msg = self.clientSocket.recv(1024)
        # #do some checks and if msg == someWeirdSignal: break:
        # print(self.clientAddress, ' >> ', msg)
        # CARDS.append(msg.decode("utf-8"))
    	#Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        self.clientSocket.send(bytes(card,'utf-8'))
    def getCards(self):
        global CARDS
        card = self.clientSocket.recv(1024)
        CARDS.append(card.decode("utf-8"))
    def passCard(self,client):
        global CARDS
        index = len(CARDS) - 1
        card = CARDS[index]
        del CARDS[index]
        client.giveCards(card)


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
        global CLIENTS
        global SUITS, CARDS
        NUMBERS= list(range(1,NUMBER_OF_PLAYERS+1))
        for number in NUMBERS:
            for suit in SUITS:
                CARDS.append(str(number)+suit)
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
            if len(CARDS) != 0:
                for client in CLIENTS:
                    index = random.randint(0,len(CARDS)-1)
                    card = CARDS[index]
                    del CARDS[index]
                    client.giveCards(card)
            else:
                break
        while True:
            for client in CLIENTS:
                client.getCards()
            if(len(CARDS) == NUMBER_OF_PLAYERS):
                for i in range(len(CLIENTS)):
                    if(i == 0):
                        CLIENTS[i].passCard(CLIENTS[0])
                    else:
                        CLIENTS[i].passCard(CLIENTS[i+1])
game = Game()
game.main()
