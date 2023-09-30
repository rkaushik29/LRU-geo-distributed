import socket
import threading
from collections import OrderedDict

# Defines the main server's data (characters A-Z as key with their data as values)
main_server_data = {chr(ord('A') + i): f"Data:{chr(ord('A') + i)}" for i in range(26)}

# Reads details of the servers and clients from the input file
def read_server_client_details(input_file):
    global M, N             # used to start threads below
    server_details = {}
    client_details = {}

    with open(input_file, 'r') as file:
        M, N, R = map(int, file.readline().strip().split())
        
        for _ in range(M):
            server_id, x, y = file.readline().strip().split()
            server_details[server_id] = (float(x), float(y))

        for _ in range(N):
            client_id, x, y = file.readline().strip().split()
            client_details[client_id] = (float(x), float(y))

    return server_details, client_details

# Function to write the state of all server caches to server_out.txt
def display_cache_state(output_file):
    with open(output_file, 'w') as output:
        for port, cache in server_caches.items():
            output.write(f"Server{str(port - 49152 + 1)} at {server_locations[str(port - 49152 + 1)]}\nCache:\n")
            for key, value in cache.cache.items():
                output.write(f"{key}: {value}\n")
            output.write("\n")
        output.write("---------------------------------------------------\n")

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Update the key to the most recently used position
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return None

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            # Remove the least recently used item
            self.cache.popitem(last=False)

        self.cache[key] = value

# Function to handle client requests
def handle_client(client_socket, client_location, server_port):
    request = client_socket.recv(1024).decode()
    
    # Calculate distances to each server and find the nearest one
    nearest_server = None
    nearest_distance = float('inf')
    for port, server_location in server_locations.items():
        distance = calculate_distance(client_location, server_location)
        if distance < nearest_distance:
            nearest_server = port
            nearest_distance = distance

    # Check if the request is in the cache
    response = server_caches[server_port].get(request)

    if response is None:
        # Data not found in cache, fetch from main_server_data
        response = main_server_data.get(request, "Data not found")

        # Store the response in the cache
        server_caches[server_port].put(request, response)

    # Display the state of all caches
    display_cache_state(output_file="server_out.txt")

    client_socket.send(response.encode())
    client_socket.close()

# Calculate distance between two coordinates (simplified using Euclidean distance)
def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Function to start a server at a given port
def start_server(port, location):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(5)
    print(f"Server{str(port - 49152 + 1)} listening at {location}")

    while True:
        client_socket, _ = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, location, port))
        client_thread.start()

# Define server locations (coordinates)
server_locations, _ = read_server_client_details('input.txt')

# Create an LRU cache for each server
server_caches = {port: LRUCache(capacity=3) for port in range(49152, 49152 + max(int(i) for i in server_locations.keys()))}  # Adjust capacity as needed

# Start servers with locations and ports
for server_id, location in server_locations.items():
    server_port = 49152 + list(server_locations.keys()).index(server_id)
    server_thread = threading.Thread(target=start_server, args=(server_port, location))
    server_thread.start()
