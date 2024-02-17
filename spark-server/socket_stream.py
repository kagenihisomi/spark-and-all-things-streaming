import socket
import time

def send_data_to_socket(host='localhost', port=4000, message='Hello, Spark!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        try:
            while True:
                # Send data
                s.sendall(message.encode('utf-8'))
                # Wait for a second before sending the next message
                time.sleep(1)
        except KeyboardInterrupt:
            print("Data streaming stopped by the user")

if __name__ == "__main__":
    send_data_to_socket()