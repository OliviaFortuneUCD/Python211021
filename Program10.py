# import pandas
import pandas as pd

# Read the data using csv
data = pd.read_csv('EmployeeDataframe.csv')
# Filter employee who has performance score of less than 500
data.query('age<20')
print(data.query('age<20'))