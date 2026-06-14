# Capture user input for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Display the captured input
print(f"Username: {username}")
print("Password: [hidden]")  # Hide the actual password

# Check the user's role
if username == "admin":
    print("Admin access granted.")
else:
    print("Regular user access.")