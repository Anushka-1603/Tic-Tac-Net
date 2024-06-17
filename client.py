import socket
server_ip_address = '127.0.0.1'   # Replace with address of VM

# Server address and port
SERVER_HOST = server_ip_address
SERVER_PORT = 12345

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send a request to run the game
client_socket.sendall('run_game'.encode('utf-8'))

# Close the connection
client_socket.close()