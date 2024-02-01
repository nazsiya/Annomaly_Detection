# Annomaly Detection

# Overview
This repository demonstrates anomaly detection in transactions using Python. The process involves importing necessary libraries, exploring the dataset, analyzing data insights, visualizing distributions, and training an Isolation Forest model for anomaly detection. The README provides step-by-step explanations and code snippets.

# Dataset
The dataset consists of transaction details, including Transaction Amount, Transaction Volume, Average Transaction Amount, Frequency of Transactions, Time Since Last Transaction, Day of the Week, Time of Day, Age, Gender, Income, and Account Type. A sample is presented in the README.

# Exploratory Data Analysis (EDA)
EDA is performed to understand the dataset. Null values, data types, and descriptive statistics are analyzed. Visualizations, such as histograms, box plots, and scatter plots, are used to explore transaction patterns and relationships.

# Correlation Heatmap
A correlation heatmap is generated to understand the relationships between different columns in the dataset.

# Anomaly Detection
Anomalies are detected by calculating mean and standard deviation of Transaction Amount, defining an anomaly threshold, and flagging anomalies. Visualizations highlight anomalies in scatter plots.

# Model Training
An Isolation Forest model is trained on relevant features (Transaction Amount, Average Transaction Amount, Frequency of Transactions) using a dataset split into training and testing sets.

# Model Evaluation
The model's performance is evaluated on the test set using precision, recall, and F1-score metrics. The high accuracy indicates successful anomaly detection.

# User Input and Prediction
Relevant features are gathered from user input, and the trained model predicts anomalies. The result is displayed, indicating whether the transaction is normal or flagged as an anomaly.

# How to Use
Clone the repository to your local machine.
Install required dependencies using pip install -r requirements.txt.
Run the Flask app using python app.py.
Access the web app in your browser at http://127.0.0.1:5000/.
Enter transaction details and click "Predict" to see the anomaly detection result.

# Contributing
Contributions, suggestions, bug reports, or enhancements are welcome. Feel free to open an issue or submit a pull request.
