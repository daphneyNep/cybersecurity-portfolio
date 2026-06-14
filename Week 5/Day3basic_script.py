import numpy as np
import matplotlib.pyplot as plt

# Generate normal data
normal_data = np.random.normal(loc=50, scale=5, size=100)

# Generate anomalous data (mean = 55, size = 20)
anomalous_data = np.random.normal(loc=55, scale=5, size=20)

# Combine the datasets
data = np.concatenate([normal_data, anomalous_data])

# Plot the data
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='blue', label='Data Distribution')

# Add lines for the means
plt.axvline(x=50, color='red', linestyle='dashed', linewidth=2, label='Normal Mean')
plt.axvline(x=55, color='green', linestyle='dashed', linewidth=2, label='Anomalous Mean')

# Labels and title
plt.title('Normal vs Anomalous Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Show the plot
plt.show()