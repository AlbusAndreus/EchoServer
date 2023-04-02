import socket

host = "127.0.0.1"
port = 5004
sock = socket.socket()
sock.bind((host, port))
sock.listen(2)
conn, address = sock.accept()
while True:
    data = conn.recv(1020).decode()
    conn.send(data.encode())