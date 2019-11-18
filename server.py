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
            print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Menu: \n ")
            print(" [1] Start Server \n [2] Instructions/Controls \n [3] About the Game \n [4] Exit \n")
            menu_option = input('\n >>> Enter: ')
            print('\n -----------------------------------------------------------')

            if menu_option == '1':
                #play_game()
                self.start_server()
            elif menu_option == '2':
                #game instructions
                self.game_instructions()
            elif menu_option == '3':
                #about the game
                self.about_the_game()
            elif menu_option == '4':
                #quit game
                menu_loop = False
            else:
                print('\n Please choose a number.\n')

    def start_server(self):
        PORT = int(input(" Enter port number: "))
        NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))
        global CLIENTS
        global SUITS, CARDS
        NUMBERS= list(range(1,NUMBER_OF_PLAYERS+1))
        for number in NUMBERS:
            for suit in SUITS:
                CARDS.append(str(number)+suit)
        while NUMBER_OF_PLAYERS <= 2:
            print(" Minimum number of players is 3")
            NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))

        print(" Waiting for "+str(NUMBER_OF_PLAYERS)+" clients on port "+str(PORT)+"...")
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

    def game_instructions(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Instructions: \n Each player will be dealt with 4 cards. Players will pass \n one card to their right until one of them gets four of a \n kind. The player who first gets a four of a kind will be \n declared the winner.\n\n -----------------------------------------------------------\n")	

    def about_the_game(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")

game = Game()
game.main()
