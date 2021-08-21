import pandas as pd
import numpy as np

df = pd.read_csv('movies_dataset.txt', encoding= 'unicode_escape')

start_year = 1950
end_year = 1960
mask = (df['year'] > start_year) & (df['year'] <= end_year)
df1 = df.loc[mask]
df_count_year = df1.count()
print("Number of movies released between the year 1950 and 1960 are:", df_count_year['year'])

rating = 4.0
mask1 = (df['rating'] > rating)
df2 = df.loc[mask1]
df_count_rating = df2.count()
print("Number of movies whose ratings are more than 4 are:", df_count_rating['rating'])


start_rating = 3
end_rating = 4
mask2 = (df['rating'] > start_rating) & (df['rating']<end_rating)
df3 = df.loc[mask2]
print("Movie names whose ratings are between 3 and 4 are:\n", df3['Movie_name'].head())

total_duration = 7200
mask2 = (df['duration'] > total_duration)
df4 = df.loc[mask2]
df_count_duration = df4.count()
print("Number of movies with duration more than 2 hours are:",df_count_duration['duration'])

# df5 = df.loc()
# df5 = df['year'].sort()
# print(df5['Movie_name']['year'].head())

# df['Movie_name'] = df['Movie_name'].astype(float)
# df_total_count = df['Movie_name'].count()
# print("Total number of movies in a dataset:", df_total_count.head())

num = len(df)
print("The number of movies in the dataset is {}".format(num))