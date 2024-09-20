import numpy as np


def generate_energy_data_stream(hours=168, anomaly_freq=30):
    if hours <= 0:
        raise ValueError("Hours must be a positive integer.")
    if anomaly_freq <= 0:
        raise ValueError("Anomaly frequency must be a positive integer.")

    # Set a random seed for reproducibility
    np.random.seed(42)

    # Generate a daily pattern using a sine wave repeated across the week
    daily_pattern = np.sin(np.linspace(0, 2 * np.pi, 24))
    week_pattern = np.tile(daily_pattern, int(hours / 24))

    # Apply random variation to simulate real-world energy consumption fluctuations
    week_variation = np.random.normal(1.0, 0.1, hours)
    data = week_pattern * week_variation

    # Introduce random noise into the data
    noise = np.random.normal(0, 0.05, hours)
    data = data + noise

    # Introduce periodic anomalies at specified frequency
    for i in range(0, hours, anomaly_freq):
        data[i] = data[i] + np.random.normal(5, 1)  # Anomaly as a spike in usage

    return data  # Return the simulated energy data stream

