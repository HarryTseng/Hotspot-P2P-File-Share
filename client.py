import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.settimeout(1.0)
MESSAGE = b"MOBILE_DEVICE"
addr = ('255.255.255.255', 8080)

try:
    client.sendto(MESSAGE, addr)
    data, server = client.recvfrom(1024)
    if data == b"LAPTOP_REPLY":
        print("Receive")

except socket.timeout:
    print("Time Exceed")

finally:
    client.close()