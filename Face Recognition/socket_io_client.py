import socketio

# Create a Socket.IO client instance
sio = socketio.Client()

# Define event handlers
@sio.event
def connect():
    print("Successfully connected to the server")

@sio.event
def connect_error(data):
    print("Failed to connect to the server")
    print(data)

@sio.event
def disconnect():
    print("Disconnected from the server")

# Adjusted event handler for receiving messages
@sio.on('message1')
def on_message1(data):
    print("Received message1:", data)

# Adjusted event handler for test response
@sio.on('test response')
def on_test_response(data):
    print("Test response received:", data)

# Adjusted event handler for rulesResponse
@sio.on('rulesResponse')
def on_rules_response(data):
    print("Rules response received:", data)

# Function to join rooms
def join_rooms(rooms_ids):
    sio.emit("joinRooms", rooms_ids)

# Function to create rooms
def create_rooms(rooms_ids):
    sio.emit("createRooms", rooms_ids)

# Function to leave rooms
def leave_rooms(rooms_ids):
    sio.emit("leaveRooms", rooms_ids)

# Function to send a message to a room
def send_room_message(room_id, message_value):
    sio.emit("messageToRoom", {"roomId": room_id, "value": message_value})

# Function to get rules
def get_rules(user, project_name, token):
    sio.emit("getRules", {"user": user, "projectName": project_name, "token": token})

# Connect to the Socket.IO server
server_url = "http://143.47.53.106:5167/"  # Ensure the correct protocol (https)
try:
    sio.connect(server_url, wait_timeout=20)  # Increase timeout
except socketio.exceptions.ConnectionError as e:
    print("Connection failed:", e)

# Example usage
# join_rooms(["room1", "room2"])
# send_room_message("room1", "Hello from Python client!")
# get_rules("username", "projectName", "token")

# Wait for messages
sio.wait()