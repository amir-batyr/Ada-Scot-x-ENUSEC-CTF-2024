import socket
import hashlib

# Define the target host and port
host = #IP address
port = #Port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    print("Connecting to the server...")
    s.connect((host, port))
    print("Connected!")

    # Receive the initial message
    initial_message = s.recv(1024).decode()
    data = initial_message[49:]

    # Calculate the MD5 checksum
    md5_checksum = hashlib.md5(data.encode()).hexdigest()

    s.sendall((md5_checksum + '\n\r').encode('utf-8'))

    response = s.recv(1024)
    print(response.decode())
    response = s.recv(1024)
    print(response.decode())
