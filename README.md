# Data Stream Anomaly Detector

## Install Required Packages
```bash
  pip install -r requirements.txt
```

## Project Description
This software system is engineered to identify anomalies within a continuous stream of data in real-time. To achieve this objective, the project has been structured into four distinct modules using Python:

### Module `data_stream.py`:

The `data_stream.py` module is responsible for simulating a continuous data stream that mimics real-world scenarios, particularly focusing on energy consumption data. It generates synthetic data incorporating daily and weekly patterns, alongside random noise and intentional anomalies to reflect realistic operational conditions.

**Core Functionality:**
- **Daily/Weekly Pattern Simulation**: It models energy usage using a sinusoidal (sine wave) pattern, repeated across the duration of the simulated week. This reflects typical cyclical behavior in energy consumption.
- **Noise Addition**: Random noise is introduced using a normal distribution to represent natural fluctuations and irregularities observed in actual data.
- **Anomaly Injection**: Regularly spaced anomalies are added by injecting spikes at specified intervals, simulating unexpected events or outliers in the data stream.

**Logic Flow:**
1. **Parameter Validation**: Before data simulation begins, the function checks that parameters like `hours` and `anomaly_freq` are positive integers, preventing erroneous inputs.
2. **Pattern Generation**: A base sine wave pattern is created to simulate predictable, periodic energy consumption.
3. **Variability Integration**: Random variations are computed and applied to the sine wave, enhancing the data's authenticity by simulating day-to-day consumption changes.
4. **Noise Enhancement**: Additional Gaussian noise is overlaid, further diversifying the stream to closely match stochastic elements found in real data.
5. **Anomaly Addition**: Spikes, modeled as anomalies, are introduced at regular intervals to emulate abnormal or unusual conditions in the data.

**Output**: The function returns an array representing the synthesized data stream, suitable for testing and validating anomaly detection methods.

Through this module, users can produce and experiment with richly varied data, key for developing and tuning anomaly detection algorithms.

### Module `anomaly_detection.py`:

The `anomaly_detection.py` module is designed to detect anomalies in streaming data using advanced machine learning techniques. It incorporates adaptive algorithms to identify irregularities in the data effectively, adapting to new patterns over time.

**Core Functionality:**

- **Model Initialization**: The module utilizes Isolation Forest for anomaly detection, a robust algorithm that isolates anomalies based on the idea of random data partitioning. Incremental PCA is employed for dimensionality reduction, which helps in adapting to streaming data efficiently.

- **Initial Model Fitting**: Before real-time detection, the model is initially trained on a set of historical data, allowing it to establish a baseline understanding of normal behavior.

- **Real-time Detection**: As new data comes in, the module continuously buffers data points, periodically checking for anomalies when enough data is accumulated.

- **Model Updating**: The model adapts to new data distributions over time by periodically retraining with the latest data points, ensuring it remains accurate even as data patterns evolve.

**Logic Flow:**

1. **Initialization**: Upon instantiation, the detector sets up model parameters, including a buffer to store a window of the most recent data points for analysis.
2. **Initial Fitting**: Using a specified batch of initial data, the model trains the PCA to identify significant dimensions and the Isolation Forest to learn normal data distribution.
3. **Data Handling and Anomaly Detection**:
   * New data points are added to the buffer.
   * Once the buffer is full, the latest data batch is transformed via PCA, and the transformed data is checked for anomalies using the Isolation Forest.
   * Anomaly results are returned for the latest data point.
4. **Model Updating**: When the buffer is used for detection, the model is retrained with this recent data, ensuring adaptation to any new trends or patterns that may emerge.

**Output**: The class returns anomaly detection outcomes for each data point, indicating whether it is considered an anomaly within the context of the current data environment.

This module offers a scalable and effective approach to anomaly detection, capable of adapting to changes in data characteristics over time, thus making it ideal for use in dynamic data streams.

### Module `visualization.py`:

