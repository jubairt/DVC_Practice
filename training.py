import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('Linear_Regression_Data.csv')

# Input feature (X) and target (y)
X = data[['YearsExperience']]
y = data['Salary']
y = y/10

# Train model
model = LinearRegression()
model.fit(X, y)

# Save Model
import joblib
joblib.dump(model, 'model.pkl')