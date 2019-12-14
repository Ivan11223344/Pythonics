import socket
sock = socket.socket()
sock.bint((",9090))
sock.listen(3)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send