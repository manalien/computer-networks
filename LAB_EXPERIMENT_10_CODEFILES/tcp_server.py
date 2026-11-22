import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to localhost and port 12345
server_socket.bind(('localhost', 12345))

# Start listening for connections
server_socket.listen(1)

print("TCP Server is waiting for connection...")

# Accept client connection
conn, addr = server_socket.accept()

print("Connected by", addr)

# Receive message from client
data = conn.recv(1024)
print("Received:", data.decode())

# Send response
conn.send(b"Hello from server")

# Close connection
conn.close()
server_socket.close()