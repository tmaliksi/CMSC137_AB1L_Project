# import needed modules
import pickle, random, socket, struct, sys, threading

# initiate required variables
SUITS = ["C","S","H","D"]
CARDS = []
CLIENTS = []
isEND = False
HOST = 0
PORT = 0
NUMBER_OF_PLAYERS = 0

# define ClientThread class
class ClientThread(threading.Thread):
    # define initialization of class instances
    def __init__(self,clientSocket,clientAddress):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.clientAddress = clientAddress
        self.score = 0
        self.clientCards = []
        self.isWinner = False
        self.name = clientSocket.recv(1024).decode('utf-8')
        print("New connection added: ", clientAddress)
    # define getCards function
    def getCards(self):
        # use global CARDS variable
        global CARDS
        # receive index of card from client
        card = self.clientSocket.recv(1024)
        # remove card from client's array and insert into global CARDS
        CARDS.insert(0,self.clientCards.pop(int(card.decode("utf-8"))))

    def passCard(self,client):
        # use global CARDS variable
        global CARDS
        # get index of last card from CARDS
        index = len(CARDS) - 1
        # remove last card from CARDS
        card = CARDS.pop(index)
        # append removed card to client's array of cards
        client.clientCards.append(card)

    def checkIfComplete(self):
        # check if card has one or two digits
        if(len(self.clientCards[0]) > 2):
            kind = self.clientCards[0][0:2]
        else:
            kind = self.clientCards[0][0]
        # loop through all cards and check if all cards have the same number
        for card in self.clientCards[1:4]:
            if(len(self.clientCards[0]) > 2):
                if(kind != card[0:1]):
                    # if not, return False
                    return False
            else:
                if(kind != card[0]):
                    # if not, return false
                    return False
        # if yes, declare client as winner and add score
        self.isWinner = True
        self.score += 1
        # return True
        return True

class Game:
    # print description of game
    def display_description(self):
        print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n About the Game: \n This program is created by Peter John Castillo, Abigail \n Fernandez, Troy Abraham Maliksi, and Arvin Sartillo as part \n of the final requirements for CMSC 137 Data Communications \n and Networking. \n -----------------------------------------------------------\n")
        input(" Enter any key to continue...")

    # print main menu
    def main(self):
        menu_loop = True
        while menu_loop:
            print("\n -----------------------------------------------------------\n                     1-2-3 Pass Game\n Menu: \n ")
            print(" [1] Start Server \n [2] About the Game \n [3] Exit \n")
            menu_option = input('\n >>> Enter: ')
            print('\n -----------------------------------------------------------')

            # do function based on user input
            if menu_option == '1':
                self.start_server()
                self.start_game()
            elif menu_option == '2':
                self.display_description()
            elif menu_option == '3':
                menu_loop = False
            else:
                print('\n Please choose a number.\n')

    def start_server(self):
        global CLIENTS, SUITS, CARDS, isEND, HOST, PORT, NUMBER_OF_PLAYERS
        # get IP address, port number, and number of players
        HOST = input(" Enter IP address: ")
        PORT = int(input(" Enter port number: "))
        NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))

        # check if number of players is within 3-13
        while NUMBER_OF_PLAYERS <= 2 or NUMBER_OF_PLAYERS > 13:
            print(" Minimum number of players is 3 and maximum number of players is 13")
            NUMBER_OF_PLAYERS = int(input(" Enter number of players: "))

        # initializre socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # try to bind to given ip address and port number
        while True:
            try:
                s.bind((HOST,PORT))
                break
            except:
                print("Invalid port.")
                PORT = int(input(" Enter port number: "))
        # listen for clients
        s.listen(1)
        # print how many number of clients are needed and append joined clients to array of CLIENTS
        for i in range(NUMBER_OF_PLAYERS):
            print(" Waiting for "+str(NUMBER_OF_PLAYERS - len(CLIENTS))+" client/s on port "+str(PORT)+"...")
            clientSocket, clientAddress = s.accept()
            CLIENTS.append(ClientThread(clientSocket,clientAddress))

    def start_game(self):
        global CLIENTS, SUITS, CARDS, isEND, NUMBER_OF_PLAYERS
        # initialize values of clients
        for client in CLIENTS:
            client.clientCards = []
            client.isWinner = False
        isEND = False
        # make list of numbers equal to number of clients
        NUMBERS = list(range(1,NUMBER_OF_PLAYERS+1))
        # make card strings
        for number in NUMBERS:
            for suit in SUITS:
                CARDS.append(str(number)+suit)

        # distribute cards to card arrays of clients
        while len(CARDS) != 0:
            for client in CLIENTS:
                index = random.randint(0,len(CARDS)-1)
                card = CARDS.pop(index)
                client.clientCards.append(card)
        while True:
            # check if a client has won
            for client in CLIENTS:
                isEND = client.checkIfComplete()
            # if yes, send win or lose messages to clients
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
            # send card arrays to clients
            for client in CLIENTS:
                packet = pickle.dumps(client.clientCards)
                length = struct.pack('!I', len(packet))
                packet = length + packet
                client.clientSocket.send(packet)
            # print cards of each client
            for client in CLIENTS:
                print("Client "+client.name+" has " + str(client.clientCards))
            # break from loop if a player has won
            if(isEND):
                break
            # get cards from clients
            for client in CLIENTS:
                client.getCards()
            # pass DEMO_CARDS
            if(len(CARDS) == NUMBER_OF_PLAYERS):
                for i in range(len(CLIENTS)):
                    if(i == len(CLIENTS)-1):
                        CLIENTS[i].passCard(CLIENTS[0])
                    else:
                        CLIENTS[i].passCard(CLIENTS[i+1])
        # initiate dictionary of scores
        scores = {}
        for client in CLIENTS:
            scores[client.name] = client.score
        # send dictionary to clients
        packet = pickle.dumps(scores)
        length = struct.pack('!I', len(packet))
        packet = length + packet
        for client in CLIENTS:
            client.clientSocket.send(packet)
        print("GAME OVER!")
        for client in CLIENTS:
            print("Client "+client.name+" has " + str(client.score))
        # check if clients want to play again
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

game = Game()
game.main()
