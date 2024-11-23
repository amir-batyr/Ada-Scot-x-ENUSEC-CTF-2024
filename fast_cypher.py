import socket

host = #IP address
port = #Port


def caesar_cipher_brute_force(encoded_text):
    alphabet_size = 26
    for shift in range(1, alphabet_size):
        decoded_text = ""
        for char in encoded_text:
            if char.isalpha():
                # Apply shift
                shifted = ord(char) - shift

                # Handle wrap-around for lowercase letters
                if char.islower():
                    if shifted < ord('a'):
                        shifted += alphabet_size
                # Handle wrap-around for uppercase letters
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += alphabet_size

                decoded_text += chr(shifted)
            else:
                # Non-letter characters remain the same
                decoded_text += char
        if decoded_text[:3] == 'the':
            return decoded_text

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    print("Connecting to the server...")
    s.connect((host, port))
    print("Connected!")

    # Receive the initial message
    initial_message = s.recv(1024).decode()
    print(initial_message)
    initial_message = s.recv(1024).decode()
    print(initial_message[20:])
    s.sendall((str(caesar_cipher_brute_force(initial_message[20:])) + '\n\r').encode('utf-8'))
    response = s.recv(1024)
    print(response.decode())
    response = s.recv(1024)
    print(response.decode())
