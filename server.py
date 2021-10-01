
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(10)

while True:
    clientsocket, address = s.accept()
    print(f'welcome from {address} ')
    clientsocket.send(bytes('welcome to the server', 'utf-8'))
    clientsocket.close()