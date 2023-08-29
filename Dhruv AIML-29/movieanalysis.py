#The following dataset is of MURDER ON THE ORIENT EXPRESS (1974) which contains 66K ratings 
import pandas as pd
data = {
    'Rating': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'No. of Votes': [381, 250, 420, 1100, 3100, 8900, 22000, 18000, 6400, 5500]
}

df = pd.DataFrame(data)

#MEAN
ws = (df['Rating'] * df['No. of Votes']).sum()
tv = df['No. of Votes'].sum()
mean = ws / tv
mean = min(max(mean, 1), 10)
print("Weighted Mean Rating (1-10):", mean)

#MEDIAN
tv = df['No. of Votes'].sum()

rs = []
for r, v in zip(df['Rating'], df['No. of Votes']):
    rs.extend([r] * v)

rs.sort()

mi = tv // 2
if tv % 2 == 0:
    median = (rs[mi - 1] + rs[mi]) / 2
else:
    median = rs[mi]
median = min(max(median, 1), 10)
print("Median Rating (1-10):", median)

#MODE
mode = 3*median - 2*mean
print("Mode Rating (1-10) : ",mode)