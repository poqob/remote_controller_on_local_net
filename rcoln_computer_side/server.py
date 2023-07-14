import socket
from package_handler import PackageHandler
from service_handler import ServiceHandler
import threading
from enum import Enum


class ServerStatus(Enum):
    off = (0,)
    on = (1,)


class UDPServer:
    # fields
    server_status = ServerStatus.off
    stop_event = None
    serviceHandler = None

    # constructure
    def __init__(self, address, port, buffer_size):
        self.address = address
        self.port = port
        self.buffer_size = buffer_size
        self.udp_socket = None
        self.stop_event = threading.Event()
        self.serviceHandler = ServiceHandler()

    # run the server
    def start_server(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((self.address, self.port))
        print(f"Server started on: {self.address}:{self.port}")
        self.thread = threading.Thread(target=self.serve)
        self.stop_event.clear()
        self.thread.start()
        self.server_status = ServerStatus.on

    # kill server and server extensions
    def kill_server(self):
        if self.udp_socket:
            self.udp_socket.close()
            self.udp_socket = None
        self.stop_event.set()
        # self.thread.join()
        self.server_status = ServerStatus.off
        print("Server killed.")

    # server main activity
    def serve(self):
        while not self.stop_event.is_set():
            try:
                # action
                data, sender_address = self.udp_socket.recvfrom(self.buffer_size)
                service, model = PackageHandler.handle(
                    data=data, sender_address=sender_address
                )  # returns service , model
                # direct solved packages to service handler
                self.serviceHandler.accept(service=service, model=model)

            except OSError as e:
                # Handle the OSError if needed
                # print("Error occurred:", e)
                pass

    # server destructor
    def destroy(self):
        try:
            if self.serviceHandler:
                self.serviceHandler.stopServices()
                self.serviceHandler = None
            if self.server_status is ServerStatus.on:
                self.kill_server()
        except Exception as e:
            print(e)

    # monitoring local wlan0 address of machine that runs the server
    def get_local_ip_port(self):
        # Create a temporary socket to retrieve the local IP and port
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))  # Connect to a known external IP

        ip_port = f"IP: {temp_socket.getsockname()[0]}, Port: {self.port}"

        temp_socket.close()
        return ip_port


if __name__ == "__main__":
    server = UDPServer("127.0.0.1", 12345, 1024)
    server.start_server()
