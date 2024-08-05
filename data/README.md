# Data Directory

This directory contains various datasets prepared for modeling in the "Healthcare Market Saturation and Fraud" project. The files include different versions of data for training, validation, and testing, including those with scaling and PCA transformations applied.

## Files

- **X_test.csv**: Additional CSV prepared for modeling data. Contains features for testing.
- **X_val.csv**: Additional CSV prepared for modeling data. Contains features for validation.
- **cms_data.csv**: Contains raw CMS data files used in the project.
- **cms_data_sql.csv**: Contains CMS data with corrected column names for SQL compatibility.
- **x_test_pca.csv**: Features for testing after PCA (Principal Component Analysis) transformation.
- **x_test_scaled.csv**: Features for testing after scaling transformation.
- **x_test_scaled_pca.csv**: Features for testing after both scaling and PCA transformations.
- **x_train.csv**: Additional CSV prepared for modeling data. Contains features for training.
- **x_train_pca.csv**: Features for training after PCA transformation.
- **x_train_scaled.csv**: Features for training after scaling transformation.
- **x_train_scaled_pca.csv**: Features for training after both scaling and PCA transformations.
- **x_val_pca.csv**: Features for validation after PCA transformation.
- **x_val_scaled.csv**: Features for validation after scaling transformation.
- **x_val_scaled_pca.csv**: Features for validation after both scaling and PCA transformations.
- **y_test.csv**: Labels for testing data.
- **y_train.csv**: Labels for training data.
- **y_train_scaled.csv**: Labels for training data after scaling transformation.
- **y_val.csv**: Labels for validation data.

## Description

- **`X_*.csv`** files: Contain feature data for different stages of preprocessing and transformations, such as scaling and PCA.
- **`y_*.csv`** files: Contain the corresponding labels for the datasets.
- **`cms_data.csv` and `cms_data_sql.csv`**: Raw and SQL-compatible CMS data files, respectively.

## Usage

These datasets are used for building and evaluating models. Ensure you use the correct version of the dataset for your modeling needs and preprocessing steps.


