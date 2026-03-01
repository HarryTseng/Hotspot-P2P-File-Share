import socket
import os
import tkinter as tk
from tkinter import filedialog

#UDP discovery
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

server_ip = server[0]

#TCP file transfer
if server_ip:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 8081))

    #以視窗選擇要傳的檔案
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()

    #檔案資訊
    file = open(file_path, "rb")
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    header = f"{file_name}|{file_size}"
    header_padded = header.encode().ljust(1024)
    client.sendall(header_padded)

    #傳檔案
    data = file.read()
    client.sendall(data)

    file.close()
    client.close()

else:
    exit()