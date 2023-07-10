import socket


class UDPServer:
    def __init__(self, address, port, buffer_size):
        self.address = address
        self.port = port
        self.buffer_size = buffer_size
        self.udp_socket = None

    def start_server(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((self.address, self.port))

        while True:
            data, sender_address = self.udp_socket.recvfrom(self.buffer_size)
            print("Received data:", data.decode('utf-8'))

    def kill_server(self):
        if self.udp_socket is not None:
            self.udp_socket.close()
            print("Server killed.")
