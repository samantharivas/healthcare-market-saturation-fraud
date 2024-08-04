# Models Directory

This directory contains the pre-trained models used in the "Healthcare Market Saturation and Fraud" project. The models have been trained and saved for various machine learning algorithms, and can be used for evaluation and inference.

## Files

- **bag_best_model.zip**: A ZIP archive containing the best performing Bagging model.
- **lasso_best_model.pkl**: The best performing Lasso Regression model, saved in Pickle format.
- **logreg_best_model.pkl**: The best performing Logistic Regression model, saved in Pickle format.
- **ridge_best_model.pkl**: The best performing Ridge Regression model, saved in Pickle format.
- **sgd_best_model.pkl**: The best performing Stochastic Gradient Descent model, saved in Pickle format.
- **xgb_best_model.pkl**: The best performing XGBoost model, saved in Pickle format.


## Usage

To use any of the models, load the corresponding file using the appropriate library (e.g., `pickle` for `.pkl` files) in your Python environment. Ensure that you have the necessary libraries installed to use these models.

Example of loading a Pickle model:

```python
import pickle

with open('models/lasso_best_model.pkl', 'rb') as file:
    model = pickle.load(file)
```
