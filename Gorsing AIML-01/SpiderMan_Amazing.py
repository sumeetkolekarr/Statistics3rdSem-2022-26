import pandas as pd
df = pd.read_csv("SpiderMan_Amazing.csv")

Stat = [df['Rating']]

d = pd.DataFrame(Stat)
print(df.describe())
print("Median is",df['Rating'].quantile(0.5))
a = (df['Rating'].quantile(0.25))
b = (df['Rating'].quantile(0.75))
c = b - a
print("The IQR is", c)
