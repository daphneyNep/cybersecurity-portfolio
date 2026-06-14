# Sample login log entries
login_logs = [
    "2023-10-01 10:00:00 user1 SUCCESS",
    "2023-10-01 10:01:00 user2 FAILED",
    "2023-10-01 10:02:00 user1 FAILED",
    "2023-10-01 10:03:00 admin SUCCESS",
    "2023-10-01 10:04:00 user2 FAILED",
]

# Dictionary to track failed login attempts
failed_attempts = {}

# Parse the logs and identify failed attempts
for log in login_logs:
    parts = log.rsplit(' ', 1)  # Split from the right into 2 parts
    status = parts[-1]  # The status is the last part
    username = parts[0].rsplit(' ', 1)[-1]  # Get the username from the first part
    timestamp = parts[0][:-len(username)-1]  # Get the timestamp

    if status == "FAILED":
        print(f"Failed login attempt by {username} at {timestamp}.")

        # Increment the failed attempt count
        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1

# Display total failed attempts per user
print("\nTotal Failed Login Attempts:")
for user, count in failed_attempts.items():
    print(f"{user}: {count}")
    
