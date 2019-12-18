import socket
sock = socket.socket()

def printed():
    print("здесь ничего нет")

sock.connect(("localhost", 9090))
sock.send("wertyui")
data = sock.recv(1024)
sock.close()
print(data)