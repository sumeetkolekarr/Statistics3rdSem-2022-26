import pandas as pd
df = pd.read_csv("imdb-spider-man-reviews.csv")

Anim = df.loc[df['Movie'] == 'The Amazing Spider-Man']
Real = df.loc[df['Movie'] == 'Spider-Man: Homecoming']

Anim.to_csv("SpiderMan_Amazing.csv")
Real.to_csv("SpiderMan_Homecoming.csv")