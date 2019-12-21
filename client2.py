import socket 
import threading
def read_sok():
    while 1 :
        data = sor.recv(1024)
        print(data.decode('utf-8'))
server = 'localhost', 6003
aliast = input()
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto((aliast+'Connect to server').encode('utf-8'), server)
potok = threading.Thread(target= read_sok)
potok.start()
while 1 :
    message = input()
    sor.sendto(('['+aliast+']'+message).encode('utf_8'), server)