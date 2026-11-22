import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send message to server
s.sendto(b"Hello from Client", ('localhost', 12345))

# Receive response
data, addr = s.recvfrom(1024)

print("Received from server:", data.decode())

# Close socket
s.close()