# server.py
import socket
import threading

clients = []
client_data = {}

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            client_data[addr] = data
            other_clients = [c for c in clients if c != conn]
            for client in other_clients:
                client.send(data.encode())
        except:
            break

    conn.close()
    clients.remove(conn)
    del client_data[addr]
    print(f"Connection closed: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(2)
print("Server started, waiting for connections...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    client_data[addr] = "0,0"
    threading.Thread(target=handle_client, args=(conn, addr)).start()
