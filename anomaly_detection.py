from sklearn.ensemble import IsolationForest
import numpy as np
from sklearn.decomposition import IncrementalPCA

class StreamAnomalyDetector:
    def __init__(self, window_size=24):
        if window_size <= 0:
            raise ValueError("Window size must be a positive integer.")
        # Set the size of the window for data buffering
        self.window_size = window_size
        # Initialize Incremental PCA for dimensionality reduction
        self.ipca = IncrementalPCA(n_components=1)
        # Initialize the Isolation Forest model for anomaly detection
        self.detector = IsolationForest(contamination=0.05, random_state=42)
        # Buffer to hold recent data points
        self.buffer = []

    def fit_initial(self, data):
        try:
            if len(data) < self.window_size:
                raise ValueError("Initial data size is less than window size.")
            # Reshape data for compatibility with PCA
            data = np.array(data).reshape(-1, 1)
            # Fit PCA model to initial data
            reduced_data = self.ipca.fit_transform(data)
            # Train Isolation Forest on reduced data
            self.detector.fit(reduced_data)
        except Exception as e:
            print(f"Error during initial fit: {e}")
            raise

    def detect(self, new_data):
        try:
            if not isinstance(new_data, (int, float)):
                raise ValueError("New data point must be a number.")

            # Reshape new data point
            new_data = np.array([new_data]).reshape(1, -1)
            # Add new data point to buffer
            self.buffer.append(new_data)

            # Once buffer is full, perform detection
            if len(self.buffer) >= self.window_size:
                # Stack buffered data into an array
                batched_data = np.vstack(self.buffer[-self.window_size:])
                # Transform data using PCA
                reduced_data = self.ipca.transform(batched_data)
                # Predict anomalies using Isolation Forest
                anomalies = self.detector.predict(reduced_data)
                # Maintain buffer size
                self.buffer = self.buffer[-self.window_size:]
                # Update model for dynamic adaptation
                self.update_model()
                # Return the anomaly status of the latest data point
                return 1 if anomalies[-1] == -1 else 0
            else:
                return 0  # Return 0 if not enough data to determine anomaly
        except Exception as e:
            print(f"Error during detection: {e}")
            raise

    def update_model(self):
        try:
            # Retrain the PCA and the Isolation Forest on the current buffer of data
            if len(self.buffer) >= self.window_size:
                # Take the current batch for model updating
                batched_data = np.vstack(self.buffer[-self.window_size:])
                # Fit PCA and Isolation Forest with the new batch
                reduced_data = self.ipca.fit_transform(batched_data)
                self.detector.fit(reduced_data)
        except Exception as e:
            print(f"Error during model update: {e}")
            raise
