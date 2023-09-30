import socket
###################### I/O Operations for Testing ######################
# Read client requests from input file
def read_client_requests(input_file):
    client_requests = []

    with open(input_file, 'r') as file:
        M, N, R = map(int, file.readline().strip().split())

        for i in range(M + N + R):
            line = file.readline().strip()
            if i >= M+N:
                parts = line.split()
                if len(parts) == 3:
                    client_requests.append((parts[0], parts[1], parts[2]))

    return client_requests

# Read server and client details from input file
def read_server_client_details(input_file):
    server_details = {}
    client_details = {}

    with open(input_file, 'r') as file:
        M, N, R = map(int, file.readline().strip().split())

        # Read server locations and assign ports dynamically
        server_ports = range(49152, 49152 + M)
        for i in range(M):
            server_id, x, y = file.readline().strip().split()
            server_details[server_id] = (float(x), float(y), server_ports[i])  # Include the server port

        # Read client locations
        for _ in range(N):
            client_id, x, y = file.readline().strip().split()
            client_details[client_id] = (float(x), float(y))

    return server_details, client_details
########################################################################

# Function to send a request to the nearest server based on client's location
def send_request(request, client_id, server_locations):
    nearest_server = None
    nearest_distance = float('inf')

    for server_id, server_location in server_locations.items():
        distance = calculate_distance(client_locations[client_id], (server_location[0], server_location[1]))
        if distance < nearest_distance:
            nearest_server = server_id
            nearest_distance = distance
    print(nearest_distance)

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 49152 + int(nearest_server) - 1))
        client_socket.send(request.encode())
        response = client_socket.recv(1024).decode()
        print(f"Response from server {nearest_server} for {client_id}: {response}")

        client_socket.close()
        return response
    except ConnectionRefusedError:
        return "Connection Error"

# Calculate distance between two coordinates (using Euclidean distance)
def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# # Define server locations (coordinates)
# server_locations = {
#     49152: (0, 0),
#     8081: (1, 1),
#     8082: (2, 2),
#     8083: (3, 3),
#     8084: (4, 4),
# }

# # Define client locations (coordinates)
# client_locations = {
#     'Client 1': (0.5, 0.5),
#     'Client 2': (3.5, 3.5),
# }

server_locations, client_locations = read_server_client_details('input.txt')

# Example client requests with coordinates
client_requests = read_client_requests('input.txt')

for client_id, request_name, data in client_requests:
    response = send_request(data, client_id, server_locations)
    print(f"{request_name} by {client_id}: {response}")

