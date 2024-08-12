# Models Directory

This directory contains the pre-trained models used in the "Healthcare Market Saturation and Fraud" project. The models have been trained and saved for various machine learning algorithms, and can be used for evaluation and inference.

## Files

- **`ada_best_model.joblib`**: The best performing AdaBoost model, saved in Joblib format.
- **`ada_best_model.pkl`**: The best performing AdaBoost model, saved in Pickle format.
- **`bag_best_model.joblib`**: The best performing Bagging Classifier model, saved in Joblib format.
- **`bag_best_model.pkl`**: The best performing Bagging Classifier model, saved in Pickle format.
- **`lasso_best_model.joblib`**: The best performing Lasso Regression model, saved in Joblib format.
- **`lasso_best_model.pkl`**: The best performing Lasso Regression model, saved in Pickle format.
- **`logreg_best_model.joblib`**: The best performing Logistic Regression model, saved in Joblib format.
- **`logreg_best_model.pkl`**: The best performing Logistic Regression model, saved in Pickle format.
- **`nn_best_model.joblib`**: The best performing Neural Network model, saved in Joblib format.
- **`nn_best_model.pkl`**: The best performing Neural Network model, saved in Pickle format.
- **`qda_best_model.joblib`**: The best performing Quadratic Discriminant Analysis model, saved in Joblib format.
- **`qda_best_model.pkl`**: The best performing Quadratic Discriminant Analysis model, saved in Pickle format.
- **`ridge_best_model.joblib`**: The best performing Ridge Regression model, saved in Joblib format.
- **`ridge_best_model.pkl`**: The best performing Ridge Regression model, saved in Pickle format.
- **`sgd_best_model.joblib`**: The best performing Stochastic Gradient Descent model, saved in Joblib format.
- **`sgd_best_model.pkl`**: The best performing Stochastic Gradient Descent model, saved in Pickle format.
- **`svm_best_model.joblib`**: The best performing Support Vector Machine model, saved in Joblib format.
- **`svm_best_model.pkl`**: The best performing Support Vector Machine model, saved in Pickle format.
- **`xgb_best_model.joblib`**: The best performing XGBoost model, saved in Joblib format.
- **`xgb_best_model.pkl`**: The best performing XGBoost model, saved in Pickle format.

## Usage

To use any of the models, load the corresponding file using the appropriate library (e.g., `pickle` for `.pkl` files) in your Python environment. Ensure that you have the necessary libraries installed to use these models.

Example of loading a Pickle model:

```
import pickle

with open('models/bag_best_model.pkl', 'rb') as file:
    model = pickle.load(file)
```

Example of loading a Joblib model: 
```
import joblib

model = joblib.load('models/bag_best_model.joblib')
``` 
