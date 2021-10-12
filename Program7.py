# import pandas
import pandas as pd

# Read the data using csv
data=pd.read_csv('EmployeeDataframe.csv')
# Filter columns
data.filter(['name', 'department','grade'])
print(data.filter(['name', 'department','grade']))