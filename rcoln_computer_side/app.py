import tkinter as tk
from server_manager import ServerManager

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
            self.frame, text="Start Server", command=self.sm.start
        )
        self.start_button.grid(row=1, column=0, padx=10)

        self.stop_button = tk.Button(
            self.frame, text="Stop Server", command=self.sm.stop
        )
        self.stop_button.grid(row=1, column=1, padx=10)

    def on_destroy(self):
        # kill server
        self.sm.destroy()
        self.root.destroy()
        exit()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Server Manager")
    app = ServerManagerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_destroy)
    root.mainloop()
