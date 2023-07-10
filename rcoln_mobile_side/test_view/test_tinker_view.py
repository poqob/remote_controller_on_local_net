import tkinter as tk
import socket


# 0: create socket, 1: socket type-UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Replace with the desired destination IP address
destination_address = '127.0.0.1'
destination_port = 5100  # Replace with the desired destination port


def send(data):
    bytes_data = data.encode('utf-8')
    sock.sendto(bytes_data, (destination_address, destination_port))


def button_click(event):
    button = event.widget
    key = button["text"]
    send(key)


def create_tkinter_app():
    root = tk.Tk()
    root.title("test sender")

    # Create a frame to hold the buttons
    frame = tk.Frame(root)
    frame.pack(pady=20)

    # Create the buttons
    button1 = tk.Button(frame, text="A")
    button1.grid(row=0, column=0, padx=10)
    # Bind left mouse button click event
    button1.bind("<Button-1>", button_click)
    button2 = tk.Button(frame, text="D")
    # Bind left mouse button click event
    button2.bind("<Button-1>", button_click)
    button2.grid(row=0, column=1, padx=10)

    root.mainloop()


def on_close():
    socket.close()


if __name__ == "__main__":
    create_tkinter_app()
