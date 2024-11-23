import socket

host = #IP address
port = #Port

for i in range(1, 500):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        
        # Receive the initial message
        initial_message = s.recv(1024).decode()
        initial_message = s.recv(1024).decode()
        
        # Create a string of length i
        message_to_send = 'X' * i
        
        # Send the message
        s.send((message_to_send + '\n\r').encode('utf-8'))
        
        # Optionally, receive a response from the server
        response = s.recv(1024).decode()
        response = s.recv(1024).decode()
        print(f"Received response: {response},{i}")
    
    # Socket is automatically closed at the end of the 'with' block
