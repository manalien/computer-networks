import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server to localhost and port 12345
server_socket.bind(('localhost', 12345))

print("UDP Server is ready...")

# Receive message from client
data, addr = server_socket.recvfrom(1024)

print("Received:", data.decode())

# Send response to client
server_socket.sendto(b"Hello from server!", addr)

# Close socket
server_socket.close()