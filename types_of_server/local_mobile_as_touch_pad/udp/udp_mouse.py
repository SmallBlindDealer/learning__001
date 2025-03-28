import socket
import json
from pynput.mouse import Controller, Button

mouse = Controller()

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

is_holding = False  # Track hold-click state

while True:
    data, addr = sock.recvfrom(1024)
    try:
        decoded_data = json.loads(data.decode())

        if decoded_data["type"] == "move":
            dx = float(decoded_data["dx"])
            dy = float(decoded_data["dy"])
            mouse.move(dx, dy)

        elif decoded_data["type"] == "click":
            mouse.click(Button.left, 1)

        elif decoded_data["type"] == "right_click":
            mouse.click(Button.right, 1)

        elif decoded_data["type"] == "hold_click":
            if not is_holding:
                mouse.press(Button.left)
                is_holding = True  # Start holding click

        elif decoded_data["type"] == "release_click":
            if is_holding:
                mouse.release(Button.left)
                is_holding = False  # Release click

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e} | Data: {data}")
    except KeyError as e:
        print(f"Missing Key: {e} | Data: {data}")
    except Exception as e:
        print(f"Error: {e} | Data: {data}")
