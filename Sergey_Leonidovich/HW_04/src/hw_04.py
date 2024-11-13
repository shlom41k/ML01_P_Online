import os
import pandas as pd


"""
ЗАДАНИЕ. 
Имеется файл .csv со следующими полями: 'UserId', 'movieId', 'rating', 'timestamp'.
Необходимо найти:
1. Общее число оценок в файле
2. Общее количество пользователей, поставивших оценки
3. Общее количество оцененных фильмов
4. ID самого активного пользователя
5. Фильм, собравший наибольшее количество оценок
"""


# Путь к файлу с данными
file_path = "../data/ratings_small.csv"
file_path = file_path if os.path.isfile(file_path) else "../data/ratings_small.txt"


if __name__ == "__main__":

    # 1) Загружаем данные из файла и отбрасываем строки с пропущенными значениями
    df = pd.read_csv(file_path)
    print(f"Файл '{file_path}' успешно импортирован.")
    df.dropna()

    # 2) Общее число оценок в файле
    print(f"Общее число оценок в файле: {len(df[df['rating'] > 0])}.")

    # 3) Общее число пользователей, поставивших оценки
    print(f"Общее число пользователей, поставивших оценки: {len(df['userId'].value_counts())}.")

    # 4) Общее количество оцененных фильмов
    print(f"Общее количество оцененных фильмов: {len(df['movieId'].value_counts())}.")

    # 5) ID самого активного пользователя:
    print(f"ID самого активного пользователя: UserId={df['userId'].value_counts().idxmax()} ({df['userId'].value_counts().max()} оценка/и/ок).")

    # 6) Фильм, собравший наибольшее количество оценок:
    print(f"Фильм, собравший наибольшее количество оценок: movieId={df['movieId'].value_counts().idxmax()} ({df['movieId'].value_counts().max()} оценка/и/ок)).")



