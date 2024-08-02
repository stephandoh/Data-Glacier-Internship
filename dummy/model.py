import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Read the dataset
csv_path = r'C:\Users\steph\Sondoh_Glacier\dummy\USA_Housing.csv'
USAHousing = pd.read_csv(csv_path)

# Step 2: Prepare the features and target variable
X = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAHousing['Price']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Step 4: Train the Linear Regression model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Step 5: Save the trained model using pickle
pickle.dump(lm, open('model.pickle', 'wb'))
