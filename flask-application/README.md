# Flask Application for Healthcare Fraud Detection

This Flask application allows users to interact with a predictive model designed for detecting healthcare fraud based on various features.

**Link to Flask app**: [Healthcare Fraud Detection Flask App](https://bit.ly/ad599_fwa_model)

## Table of Contents

1. [Usage](#usage)
   - [Setting Up the Flask Application](#setting-up-the-flask-application)
   - [Using the Application](#using-the-application)
2. [Additional Notes](#additional-notes)
3. [Files and Directories](#files-and-directories)

## Usage

### Setting Up the Flask Application

1. **Ensure Python is Installed**

   Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**

   Navigate to the Flask application directory and install the required dependencies:

   ```bash
   pip install -r Flask_app_files/requirements.txt
   ```

3. **Navigate to the Flask Application Directory**

   Change to the directory containing the Flask application files:

   ```bash
   cd Flask_app_files
   ```

4. **Create and Activate a Virtual Environment (Optional but Recommended)**

   - Create a virtual environment:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:

     - On macOS/Linux:

       ```bash
       source venv/bin/activate
       ```

     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

5. **Run the Flask Application**

   Start the Flask application with the following command:

   ```bash
   python fwa_app.py
   ```

   Once the application is running, open a web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the application.

### Using the Application

1. **Upload Data**

   Use the web interface to upload data or interact with the application as per the designed functionalities.

2. **View Results**

   The application will display results based on the model's predictions and any additional information.

## Additional Notes

- **Model Files**

  - `xgb_best_model.pkl`: Serialized XGBoost model used for predictions.
  - `encoder.pkl`: Serialized encoder for data preprocessing.
  - `scaler.pkl`: Serialized scaler for data normalization.

- **Frontend Interface**

  - The `templates/index.html` file provides the frontend interface for the Flask application. Ensure this file is properly configured for user interactions.

- **Data Files**

  - Make sure any required data files are properly formatted and placed in the appropriate directories for the application to access.

## Files and Directories

### `/Flask_app_files/`

- **`fwa_app.py`**: Main script for the Flask application.
- **`requirements.txt`**: File listing required Python packages.
- **`encoder.pkl`**: Serialized encoder for data preprocessing.
- **`scaler.pkl`**: Serialized scaler for data normalization.
- **`xgb_best_model.pkl`**: Serialized XGBoost model used for predictions.
- **`templates/`**: Directory containing HTML templates.
  - **`index.html`**: Frontend interface for the Flask application.

This application aims to provide insights into healthcare fraud detection by utilizing a predictive model. If you encounter any issues or have questions, please refer to the documentation or contact the project contributors.
