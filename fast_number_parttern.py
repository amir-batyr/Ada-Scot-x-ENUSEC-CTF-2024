import socket

host = #IP address
port = #Port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    print("Connecting to the server...")
    s.connect((host, port))
    print("Connected!")

    # Receive the initial message
    print(s.recv(1024).decode())

    initial_message = s.recv(1024).decode()
    array = initial_message[14:-16].split(',')
    missing = 0
    for i in range(len(array)):
        try:
            array[i] = int(array[i])
        except:
            missing = i

    for i in range(len(array)):
        if i != missing and (i+1) != missing:
            s.sendall((str(array[missing+1]-(array[i+1] - array[i])) + '\n\r').encode('utf-8'))
            response = s.recv(1024)
            print(response.decode())
            response = s.recv(1024)
            print(response.decode())
            exit()
