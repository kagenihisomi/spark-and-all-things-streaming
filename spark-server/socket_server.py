import socket
import threading
import time

def handle_client_connection(client_socket, client_address):
    try:
        print(f"New connection: {client_address}")
        while True:
            # Send data
            message = 'Hello, Spark! ' + time.strftime("%Y-%m-%d %H:%M:%S")
            client_socket.sendall(message.encode('utf-8'))

            # print(message)
            # Wait for 1 second
            time.sleep(1)
    except ConnectionResetError:
        print(f"Client {client_address} disconnected")
    finally:
        client_socket.close()

def start_server(host='localhost', port=4000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server started at {host}:{port}. Waiting for connections...")
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
            client_thread.start()

if __name__ == "__main__":
    start_server()