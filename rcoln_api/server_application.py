import tkinter as tk
from server import UDPServer

receiver_address = '0.0.0.0'
receiver_port = 5100
buffer_size = 1024


class ServerManagerApp:
    def __init__(self, root):
        self.root = root
        self.server = None

        # Create a frame to hold the buttons
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Create the buttons
        self.start_button = tk.Button(
            self.frame, text="Start Server", command=self.start_server)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(
            self.frame, text="Stop Server", command=self.stop_server)
        self.stop_button.grid(row=0, column=1, padx=10)

    def start_server(self):
        if self.server is None:
            self.server = UDPServer(
                receiver_address, receiver_port, buffer_size)
            self.server.start_server()
        else:
            print("Server is already running.")

    def stop_server(self):
        if self.server is not None:
            self.server.kill_server()
            self.server = None
        else:
            print("Server is not running.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Server Manager")

    app = ServerManagerApp(root)

    root.mainloop()