The `visualization.py` module is designed to provide a real-time graphical representation of a data stream, highlighting anomalies as they are detected. This module enables users to visualize patterns and outliers, facilitating a deeper understanding of the data's behavior over time.

**Core Functionality:**
- **Real-Time Data Visualization**: It uses `matplotlib` to plot the data stream dynamically, with continuous updates to simulate live data feed.
- **Anomaly Highlighting**: Detected anomalies are marked on the graph, using different colors (e.g., red) to differentiate them from normal data points.
- **Anomaly Logging**: Anomalies are logged into a `pandas.DataFrame`, which is subsequently saved to a CSV file for post-analysis once the visualization session ends.

**Logic Flow:**
1. **Initialization**: The function sets up the plot with relevant labels and initializes graphical elements for both the data line and anomalies.
2. **Data Streaming Simulation**:
   * The `FuncAnimation` function dynamically updates the plot, simulating data points appearing one by one as if they are emerging in real-time.
   * For each frame (a new data point), the line data on the plot is updated to include all the data points up to the current time.
3. **Anomaly Detection Visualization**:
   * As anomalies are detected in the data stream, these points are highlighted on the plot, offering immediate visual feedback to the user.
4. **End-of-Session Processing**:
   * Upon completion or closure of the plot, the recorded anomalies are exported as a CSV file.
   * This dataset includes the indices and values of anomalies, serving as a reference for further exploration or model evaluation.

**Output**: Users interact with a continuously updating graph, and results are documented in a CSV file, supporting ongoing analysis and review.

This module effectively bridges data processing with visual representation, enhancing the interpretability of anomaly detection processes in streaming applications.

## Mathematical Explanation

### Anomaly Detection Methodology

The project uses the following key techniques:

- **Isolation Forest**: A tree-based anomaly detection algorithm well-suited for identifying rare and varied anomalous patterns. It isolates anomalies by randomly partitioning the data space, effectively separating anomalies faster than normal points.

- **Incremental PCA**: Reduces dimensionality by finding principal components incrementally. This is essential for reducing noise and adapting the model to changes in streaming data.

### Why These Libraries?

- **scikit-learn**: Offers robust implementations of Isolation Forest and Incremental PCA, providing efficiency and good documentation (the PyOD library could be used also, specifically designed for anomaly detection. However, in the interest of maintaining a minimal reliance on external libraries for the prototype and for personal experience, I proceeded using sklearn).
- **NumPy**: Essential for fast mathematical operations and data manipulation in Python.
- **Matplotlib**: Used for plotting real-time updates of data and visualizing anomalies.

## Visual Output

- As the script runs, a matplotlib window opens, displaying the data stream with detected anomalies. Anomalies are plotted in red.

- **After execution**, a CSV file named `anomalies.csv` is saved, containing the indices and values of detected anomalies for further analysis.

## Error Handling

Robust error handling is integrated into the project to ensure smooth operation and meaningful error reporting. Key areas of error management include:

- **Data Input Validation**: Validates the size and format of incoming data, whether initial or streaming.
- **Model Handling**: Catches exceptions during model training and prediction, providing informative error messages.
- **Visualization**: Ensures the lengths of input lists are compatible and reports issues when saving output.

## Conclusion
This project provides an efficient and automated approach to detecting anomalies in streaming data, leveraging powerful statistical methods and visualization tools. Through the use of robust algorithms and libraries and detailed error handling, it ensures precision and resilience in anomaly detection tasks.

For any questions or contributions, please feel free to reach out or submit a pull request. I actually really enjoyed developing this system, so any recommendations are welcome! :)

## Resources
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## Credits
In spite of my prior experience with Sklearn, the completion of this project would have been significantly delayed without the invaluable support provided by the official documentation and the community contributions on StackOverflow. I would also like to extend special gratitude to my colleague, Marcelo, a mathematician, whose expertise I consulted for gaining insights into optimal dimensionality reduction techniques and the creation of sinusoidal and normal patterns to generate more realistic data.  
