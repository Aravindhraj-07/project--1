HOUSE PRICE PREDICTION
---

## **🎯 Project Description**

This project is a **House Price Prediction Web Application** that estimates the price of a house based on several important features such as **area (sqft), bedrooms, bathrooms, floors, location, condition,** and **garage availability**.

The application allows users to easily enter house details through a simple web interface, and the trained **machine learning model** predicts the estimated house price instantly.

> **Note:** The predicted price is based only on the dataset used to train the model. It does not represent actual real-world market prices and should be considered only as a demonstration of a machine learning application.

---

## **✨ Features**

- **Enter house details** (area, bedrooms, bathrooms, etc.)
- **Predict house price instantly**
- **Interactive web interface**
- **Runs completely using a trained ML model**

---

## **� Installation and Usage**

### Prerequisites
- Python 3.7+
- Virtual environment (recommended)

### Installation
1. Clone or download the project.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install streamlit scikit-learn pandas numpy joblib
   ```

### Usage
1. Train the model (if needed):
   ```
   python part1.py
   ```
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open the provided local URL in your browser to use the app.

---

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**

---

## **🤖 Model Used**

- **Random Forest Regressor**
    - The model was trained to predict house prices using multiple input features.
    - The trained model was saved using **joblib** and loaded into the Streamlit app.

---

## **📁 Project Directory**

```
project--1/
│
├── app.py                          # Streamlit web application
├── part1.py                        # Training script for the model
├── part1.ipynb                     # Jupyter notebook for training
├── House Price Prediction Dataset.csv  # Dataset used for training
├── house_price_model.pkl           # Trained machine learning model
└── README.md                       # Project documentation
```
- [Dataset](<House Price Prediction Dataset.csv>)
- [Model](house_price_model.pkl)
- [House Price Predictor App](https://housepricepredicting-msd7777.streamlit.app/)

---

## **🚀 Future Improvements**

- **Add more realistic housing datasets**
- **Improve UI design**
- **Deploy using cloud services**
- **Add price visualization charts**

---

**Developed and Maintained by [Aravindhraj](https://www.linkedin.com/in/aravindh-raj-15b029387?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)**

---