import pandas as pd
import matplotlib.pyplot as plt

# Read data from the first CSV file
df_kantara = pd.read_csv('kantara.csv')
kr = df_kantara['rating']

# Read data from the second CSV file
df_jumanji = pd.read_csv('jumanji.csv')
jr = df_jumanji['rating']

# Calculate mean and median for both datasets
kr_mean = kr.mean()
kr_median = kr.median()

jr_mean = jr.mean()
jr_median = jr.median()

# Create a bar chart
labels = ['Kantara (Mean)', 'Jumanji (Mean)', 'Kantara (Median)','Jumanji (Median)']
values = [kr_mean,  jr_mean,kr_median, jr_median]

plt.bar(labels, values)
plt.ylabel('Rating')
plt.title('Mean and Median Ratings Comparison')
plt.show()
