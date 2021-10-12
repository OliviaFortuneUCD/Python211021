# import pandas
import pandas as pd

# Read the data using csv
data = pd.read_csv('EmployeeDataframe.csv')

# Select rows for the specific index
data.filter([0, 1, 2], axis=0)
print(data.filter([0, 1, 2], axis=0))
# Filter employee who has more than 500 and less than 700 performance score
data[(data.performance_score >=500) & (data.performance_score < 700)]