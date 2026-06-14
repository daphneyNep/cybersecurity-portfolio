# Simulated alerts with potential bias
alerts = [
    {"user": "user1", "threat_level": "low", "flagged": False},
    {"user": "user2", "threat_level": "high", "flagged": True},
    {"user": "user3", "threat_level": "medium", "flagged": True},
    {"user": "user4", "threat_level": "low", "flagged": False},
    {"user": "user5", "threat_level": "high", "flagged": True},
]

# Ethical considerations in alerting
for alert in alerts:
    if alert["flagged"]:
        print(f"Alert: {alert['user']} has a {alert['threat_level']} threat level.")
    else:
        print(f"{alert['user']} is not flagged.")