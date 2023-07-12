# TODO
# start local server on local computer ip and port
# show ip and port
# take action according to udp package's data.


import tkinter as tk
from server_manager import ServerManager
import threading
import socket

# TODO
# dedect computer ip-port pass it to server. --later
# server will send packages to computer's


class ServerManagerApp:
    # fields
    sm = ServerManager("rcoln_computer_side\config.ini")

    def __init__(self, root):
        self.root = root
        # Create a frame to hold the buttons
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Get the local IP address and port
        self.ip_port = self.sm.get_ip_port()
        # Create the IP:Port label
        self.ip_port_label = tk.Label(self.frame, text=self.ip_port)
        self.ip_port_label.grid(row=0, columnspan=2)

        # Create the buttons
        self.start_button = tk.Button(
            self.frame, text="Start Server", command=self.start_server
        )
        self.start_button.grid(row=1, column=0, padx=10)

        self.stop_button = tk.Button(
            self.frame, text="Stop Server", command=self.stop_server
        )
        self.stop_button.grid(row=1, column=1, padx=10)

    def start_server(self):
        # threading
        threading.Thread(target=self.sm.start).start()

    def stop_server(self):
        self.sm.stop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Server Manager")
    app = ServerManagerApp(root)
    root.mainloop()
