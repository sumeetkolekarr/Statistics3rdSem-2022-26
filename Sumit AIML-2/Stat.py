import pandas as pd
df = pd.read_csv("imdb-spider-man-reviews.csv")

# Separating Ratings According to the movie 
Anim = df.loc[df['Movie'] == 'Spider-Man: Into the Spider-Verse']
Real = df.loc[df['Movie'] == 'Spider-Man']

# Adding Files to the given Sheets
Anim.to_csv("SpiderVerse.csv")
Real.to_csv("SpiderMan.csv")