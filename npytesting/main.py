import numpy as np

# Simulating structured data with multiple fields per entry
structured_data = np.zeros(5, dtype=[('id', 'i4'), ('temperature', 'f4'), ('humidity', 'f4')])
structured_data['id'] = np.arange(1, 6)
structured_data['temperature'] = np.random.uniform(20, 30, 5)
structured_data['humidity'] = np.random.uniform(40, 60, 5)

# Save the structured array to a .npy file
np.save("data.npy", structured_data)
