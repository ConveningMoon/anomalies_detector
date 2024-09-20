from data_stream import generate_energy_data_stream
from anomaly_detection import StreamAnomalyDetector
from visualization import plot_energy_stream
import numpy as np


def main():
    try:
        # Generate synthetic energy data
        data_stream = generate_energy_data_stream()
        # Initialize anomaly detector
        detector = StreamAnomalyDetector()
        # Use the first 24 data points to fit the initial model
        initial_batch = np.array(data_stream[:24])
        detector.fit_initial(initial_batch)

        # List to store anomaly status for each data point
        anomalies = []
        for data_point in data_stream:
            # Determine if the current data point is an anomaly
            anomaly = detector.detect(data_point)
            anomalies.append(anomaly)

        # Visualize the data stream and detected anomalies
        plot_energy_stream(data_stream, anomalies)

    except Exception as e:
        print(f"Error in main execution: {e}")
        raise


if __name__ == "__main__":
    # Execute main function
    main()
