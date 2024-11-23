import socket
import pyotp
totp = pyotp.TOTP('JBWW23LNNVWTUIDIOR2HA4Z2F4XWE2LUFZWHSLZTPBWHAT3YM4======')

# Define the target host and port
host = #IP address
port = #Port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    # Receive the initial message
    initial_message = s.recv(1024).decode()
    s.sendall(((str(totp.now())) + '\n\r').encode('utf-8'))

    response = s.recv(1024)
    response = s.recv(1024)
    print(response.decode())

