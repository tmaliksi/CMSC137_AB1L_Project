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
        self.score = 0
        print("New connection added: ", clientAddress)

    def giveCards(self, card):
        self.clientSocket.send(card.encode())
        data = self.clientSocket.recv(1024)
        if data.decode('utf-8') != "OK":
            self.clientSocket.send(card.encode())
    def getCards(self):
        global CARDS
        card = self.clientSocket.recv(1024)
        CARDS.insert(0,card.decode("utf-8"))
    def passCard(self,client):
        global CARDS
        index = len(CARDS) - 1
        card = CARDS.pop(index)
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
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = int(input(" Enter port number: "))
        NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))
        global CLIENTS
        global SUITS, CARDS
        NUMBERS= list(range(1,NUMBER_OF_PLAYERS+1))
        for number in NUMBERS:
            for suit in SUITS:
                CARDS.append(str(number)+suit)

        while NUMBER_OF_PLAYERS <= 2 or NUMBER_OF_PLAYERS > 13:
            print(" Minimum number of players is 3 and maximum number of players is 13")
            NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # host = "192.168.1.20"
        s.bind((HOST,PORT))
        s.listen(1)
        for i in range(NUMBER_OF_PLAYERS):
            print(" Waiting for "+str(NUMBER_OF_PLAYERS - len(CLIENTS))+" client/s on port "+str(PORT)+"...")
            clientSocket, clientAddress = s.accept()
            CLIENTS.append(ClientThread(clientSocket,clientAddress))
        while len(CARDS) != 0:
            for client in CLIENTS:
                index = random.randint(0,len(CARDS)-1)
                card = CARDS.pop(index)
                client.giveCards(card)
        while True:
            for client in CLIENTS:
                client.getCards()
            if(len(CARDS) == NUMBER_OF_PLAYERS):
                for i in range(len(CLIENTS)):
                    if(i == len(CLIENTS)-1):
                        CLIENTS[i].passCard(CLIENTS[0])
                    else:
                        CLIENTS[i].passCard(CLIENTS[i+1])


    def game_instructions(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Instructions: \n Each player will be dealt with 4 cards. Players will pass \n one card to their right until one of them gets four of a \n kind. The player who first gets a four of a kind will be \n declared the winner.\n\n -----------------------------------------------------------\n")

    def about_the_game(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")

game = Game()
game.main()
