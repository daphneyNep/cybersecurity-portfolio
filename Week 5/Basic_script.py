# Enhanced login log simulation with random devices and locations

import datetime
import random

# Lists of possible device types and locations
devices = ["Laptop", "Desktop", "Tablet", "Smartphone"]
locations = ["New York", "California", "Texas", "Florida", "Illinois"]

def log_login(username, success, ip_address):
    timestamp = datetime.datetime.now()
    status = "SUCCESS" if success else "FAILURE"

    # Randomly select a device and location
    device = random.choice(devices)
    location = random.choice(locations)

    log_entry = (
        f"{timestamp} - {username} - {status} - "
        f"IP: {ip_address} - Device: {device} - Location: {location}"
    )

    # Save to log file
    with open("detailed_login_logs.txt", "a") as log_file:
        log_file.write(log_entry + "\n")

# Simulate some login attempts
log_login("user1", True, "192.168.1.100")
log_login("user2", False, "10.0.0.5")
log_login("user3", True, "172.16.1.10")
log_login("user4", False, "192.168.0.25")
log_login("user5", True, "10.1.1.15")

print("Detailed login attempts logged.")

