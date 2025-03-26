import asyncio
import websockets
import socket
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

async def handle_client(websocket):
    async for message in websocket:
        try:
            udp_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))  # Send raw JSON
        except Exception as e:
            print(f"Error sending UDP: {e}")

async def main():
    server = await websockets.serve(handle_client, "0.0.0.0", 8765)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
