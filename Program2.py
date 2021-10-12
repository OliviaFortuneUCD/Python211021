# import pandas
import pandas as pd

# Read CSV file
sample_df=pd.read_csv('Gold.csv', sep=',' , header=None)

# display initial 5 records
sample_df.head()
print(sample_df.head()) 