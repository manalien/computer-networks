import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket
s.bind(('localhost', 12345))

print("UDP Server is ready...")

# Receive data
data, addr = s.recvfrom(1024)

print("Received:", data.decode())

# Send response
s.sendto(b"Hello from Server", addr)

# Close socket
s.close()