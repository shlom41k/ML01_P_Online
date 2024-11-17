import pandas as pd

films_stat = pd.read_csv('ratings_small.csv')

def num_of_rating():
    num_of_rating = len(films_stat.iloc[:,[2]])
    print(f"Общее число оценок {num_of_rating}")
    return num_of_rating

def userId_rated():
    num_of_users_rating = len(films_stat['userId'].unique())
    print(f"Общее число пользователей, поставивших оценки {num_of_users_rating}")
    return num_of_users_rating

def rated_films():
    num_of_rated_films = len(films_stat['movieId'].unique())
    print(f"Общее число оцененных фильмов {num_of_rated_films}")
    return num_of_rated_films

def most_active_userId():
    users_sorted_by_rating = films_stat.groupby('userId').count().sort_values('rating').tail(1)
    user_id = list(users_sorted_by_rating.index)
    num_of_rating = users_sorted_by_rating['rating'].values
    print(f"Пользователь {user_id} поставил большее количество оценок в количестве {num_of_rating}")
    return user_id, num_of_rating

def most_rated_film():
    films_sorted_by_rating = films_stat.groupby('movieId').count().sort_values('rating').tail(1)
    film_id = list(films_sorted_by_rating.index)
    num_of_rating = films_sorted_by_rating['rating'].values
    print(f"Самому оцененному фильму {film_id} поставили больше всего оценок в количестве {num_of_rating}")
    return film_id, num_of_rating

num_of_rating()
userId_rated()
rated_films()
most_active_userId()
most_rated_film()