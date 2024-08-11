import socket
import threading
import hashlib
import random

def generate_key_schedule(key):
    key_schedule = []
    for i in range(len(key)):
        key_schedule.append(ord(key[i]) + i)
    for i in range(len(key), 256):
        key_schedule.append((key_schedule[i - len(key)] + key_schedule[i - 1]) % 256)
    return key_schedule

def custom_encrypt(plaintext, key):
    key_schedule = generate_key_schedule(key)
    encrypted = []
    for round in range(3):  
        temp = []
        for i, char in enumerate(plaintext):
            key_c = key_schedule[(i + round) % len(key_schedule)]
            plaintext_c = ord(char)
            temp.append(chr((plaintext_c ^ key_c) % 256))  
        plaintext = ''.join(temp)
    encrypted = plaintext[::-1]  
    return encrypted

def custom_decrypt(ciphertext, key):
    key_schedule = generate_key_schedule(key)
    ciphertext = ciphertext[::-1] 
    decrypted = []
    for round in range(2, -1, -1): 
        temp = []
        for i, char in enumerate(ciphertext):
            key_c = key_schedule[(i + round) % len(key_schedule)]
            ciphertext_c = ord(char)
            temp.append(chr((ciphertext_c ^ key_c) % 256)) 
        ciphertext = ''.join(temp)
    return ciphertext

def handle_client(client_socket, key):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                decrypted_message = custom_decrypt(message, key)
                print(f"Received: {decrypted_message}")
        except:
            print("Connection closed.")
            client_socket.close()
            break

def server_program(ip, port, key):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print(f"Server listening on {ip}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket, key)).start()

def client_program(ip, port, key):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    print(f"Connected to {ip}:{port}")

    while True:
        message = input("Enter message: ")
        encrypted_message = custom_encrypt(message, key)
        client_socket.send(encrypted_message.encode())

if __name__ == "__main__":
    server_ip = input("Enter server IP address: ").strip()
    server_port = int(input("Enter server port: ").strip())
    client_ip = input("Enter client IP address to connect to: ").strip()
    client_port = int(input("Enter client port to connect to: ").strip())
    key = input("Enter encryption key: ").strip()

    server_thread = threading.Thread(target=server_program, args=(server_ip, server_port, key))
    client_thread = threading.Thread(target=client_program, args=(client_ip, client_port, key))

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()
