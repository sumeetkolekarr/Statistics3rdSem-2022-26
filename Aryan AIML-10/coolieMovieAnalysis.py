import pandas as pd

movieNew = pd.read_csv(r'C:\Users\ARYAN VATS\Desktop\University\Semester 3\Stats\GithubStats\Aryan AIML-10\coolieNew.csv')

movieOld = pd.read_csv(r'C:\Users\ARYAN VATS\Desktop\University\Semester 3\Stats\GithubStats\Aryan AIML-10\coolieOld.csv')


import matplotlib.pyplot as plt


# New
plt.plot(movieNew['rating'])
plt.plot([movieNew['rating'].median()]*4)
plt.plot([movieNew['rating'].mean()]*4)

#old
plt.plot(movieOld['rating'])
plt.plot([movieOld['rating'].median()]*4)
plt.plot([movieOld['rating'].mean()]*4)

# plt.plot(movieNew['rating'].mode())

plt.show()