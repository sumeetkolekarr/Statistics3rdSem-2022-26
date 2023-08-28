import pandas as pd

df = pd.read_csv(r'C:\Users\ARYAN VATS\Desktop\University\Semester 3\Stats\GithubStats\Aryan AIML-10\imdb-spider-man-reviews.csv')

sp1 = df[df['Movie'] == 'Spider-Man']
sp1R = sp1['Rating']

sp2 = df[df['Movie'] == 'Spider-Man: Homecoming']
sp2R = sp2['Rating']

sp3 = df[df['Movie'] == 'Spider-Man: No Way Home']
sp3R = sp3['Rating']

import matplotlib.pyplot as plt

plotter = lambda n,l : plt.plot(list(range(2000,4500)),[n]*2500, label=l)

# plt.plot(sp1R)
# plt.plot(sp2R)
plotter(sp1R.mean(), "Spider-Man")
#plotter(sp1R.median())
plotter(sp2R.mean(),'Homecoming')
plotter(sp3R.mean(), 'No way home')

plt.xlabel('Columns')
plt.ylabel('Spiderman')
# Add a legend
plt.legend()

plt.show()

