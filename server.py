import socket

#UDP discovery
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 8080))

while True:
    conn, addr = server.recvfrom(1024)
    if conn == b"MOBILE_DEVICE":
        print("Connected")
        server.sendto(b"LAPTOP_REPLY", addr)
        break

server.close()

#TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 8081))
server.listen(1)

conn, addr = server.accept()
print("TCP connected")

#接收檔案資訊
header_data = b""
while len(header_data) < 1024:
    chunk = conn.recv(1024 - len(header_data))
    if not chunk:
        break
    header_data += chunk

header = header_data.decode().strip()
file_name, file_size = header.split('|')
file_size  = int(file_size)

#接收導案
with open(f"received_{file_name}", "wb") as f:
    received_size = 0
    while received_size < file_size:
        to_read = min(4096, file_size - received_size)
        data = conn.recv(to_read)
        if not data:
            break
        f.write(data)
        received_size += len(data)

conn.close()
server.close()
