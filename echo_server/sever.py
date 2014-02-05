import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 10000))
s.listen(1)
c, address = s.accept()
print('Connect by', address)

while True:
    data = c.recv(1024)
    if not data:
        break
    c.send(data)
c.close()