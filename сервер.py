import socket
sock = socket.socket()
sock.bind(("",9090))
sock.listen(3)
conn, addr = sock.accept()
print ("connected:", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.npper())
conn.close()