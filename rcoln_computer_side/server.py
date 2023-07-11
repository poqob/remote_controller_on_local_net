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
                # action
                data, sender_address = self.udp_socket.recvfrom(self.buffer_size)
                print(
                    f"Received data from {sender_address[0]}: ",
                    data.decode("utf-8"),
                )
            except OSError as e:
                # Handle the OSError if needed
                # print("Error occurred:", e)
                break
        # self.kill_server()

    def kill_server(self):
        if self.udp_socket:
            self.udp_socket.close()
            self.udp_socket = None
            print("Server killed.")

    def get_local_ip_port(self):
         # Create a temporary socket to retrieve the local IP and port
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))  # Connect to a known external IP

        ip_port = f"IP: {temp_socket.getsockname()[0]}, Port: {self.port}"

        temp_socket.close()
        return ip_port