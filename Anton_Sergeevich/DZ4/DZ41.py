"""  1.	Общее число оценок в файле
2.	Общее количество пользователей, поставивших оценки
3.	Общее количество оцененных фильмов
4.	ID самого активного пользователя
5.	Фильм, собравший наибольшее количество оценок
"""



import numpy as np
import pandas as pd

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

df = pd.read_csv('ratings_small.csv')
print(df)

print('Full marks count',  df.rating.count())

print('Different count',  (df.drop_duplicates(['userId']))["userId"].count())
 
print('Movies count',  (df.drop_duplicates(['movieId']))["movieId"].count())

print('Activity of users',  (df.groupby(["userId"]).count()))