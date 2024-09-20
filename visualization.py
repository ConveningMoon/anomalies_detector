import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.animation import FuncAnimation


def plot_energy_stream(data_stream, anomalies):
    """
    Plot and animate the energy data stream, highlighting anomalies.
    """
    try:
        if len(data_stream) != len(anomalies):
            raise ValueError("Data stream and anomalies list must be of the same length.")

        # Set up the figure and axis
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_title("Energy Data Stream with Anomalies")
        ax.set_xlabel("Time (Hours)")
        ax.set_ylabel("Energy Usage (kWh)")

        # Initialize line and points for streaming data and anomalies
        line, = ax.plot([], [], lw=2, label='Energy Stream', color='blue')
        anomaly_points, = ax.plot([], [], 'ro', label='Anomalies')
        ax.legend()

        # DataFrame to keep track of detected anomalies
        anomaly_df = pd.DataFrame(columns=['Index', 'Value'])

        def init():
            # Initialize the plot limits and data placeholders
            ax.set_xlim(0, len(data_stream))
            ax.set_ylim(np.min(data_stream) - 1, np.max(data_stream) + 1)
            line.set_data([], [])
            anomaly_points.set_data([], [])
            return line, anomaly_points

        def update(frame):
            # Update plot with new data up to current frame
            x_data = np.arange(frame)
            y_data = data_stream[:frame]
            line.set_data(x_data, y_data)

            # Collect and plot anomalies up to current frame
            anomaly_indices = [i for i in range(frame) if anomalies[i] == 1]
            anomaly_values = [data_stream[i] for i in anomaly_indices]
            anomaly_points.set_data(anomaly_indices, anomaly_values)

            # Record new anomalies in the DataFrame
            if anomalies[frame - 1] == 1:
                anomaly_df.loc[frame - 1] = [frame - 1, data_stream[frame - 1]]

            return line, anomaly_points

        # Function to save the anomalies DataFrame to a CSV file
        def save_anomalies_csv():
            try:
                anomaly_df.to_csv('anomalies.csv', index=False)
                print("Anomalies have been saved to 'anomalies.csv'.")
            except Exception as e:
                print(f"Error saving anomalies to CSV: {e}")
                raise

        # Set up the animation
        anim = FuncAnimation(fig, update, frames=np.arange(1, len(data_stream) + 1),
                             init_func=init, blit=True, interval=100, repeat=False)

        plt.show()

        # Save anomalies to CSV once the plot is closed
        save_anomalies_csv()

    except Exception as e:
        print(f"Error in visualization: {e}")
        raise
