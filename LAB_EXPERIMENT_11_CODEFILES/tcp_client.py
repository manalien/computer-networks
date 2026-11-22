import socket

# Create TCP socket
s = socket.socket()

# Connect to server
s.connect(('localhost', 12345))

# Send message
s.send(b"Hello from Client")

# Receive server response
data = s.recv(1024)

print("Received from server:", data.decode())

# Close socket
s.close()