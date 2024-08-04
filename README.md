# Uncovering Healthcare Inefficiencies: Data-Driven Solutions for Market Saturation and Fraud

This project, part of the ADS-599 course in the Applied Data Science Program at the University of San Diego, aims to uncover inefficiencies in healthcare service delivery using the Market Saturation and Utilization State-County dataset from the Centers for Medicare & Medicaid Services (CMS). By analyzing healthcare provider saturation, the project seeks to identify potential fraud, waste, and abuse (FWA) and offer actionable insights for improving healthcare resource allocation.

## Contributors

- [Jessica Hin](https://github.com/JessicaH123) (@JessicaH123)
- [Amy Ou](https://github.com/amyou518) (@amyou518)
- [Samantha Rivas](https://github.com/samantharivas) (@samantharivas)

# Table of Contents

1. [Project Overview](#project-overview)
2. [Contributors](#contributors)
3. [Installation](#installation)
4. [Methods Used](#methods-used)
5. [Technologies](#technologies)
6. [Project Description](#project-description)
    - [Dataset](#dataset)
    - [Data Dictionary](#data-dictionary)
    - [Questions and Hypotheses](#questions-and-hypotheses)
    - [Analysis and Modeling](#analysis-and-modeling)
    - [Challenges](#challenges)
7. [Repository Contents](#repository-contents)
    - [Flask Application Files](#flask-application-files)
    - [Data Files](#data-files)
    - [Machine Learning Models](#machine-learning-models)
    - [Tableau Visualizations](#tableau-visualizations)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

## Installation

To replicate this analysis on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/samantharivas/healthcare-market-saturation-fraud.git
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Navigate to each directory (e.g., `data`, `Flask_app_files`) and follow the setup instructions provided in their respective `README.md` files.**

5. **Run the Jupyter notebooks for data exploration and modeling:**
    - Open and run `Preprocessing.ipynb` for data cleaning and preparation.
    - Open and run `Modeling.ipynb` for building and evaluating predictive models.

## Methods Used

- **Inferential Statistics**
- **Data Mining**
- **Predictive Modeling**
- **Machine Learning**
- **Data Visualization**
- **Data Engineering**
- **Data Manipulation**

## Technologies

- **Python**
- **SQL**
- **Jupyter Notebook**
- **Tableau**
- **Flask** (for deploying models and creating a GUI)

## Project Description

### Dataset

The project utilizes the [CMS Market Saturation and Utilization State-County dataset](https://data.cms.gov/summary-statistics-on-use-and-payments/program-integrity-market-saturation-by-type-of-service/market-saturation-utilization-state-county).

- **Number of Variables**: 49
- **Size of Dataset**: 1,044,711 rows

### Data Dictionary

For detailed descriptions of each variable, refer to the [data dictionary](https://data.cms.gov/resources/market-saturation-utilization-state-county-data-dictionary).

### Questions and Hypotheses

- What patterns indicate potential fraud, waste, and abuse in healthcare services?
- How does market saturation correlate with inefficiencies in healthcare delivery?

### Analysis and Modeling

- **Preprocessing**: Handle missing values and ensure data quality.
- **Exploratory Data Analysis (EDA)**: Uncover initial insights from the data.
- **Model Building**: Create and evaluate predictive models for detecting FWA.
- **Visualization**: Use Tableau to create visualizations that enhance interpretability.

### Challenges

- Efficiently handling large datasets.
- Ensuring data quality and consistency.
- Selecting and tuning appropriate models.

## Repository Contents

### `/Flask_app_files/`

Files related to the Flask application used for model deployment and GUI:

- **`fwa_app.py`**: Main script for the Flask application.
- **`encoder.pkl`**: Serialized encoder for data preprocessing.
- **`scaler.pkl`**: Serialized scaler for data normalization.
- **`xgb_best_model.pkl`**: Serialized best XGBoost model.

### `/data/`

Datasets and processed data used for modeling:

- **`cms_data.csv`**: Raw data file from CMS.
- **`X_train.csv`**, **`X_test.csv`**, **`X_val.csv`**: Prepared feature datasets.
- **`y_train.csv`**, **`y_test.csv`**, **`y_val.csv`**: Target variables.
- **`x_train_scaled.csv`**, **`x_test_scaled.csv`**, **`x_val_scaled.csv`**: Scaled feature data.
- **`x_train_pca.csv`**, **`x_test_pca.csv`**, **`x_val_pca.csv`**: PCA-transformed feature data.

### `/models/`

Trained machine learning models:

- **`xgb_best_model.pkl`**: Best XGBoost model.
- **`logreg_best_model.pkl`**: Best Logistic Regression model.
- **`lasso_best_model.pkl`**: Best Lasso model.
- **`ridge_best_model.pkl`**: Best Ridge model.
- **`sgd_best_model.pkl`**: Best Stochastic Gradient Descent model.

### `/tableau-visualizations/`

Tableau visualization files:

- **`beneficiaries.twbx`**: Workbook for visualizing beneficiary data.
- **`dual-eligibility.twbx`**: Workbook for visualizing dual eligibility data.
- **`providers.twbx`**: Workbook for visualizing provider data.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

We would like to thank our professor and mentors for their guidance throughout this project. Special thanks to the University of San Diego for providing the resources and support necessary to complete this project.
