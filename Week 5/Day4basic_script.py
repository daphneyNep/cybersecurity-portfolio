# Modified model output
model_output = {
    "user1": {"anomaly_score": 0.2, "flagged": False},
    "user2": {"anomaly_score": 0.95, "flagged": True},
    "user3": {"anomaly_score": 0.6, "flagged": True},
    "user4": {"anomaly_score": 0.3, "flagged": False},
}

# Display results
for user, details in model_output.items():
    print(
        f"{user}: Anomaly Score = {details['anomaly_score']}, "
        f"Flagged = {details['flagged']}"
    )