# Simulated login attempts
login_attempts = [
    {"user": "user1", "success": True},
    {"user": "user2", "success": False},
    {"user": "user3", "success": False},
    {"user": "user4", "success": True},
]

# Automated monitoring
for attempt in login_attempts:
    if not attempt["success"]:
        print(f"Alert: {attempt['user']} failed to log in!")
    else:
        print(f"{attempt['user']} logged in successfully.")