import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 12345))

# Send message
client_socket.send(b"Hello from client")

# Receive response
data = client_socket.recv(1024)
print("Received:", data.decode())

# Close socket
client_socket.close()