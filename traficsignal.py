import time

class TrafficLight:
    def __init__(self, position):
        self.position = position  # Position of the traffic light (e.g., "NORTH", "EAST")
        self.state = "RED"  # Initial state of the traffic light
        self.timer = 0  # Timer for the current state

    def change_state(self, new_state, duration):
        self.state = new_state
        self.timer = duration
        print(f"[{self.position}] Traffic light turned {new_state} for {duration} seconds.")

    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1

    def is_green(self):
        return self.state == "GREEN"

class TrafficController:
    def __init__(self):
        self.traffic_lights = {
            "NORTH": TrafficLight("NORTH"),
            "EAST": TrafficLight("EAST"),
            "SOUTH": TrafficLight("SOUTH"),
            "WEST": TrafficLight("WEST"),
        }
        self.cycle_order = ["NORTH", "EAST", "SOUTH", "WEST"]
        self.current_index = 0
        self.default_green_duration = 10
        self.default_yellow_duration = 3

    def run_cycle(self):
        # Turn all lights RED initially
        for light in self.traffic_lights.values():
            light.change_state("RED", 0)

        # Activate green light for the current direction
        current_direction = self.cycle_order[self.current_index]
        green_light = self.traffic_lights[current_direction]
        green_light.change_state("GREEN", self.default_green_duration)

        # Simulate green light duration
        while green_light.timer > 0:
            time.sleep(1)  # Simulate 1 second
            green_light.update_timer()

        # Change to yellow light
        green_light.change_state("YELLOW", self.default_yellow_duration)

        # Simulate yellow light duration
        while green_light.timer > 0:
            time.sleep(1)  # Simulate 1 second
            green_light.update_timer()

        # Move to the next direction in the cycle
        self.current_index = (self.current_index + 1) % len(self.cycle_order)

    def start(self):
        print("Starting traffic light controller...")
        while True:
            self.run_cycle()

# Main Execution
if __name__ == "__main__":
    controller = TrafficController()
    controller.start()
