from server import UDPServer

# Define the server parameters
receiver_address = '0.0.0.0'
receiver_port = 5100
buffer_size = 1024

# Create an instance of the UDPServer
server = UDPServer(receiver_address, receiver_port, buffer_size)

# Start the server
server.start_server()

# Perform some actions...

# Stop the server
server.kill_server()
