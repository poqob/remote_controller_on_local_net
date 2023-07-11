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
        print(f"Server started on: {self.address}:{self.port}")

        while True:
            try:
                data, sender_address = self.udp_socket.recvfrom(self.buffer_size)
                print("Received data:", data.decode("utf-8"))
            except OSError as e:
                # Handle the OSError if needed
                # print("Error occurred:", e)
                break
        self.kill_server()

    def kill_server(self):
        if self.udp_socket:
            self.udp_socket.close()
            self.udp_socket = None
            print("Server killed.")
