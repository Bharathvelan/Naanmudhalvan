import random
import time
import base64

# Simple grid environment (0 = free, 1 = obstacle)
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

def find_path(grid, start, goal):
    path = [start]
    x, y = start
    while (x, y) != goal:
        if x < goal[0] and grid[x+1][y] == 0:
            x += 1
        elif y < goal[1] and grid[x][y+1] == 0:
            y += 1
        else:
            break
        path.append((x, y))
    return path

# Simulated sensor: random obstacle detection
def detect_obstacle():
    return random.choice([False, False, False, True])  # Rarely True

def get_user_command():
    return input("Command (start/stop/status): ").strip().lower()

# Basic data encryption (base64 for demo)
def encrypt_message(message):
    return base64.b64encode(message.encode()).decode()

def decrypt_message(encoded):
    return base64.b64decode(encoded.encode()).decode()


def main():
    print("Welcome to Autonomous Robot Simulation")
    while True:
        cmd = get_user_command()
        if cmd == "start":
            print("Planning path...")
            path = find_path(grid, start, goal)
            print("Path found:", path)

            for step in path:
                print(f"Moving to {step}...")
                if detect_obstacle():
                    print("Obstacle detected! Stopping.")
                    break
                time.sleep(0.5)

            print("Navigation complete.")
        elif cmd == "status":
            msg = "System is operational"
            encrypted = encrypt_message(msg)
            print("Encrypted status:", encrypted)
            print("Decrypted:", decrypt_message(encrypted))
        elif cmd == "stop":
            print("System shutting down.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
