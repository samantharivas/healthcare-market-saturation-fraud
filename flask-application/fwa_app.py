from flask import Flask, render_template, request, jsonify
import pickle

import joblib
import pandas as pd
import os

# Create Flask app instance
app = Flask(__name__)

# Load preprocessing components and model
with open('binary_encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('pca.pkl', 'rb') as file:
    pca = pickle.load(file)

with open('bag_best_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Collect data from the form
    form_data = {
        'type_of_service': request.form['type_of_service'],
        'state': request.form['state'],
        'county': request.form['county'],
        'number_of_fee_for_service_beneficiaries': float(request.form['number_of_fee_for_service_beneficiaries']),
        'number_of_providers': float(request.form['number_of_providers']),
        'average_number_of_users_per_provider': float(request.form['average_number_of_users_per_provider']),
        'percentage_of_users_out_of_ffs_beneficiaries': float(request.form['percentage_of_users_out_of_ffs_beneficiaries']),
        'number_of_users': float(request.form['number_of_users']),
        'average_number_of_providers_per_county': float(request.form['average_number_of_providers_per_county']),
        'percentage_of_dual_eligible_users_out_of_total_users': float(request.form['percentage_of_dual_eligible_users_out_of_total_users']),
        'total_payment': float(request.form['total_payment']),
        'number_of_fee_for_service_beneficiaries_dual_color_1': request.form['number_of_fee_for_service_beneficiaries_dual_color_1'],
        'number_of_fee_for_service_beneficiaries_dual_color_2': request.form['number_of_fee_for_service_beneficiaries_dual_color_2'],
        'number_of_fee_for_service_beneficiaries_dual_color_3': request.form['number_of_fee_for_service_beneficiaries_dual_color_3'],
        'number_of_fee_for_service_beneficiaries_dual_color_4': request.form['number_of_fee_for_service_beneficiaries_dual_color_4'],
        'number_of_fee_for_service_beneficiaries_dual_color_5': request.form['number_of_fee_for_service_beneficiaries_dual_color_5'],
        'number_of_providers_dual_color_1': request.form['number_of_providers_dual_color_1'],
        'number_of_providers_dual_color_2': request.form['number_of_providers_dual_color_2'],
        'number_of_providers_dual_color_3': request.form['number_of_providers_dual_color_3'],
        'number_of_providers_dual_color_4': request.form['number_of_providers_dual_color_4'],
        'number_of_providers_dual_color_5': request.form['number_of_providers_dual_color_5'],
        'average_number_of_users_per_provider_dual_color_1': request.form['average_number_of_users_per_provider_dual_color_1'],
        'average_number_of_users_per_provider_dual_color_2': request.form['average_number_of_users_per_provider_dual_color_2'],
        'average_number_of_users_per_provider_dual_color_3': request.form['average_number_of_users_per_provider_dual_color_3'],
        'average_number_of_users_per_provider_dual_color_4': request.form['average_number_of_users_per_provider_dual_color_4'],
        'average_number_of_users_per_provider_dual_color_5': request.form['average_number_of_users_per_provider_dual_color_5'],
        'percentage_of_users_out_of_ffs_beneficiaries_dual_color_1': request.form['percentage_of_users_out_of_ffs_beneficiaries_dual_color_1'],
        'percentage_of_users_out_of_ffs_beneficiaries_dual_color_2': request.form['percentage_of_users_out_of_ffs_beneficiaries_dual_color_2'],
        'percentage_of_users_out_of_ffs_beneficiaries_dual_color_3': request.form['percentage_of_users_out_of_ffs_beneficiaries_dual_color_3'],
        'percentage_of_users_out_of_ffs_beneficiaries_dual_color_4': request.form['percentage_of_users_out_of_ffs_beneficiaries_dual_color_4'],
        'percentage_of_users_out_of_ffs_beneficiaries_dual_color_5': request.form['percentage_of_users_out_of_ffs_beneficiaries_dual_color_5'],
        'number_of_users_dual_color_1': request.form['number_of_users_dual_color_1'],
        'number_of_users_dual_color_2': request.form['number_of_users_dual_color_2'],
        'number_of_users_dual_color_3': request.form['number_of_users_dual_color_3'],
        'number_of_users_dual_color_4': request.form['number_of_users_dual_color_4'],
        'number_of_users_dual_color_5': request.form['number_of_users_dual_color_5'],
        'average_number_of_providers_per_county_dual_color_1': request.form['average_number_of_providers_per_county_dual_color_1'],
        'average_number_of_providers_per_county_dual_color_2': request.form['average_number_of_providers_per_county_dual_color_2'],
        'average_number_of_providers_per_county_dual_color_3': request.form['average_number_of_providers_per_county_dual_color_3'],
        'average_number_of_providers_per_county_dual_color_4': request.form['average_number_of_providers_per_county_dual_color_4'],
        'average_number_of_providers_per_county_dual_color_5': request.form['average_number_of_providers_per_county_dual_color_5'],
        'number_of_dual_eligible_users_dual_color_1': request.form['number_of_dual_eligible_users_dual_color_1'],
        'number_of_dual_eligible_users_dual_color_2': request.form['number_of_dual_eligible_users_dual_color_2'],
        'number_of_dual_eligible_users_dual_color_3': request.form['number_of_dual_eligible_users_dual_color_3'],
        'number_of_dual_eligible_users_dual_color_4': request.form['number_of_dual_eligible_users_dual_color_4'],
        'number_of_dual_eligible_users_dual_color_5': request.form['number_of_dual_eligible_users_dual_color_5'],
        'percentage_of_dual_eligible_users_out_of_total_users_dual_color_1': request.form['percentage_of_dual_eligible_users_out_of_total_users_dual_color_1'],
        'percentage_of_dual_eligible_users_out_of_total_users_dual_color_2': request.form['percentage_of_dual_eligible_users_out_of_total_users_dual_color_2'],
        'percentage_of_dual_eligible_users_out_of_total_users_dual_color_3': request.form['percentage_of_dual_eligible_users_out_of_total_users_dual_color_3'],
        'percentage_of_dual_eligible_users_out_of_total_users_dual_color_4': request.form['percentage_of_dual_eligible_users_out_of_total_users_dual_color_4'],
        'percentage_of_dual_eligible_users_out_of_total_users_dual_color_5': request.form['percentage_of_dual_eligible_users_out_of_total_users_dual_color_5'],
        'percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_1': request.form['percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_1'],
        'percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_2': request.form['percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_2'],
        'percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_3': request.form['percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_3'],
        'percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_4': request.form['percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_4'],
        'percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_5': request.form['percentage_of_dual_eligible_users_out_of_dual_eligible_ffs_beneficiaries_dual_color_5'],
        'total_payment_dual_color_1': request.form['total_payment_dual_color_1'],
        'total_payment_dual_color_2': request.form['total_payment_dual_color_2'],
        'total_payment_dual_color_3': request.form['total_payment_dual_color_3'],
        'total_payment_dual_color_4': request.form['total_payment_dual_color_4'],
        'total_payment_dual_color_5': request.form['total_payment_dual_color_5']
    }
    
    # Create DataFrame
    df = pd.DataFrame([form_data])

    # create list of numeric columns
    x_train_num_cols = df.select_dtypes(include=['float'])
    x_train_num_cols = x_train_num_cols.columns.tolist()
    
    # Apply binary encoding, scaling, and PCA
    X_encoded = encoder.transform(df)  # Apply binary encoding
    X_scaled = X_encoded.copy()
    X_scaled[x_train_num_cols] = scaler.transform(X_encoded[x_train_num_cols])  # Apply scaling
    X_pca = pca.transform(X_scaled)  # Apply PCA
    
    # Make prediction
    prediction = model.predict(X_pca)

    if int(prediction[0]) == 0:
        return jsonify({'prediction': '0 - Not a potential fraud, waste, and abuse candidate'})
    
    if int(prediction[0]) == 1:
        return jsonify({'prediction': '1 - A potential fraud, waste, and abuse candidate'})
    
    #return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, port=1000)