import socket
import subprocess

# Host and port for the server
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening...')

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print('Connected by', client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')

    if data == 'run_game':
        # Run the Tic Tac Toe game
        subprocess.Popen(['python3', 'tic_tac_toe.py'])
        print('Tic Tac Toe game started!')

    # Close the connection
    client_socket.close()