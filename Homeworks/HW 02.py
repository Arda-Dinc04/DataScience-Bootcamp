import random

import pandas as pd
import numpy as np

# 1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_cars = df.iloc[::20][['Manufacturer', 'Model', 'Type']]
print(filtered_cars)

# 2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
print(df.columns)
df['Min.Price'] = df['Min.Price'].fillna(df['Min.Price'].mean())
df['Max.Price'] = df['Max.Price'].fillna(df['Max.Price'].mean())
print(df['Min.Price'])

# 3) How to get the rows of a dataframe with row sum > 100?
dfNums = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows = dfNums[dfNums.sum(axis=1) > 100]
print(rows)

# 4)Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape this array into two separate 2D arrays,
# where one represents the rows and the other represents the columns. Write a function, preferably using a lambda function,
# to calculate the sum of each row and each column separately, and return the results as two separate NumPy arrays
array = np.random.randint(1, 101, (4,4))
rows_array = array.reshape(2, 8)
columns_array = array.T.reshape(2, 8)

sum_row = lambda arr: np.sum(arr, axis=1)
sum_column = lambda arr: np.sum(arr, axis=1)

sum_of_rows = sum_row(rows_array)
sum_of_columns = sum_column(columns_array)

print("Original Array:")
print(array)
print("\nSum of each row:")
print(sum_of_rows)
print("\nSum of each column:")
print(sum_of_columns)
