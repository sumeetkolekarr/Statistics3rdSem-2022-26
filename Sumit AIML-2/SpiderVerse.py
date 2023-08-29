import pandas as pd
df = pd.read_csv("SpiderVerse.csv")

Stat = [df['Rating']]

# Gives Info about many Statistics 
print(df.describe())
print("The Median is",df['Rating'].quantile(0.5))
print("The Mean is",df['Rating'].mean())

a = (df['Rating'].quantile(0.25))
b = (df['Rating'].quantile(0.75))
c = b - a
print("The IQR is", c)