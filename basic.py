import pandas as pd

df = pd.read_csv('doc/data.csv')

# Here we are follow the steps to at last visualize the data

# 1: check data info or details
print('\n\nCheck Data using info mehtod:\n\n', df.info())
print('\n\nCheck Data using describe mehtod:\n\n', df.describe())

# Data cleaning: empty cells, data in wrong formate, wrong data or dublicate data

# check null vauelse using
print('\n\nCheck null values using isnull mehtod:\n\n', df.isnull())
print('\n\nCheck null values using isnull mehtod with sum():\n\n', df.isnull().sum())

# remove null values using dropna(): used inplace=True to set thid df as permanten
print('\n\nremove null using dropna():\n\n', df.dropna())
print('\n\nCheck null values using isnull mehtod with sum():\n\n', df.isnull().sum())

# use fillna() to replace the nan value with anyone
# noraml way to find the mean value of column in which found nan value and relace the nan with mean value.
mean_value = df['Calories'].mean()
print('\n\nReplace nan vaue with mean value:\n\n', df['Calories'].fillna(mean_value))

# Finding a relation between the colums using pandas this important method corr() which is helps to find the relateion.
print('\n\nFind relation using corr():\n\n', df.corr())