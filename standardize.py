import pandas as pd

data = pd.read_csv('properties.csv')

# Standardize all numerical columns in our dataset
for col in data:
    if "unit" not in col and "name" not in col:
        data[col] = (data[col]-data[col].mean())/data[col].std()



data.to_csv("standardize.csv", index=False)
