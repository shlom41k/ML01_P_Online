import os
import re


def tokenizer(txt: str) -> list:
    assert txt != "", "Input text is empty"

    # cleaning txt
    txt = re.sub(r'[^а-яА-ЯёЁ]', " ", txt.lower())
    txt = re.sub(r'\s+', " ", txt)

    # split words
    words_list = re.split(" ", txt)

    return words_list


def load_fl(path: str) -> str:
    """
    Функция загрузки текста из файла. Файл должен быть в UTF-8 кодировке
    :param path: путь к файлу
    :return: текст
    """
    assert os.path.isfile(path), "File don't exist. Please, check path to file."

    with open(path, encoding="utf-8") as fl:
        txt = fl.read()

    return txt


if __name__ == "__main__":
    txt_raw = load_fl("book.txt")
    print(txt_raw)

    txt_tk = tokenizer(txt_raw)
    print(txt_tk)

"""
 планы
  - реализовать два режима токенизатора: разбиение по предложениям и по словам (последний есть)
  - реализовать функцию подсчета гласных и согластных букв (буду считать в отдельных словах)
"""

