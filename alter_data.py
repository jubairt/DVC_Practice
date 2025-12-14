import pandas as pd

# Read CSV file
data = pd.read_csv("Linear_Regression_Data.csv")

# Modify YearsExperience column
data["YearsExperience"] = 2 * data["YearsExperience"]

# Save back to CSV
data.to_csv("Linear_Regression_Data.csv", index=False)
