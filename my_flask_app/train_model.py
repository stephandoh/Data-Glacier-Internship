# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Create a simple dataset
data = {
    'income': [50000, 60000, 70000, 80000, 90000],
    'house_age': [5, 10, 15, 20, 25],
    'no_of_rooms': [3, 4, 3, 5, 4],
    'number_of_bedrooms': [2, 3, 2, 4, 3],
    'area_population': [30000, 40000, 35000, 45000, 50000],
    'house_price': [200000, 250000, 230000, 280000, 300000]
}

df = pd.DataFrame(data)

# Define features and target variable
X = df[['income', 'house_age', 'no_of_rooms', 'number_of_bedrooms', 'area_population']]
y = df['house_price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
