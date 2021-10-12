# import pandas
import pandas as pd

# Read the data using csv
data=pd.read_csv('EmployeeDataframe.csv')
# See initial 5 records
data.head()
print(data.head())
# See last 5 records
data.tail()
print(data.tail())
# Print the shape of a DataFrame
print(data.shape)