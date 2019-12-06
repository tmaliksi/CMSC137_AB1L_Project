# import needed modules
import pickle, random, socket, struct, sys, threading

SUITS = ["C","S","H","D"]
CARDS = []
CLIENTS = []
isEND = False
HOST = 0
PORT = 0
NUMBER_OF_PLAYERS = 0

class ClientThread(threading.Thread):
    def __init__(self,clientSocket,clientAddress):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientAddress = clientAddress
        self.score = 0
        self.clientCards = []
        self.isWinner = False
        self.name = clientSocket.recv(1024).decode('utf-8')
        print("New connection added: ", clientAddress)

    def getCards(self):
        global CARDS
        card = self.clientSocket.recv(1024)
        print(card.decode("utf-8"))
        CARDS.insert(0,self.clientCards.pop(int(card.decode("utf-8"))))

    def passCard(self,client):
        global CARDS
        index = len(CARDS) - 1
        card = CARDS.pop(index)
        client.clientCards.append(card)

    def showAllCards(self):
        print(self.clientCards)

    def checkIfComplete(self):
        if(len(self.clientCards[0]) > 2):
            kind = self.clientCards[0][0:2]
        else:
            kind = self.clientCards[0][0]
        for card in self.clientCards[1:4]:
            if(len(self.clientCards[0]) > 2):
                if(kind != card[0:1]):
                    return False
            else:
                if(kind != card[0]):
                    return False
        self.isWinner = True
        self.score += 1
        return True

class Game:
    def display_description(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")
        input(" Enter any key to continue...")

    def main(self):
        menu_loop = True
        while menu_loop:
            print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Menu: \n ")
            print(" [1] Start Server \n [2] About the Game \n [3] Exit \n")
            menu_option = input('\n >>> Enter: ')
            print('\n -----------------------------------------------------------')

            if menu_option == '1':
                #play_game()
                self.start_server()
                self.start_game()
            elif menu_option == '2':
                #about the game
                self.display_description()
            elif menu_option == '3':
                #quit game
                menu_loop = False
            else:
                print('\n Please choose a number.\n')

    def start_server(self):
        global CLIENTS, SUITS, CARDS, isEND, HOST, PORT, NUMBER_OF_PLAYERS
        HOST = input(" Enter IP address: ")
        PORT = int(input(" Enter port number: "))
        NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))

        while NUMBER_OF_PLAYERS <= 2 or NUMBER_OF_PLAYERS > 13:
            print(" Minimum number of players is 3 and maximum number of players is 13")
            NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                s.bind((HOST,PORT))
                break
            except:
                print("Invalid port.")
                PORT = int(input(" Enter port number: "))
        s.listen(1)
        for i in range(NUMBER_OF_PLAYERS):
            print(" Waiting for "+str(NUMBER_OF_PLAYERS - len(CLIENTS))+" client/s on port "+str(PORT)+"...")
            clientSocket, clientAddress = s.accept()
            CLIENTS.append(ClientThread(clientSocket,clientAddress))

    def start_game(self):
        global CLIENTS, SUITS, CARDS, isEND, NUMBER_OF_PLAYERS
        for client in CLIENTS:
            client.clientCards = []
            client.isWinner = False
        isEND = False
        NUMBERS = list(range(1,NUMBER_OF_PLAYERS+1))
        for number in NUMBERS:
            for suit in SUITS:
                CARDS.append(str(number)+suit)

        while len(CARDS) != 0:
            for client in CLIENTS:
                index = random.randint(0,len(CARDS)-1)
                card = CARDS.pop(index)
                client.clientCards.append(card)
        while True:
            for client in CLIENTS:
                isEND = client.checkIfComplete()
            if(isEND):
                for client in CLIENTS:
                    if(client.isWinner):
                        packet = pickle.dumps("WIN")
                        length = struct.pack('!I', len(packet))
                        packet = length + packet
                        client.clientSocket.send(packet)
                    else:
                        packet = pickle.dumps("LOSE")
                        length = struct.pack('!I', len(packet))
                        packet = length + packet
                        client.clientSocket.send(packet)
            for client in CLIENTS:
                packet = pickle.dumps(client.clientCards)
                length = struct.pack('!I', len(packet))
                packet = length + packet
                client.clientSocket.send(packet)
            for client in CLIENTS:
                print("Client "+client.name+" has " + str(client.clientCards))
            if(isEND):
                break
            for client in CLIENTS:
                client.getCards()
            if(len(CARDS) == NUMBER_OF_PLAYERS):
                for i in range(len(CLIENTS)):
                    if(i == len(CLIENTS)-1):
                        CLIENTS[i].passCard(CLIENTS[0])
                    else:
                        CLIENTS[i].passCard(CLIENTS[i+1])

        scores = {}
        for client in CLIENTS:
            scores[client.name] = client.score
        packet = pickle.dumps(scores)
        length = struct.pack('!I', len(packet))
        packet = length + packet
        for client in CLIENTS:
            client.clientSocket.send(packet)
        print("GAME OVER!")
        for client in CLIENTS:
            print("Client "+client.name+" has " + str(client.score))
        play_again = False
        i = 0
        while True:
            for client in CLIENTS:
                if(client.clientSocket.recv(1024).decode('utf-8') == 'Y'):
                    play_again = True
                    i += 1
            print(i)
            print(NUMBER_OF_PLAYERS)
            if(play_again and i == NUMBER_OF_PLAYERS):
                for client in CLIENTS:
                    client.clientSocket.send(b'Y')
                self.start_game()
            else:
                for client in CLIENTS:
                    client.clientSocket.send(b'N')


    def game_instructions(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Instructions: \n Each player will be dealt with 4 cards. Players will pass \n one card to their right until one of them gets four of a \n kind. The player who first gets a four of a kind will be \n declared the winner.\n\n -----------------------------------------------------------\n")

    def about_the_game(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")

game = Game()
game.main()
