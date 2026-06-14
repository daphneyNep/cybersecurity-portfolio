from datetime import datetime, timedelta

# Sample login log entries with timestamps
login_logs = [
    "2023-10-01 10:00:00 user1 SUCCESS",
    "2023-10-01 10:01:00 user2 FAILED",
    "2023-10-01 10:02:00 user1 FAILED",
    "2023-10-01 10:03:00 user2 FAILED",
    "2023-10-01 10:04:00 user2 FAILED",
    "2023-10-01 10:05:00 admin SUCCESS",
]

# Dictionary to track failed attempts
failed_attempts = {}

# Parse the logs and store failed attempt timestamps
for log in login_logs:
    parts = log.split()

    if len(parts) < 4:
        continue

    timestamp_str = parts[0] + " " + parts[1]
    username = parts[2]
    status = parts[3]

    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    if status == "FAILED":
        if username not in failed_attempts:
            failed_attempts[username] = []

        failed_attempts[username].append(timestamp)

# Check for suspicious behavior
threshold_time = timedelta(minutes=5)
suspicious_found = False

for user, attempts in failed_attempts.items():
    if len(attempts) > 2:
        first_attempt_time = attempts[0]
        last_attempt_time = attempts[-1]

        if last_attempt_time - first_attempt_time <= threshold_time:
            suspicious_found = True

            print(
                f"Suspicious behavior detected for {user}: "
                f"{len(attempts)} failed attempts within 5 minutes."
            )

            # Display timestamps
            formatted_times = [
                attempt.strftime("%Y-%m-%d %H:%M:%S")
                for attempt in attempts
            ]

            print(f"Failed attempt timestamps: {formatted_times}")
            print()

# If no suspicious behavior is detected
if not suspicious_found:
    print("No suspicious behavior detected.")