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

# check if user supplied required arguments
if (len(sys.argv) != 3):
	print("\nUsage: python3 <filename>.py <port> <number_of_players>\n")
	sys.exit()

# assign arguments to variables
PORT = int(sys.argv[1])
NUMBER_OF_PLAYERS = int(sys.argv[2])
# i = 0
# conn = []
# addr = []

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
