import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 8080))

while True:
    data, addr = server.recvfrom(1024)
    if data == b"MOBILE_DEVICE":
        print("Connected")
        server.sendto(b"LAPTOP_REPLY", addr)



