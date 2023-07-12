import socket


# 0: create socket, 1: socket type-UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Replace with the desired destination IP address
destination_address = "192.168.113.224"  # address of the computer server launch.
destination_port = 5100  # Replace with the port in config file.


def send():
    serv = input("services: [k,m,o]; k:keyboard, m:mouse, o:other \nservice:")
    data = f'{{"_service": "{serv}", "_key": "s"}}'

    bytes_data = data.encode("utf-8")
    sock.sendto(bytes_data, (destination_address, destination_port))


send()
