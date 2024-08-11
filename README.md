# Encrypted-Messenger
Simple Encrypted Messenger based on Socket Connections and Custom Encryption

### Tip: Use playit.gg if you don't want to share your ip (;

![image](https://github.com/user-attachments/assets/66991e2b-28b1-43f8-8d15-8e70175c4b55)

## Features

- Custom Encryption and Decryption: The script uses a custom encryption algorithm that involves generating a key schedule and performing multiple rounds of XOR operations on the plaintext. The ciphertext is then reversed to add an extra layer of security.
- Key Schedule Generation: The generate_key_schedule function creates a key schedule based on the provided key, ensuring that the encryption and decryption processes are synchronized.
- Client-Server Architecture: The script supports both server and client functionalities, allowing for two-way communication. The server listens for incoming connections, while the client connects to the server and sends encrypted messages.
- Multithreading: The server uses multithreading to handle multiple client connections simultaneously. Each client connection is managed in a separate thread, ensuring that the server can process multiple messages concurrently.
- Socket Programming: The script utilizes Python’s socket module to establish TCP connections between the server and clients. This enables reliable communication over the network.
- Interactive Messaging: The client program allows users to input messages, which are then encrypted and sent to the server. The server decrypts the received messages and prints them, providing a basic interactive messaging experience.
- Error Handling: The script includes basic error handling to manage connection issues. If a connection is closed or an error occurs, the server prints a message and closes the client socket.
