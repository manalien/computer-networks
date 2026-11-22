import socket

# Create TCP socket
s = socket.socket()

# Bind socket to localhost and port
s.bind(('localhost', 12345))

# Listen for client connections
s.listen(1)

print("Server waiting for connection...")

# Accept client connection
conn, addr = s.accept()

print("Connected with", addr)

# Receive data from client
data = conn.recv(1024)

print("Received from client:", data.decode())

# Send response
conn.send(b"Hello from Server")

# Close connections
conn.close()
s.close()