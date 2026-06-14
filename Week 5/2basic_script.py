# Anomaly detection in login logs
from collections import defaultdict

def inspect_logs(log_file):
    failed_attempts = defaultdict(int)
    failed_ips = defaultdict(list)

    with open(log_file, 'r') as file:
        for line in file:
            if "FAILURE" in line:
                parts = line.strip().split(" - ")

                username = parts[1]

                # Extract IP address
                ip_address = parts[3].replace("IP: ", "")

                failed_attempts[username] += 1
                failed_ips[username].append(ip_address)

    print("Failed login attempts:")
    for user, count in failed_attempts.items():
        if count > 1:
            print(f"User: {user}")
            print(f"Failed Attempts: {count}")
            print(f"IP Addresses: {', '.join(failed_ips[user])}")
            print()

# Inspect the detailed login logs
inspect_logs("detailed_login_logs.txt")