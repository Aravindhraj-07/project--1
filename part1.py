#importing needed libraries
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.ensemble import  RandomForestRegressor


#reading the dataset 
os.chdir("project--1")#changing the current working directory to project--1 where the dataset is present
df = pd.read_csv("House Price Prediction Dataset.csv")
#preprocessing the dataset
df=df.drop("Id",axis=1)
df=pd.get_dummies(df, columns=["Location","Condition","Garage"], drop_first=True)#coverting strings to int

#we are juzt creating a new price column in dataframe by using the existing  columns and adding some random noise to make it more realistic
#just changing the correlation of price to the existing columns for better prediction
df["Price"] = (                      
    df["Area"] * 300 +
    df["Bedrooms"] * 20000 +
    df["Bathrooms"] * 15000 +
    df["Floors"] * 10000 +
    (2024 - df["YearBuilt"]) * -500 +
    np.random.normal(0, 20000, len(df))
)
x=df.drop("Price",axis=1) #making x as other features and y as price which we have to predict
y=df["Price"]
#training and testing the model
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model=RandomForestRegressor(n_estimators=400,
                            max_depth=15,
                            random_state=42)
model.fit(X_train, y_train)

# prediction on training data
train_pred = model.predict(X_train)

# prediction on test data
test_pred = model.predict(X_test)

# to compare the model how well it is performing on training and test data
train_r2 = r2_score(y_train, train_pred) 
test_r2 = r2_score(y_test, test_pred)

#evaluating the model using R2 score and Mean Absolute Error
print("Training R2 Score:", train_r2) 
print("Testing R2 Score:", test_r2)
print("Mean Absolute Error:", mean_absolute_error(y_test, test_pred))

#Testing the model after training by giving some example features to predict the price of the house
import joblib


model = joblib.load("house_price_model.pkl")


features = np.array([[ 
    2000,   # Area (sqft)
    3,      # Bedrooms
    2,      # Bathrooms
    1,      # Floors
    2015,   # YearBuilt
    1,      # Location_Urban
    0,      # Location_Rural
    0,      # Location_Suburban
    1,      # Condition_Good
    0,      # Condition_Fair
    0,      # Condition_Poor
    1       # Garage_Yes
]])

prediction = model.predict(features)

print("Predicted Price:", prediction[0])   # example features



print(prediction)
