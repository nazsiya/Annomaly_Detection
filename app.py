from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained anomaly detection model
with open('annomaly_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Relevant features used during training
    relevant_features = ['Transaction_Amount', 'Average_Transaction_Amount', 'Frequency_of_Transactions']

    # Get user inputs from the form
    user_inputs = [float(request.form[feature]) for feature in relevant_features]

    # Create a DataFrame from user inputs
    user_df = pd.DataFrame([user_inputs], columns=relevant_features)

    # Predict anomalies using the model
    user_anomaly_pred = model.predict(user_df)

    # Convert the prediction to binary value (0: normal, 1: anomaly)
    user_anomaly_pred_binary = 1 if user_anomaly_pred == -1 else 0

    return render_template('result.html', anomaly_detected=user_anomaly_pred_binary)

if __name__ == '__main__':
    app.run(debug=True)
