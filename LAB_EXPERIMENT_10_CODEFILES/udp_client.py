import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send message to server
client_socket.sendto(b"Hello from client", ('localhost', 12345))

# Receive response
data, addr = client_socket.recvfrom(1024)

print("Received:", data.decode())

# Close socket
client_socket.close()