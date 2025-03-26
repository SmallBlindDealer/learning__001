import requests
import time
import pygame

SERVER_IP = "192.168.1.2"  # Replace with your MacBook's local IP
SERVER_PORT = "5000"

pygame.init()
screen = pygame.display.set_mode((400, 400))

prev_x, prev_y = None, None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if prev_x is not None and prev_y is not None:
                dx, dy = x - prev_x, y - prev_y
                requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/move", json={"dx": dx, "dy": dy})
            prev_x, prev_y = x, y
        elif event.type == pygame.MOUSEBUTTONDOWN:
            requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/click")

pygame.quit()
