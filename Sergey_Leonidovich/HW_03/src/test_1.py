from charset_normalizer.cd import encoding_unicode_range
from spacy.lang.am.examples import sentences

from settings import alphabet, sent_punct
from string import punctuation
from fuzzywuzzy import fuzz
import re


"""
1.	Загрузить файл длиной не менее 2000 символов.
2.	Составить программу, которая считает число уникальных слов в тексте (без критерия схожести)
3.	Составить программу, которая считает число гласных и согласных букв.
4.	Составить программу, которая считает число предложений, их длину и число (количество) раз использования
    каждого слова в тексте (с критерием схожести, критерий схожести слов выбрать самостоятельно,
    например, spacy (en_core_web_sm) или расстояние Левенштейна).
5.	Вывести 10 наиболее часто встречаемых слов.

p.s. Рекомендую перед решением задания проанализировать задачу и обосновать алгоритм ее решения в текстовом виде.
В процессе написания кода использовать комментарии.
"""


def read_data(filename: str) -> str:
    """
    Функция чтения данных из файла
    :param filename: имя файла (строка)
    :return: содержимое файла (строка)
    """

    with open(filename, 'r') as file:
        data = file.read()
    return data

def remove_punctuation(text: str) -> str:
    """
    Функция удаления знаков препинания из текста
    :param text: Исходный текст
    :return: Текст без знаков препинания
    """

    # Удаляем знаки препинания (через таблицу замен)
    return text.translate(str.maketrans('', '', punctuation))

def str_2_words(text: str, unique=True, words_only=True) -> set or list:
    """
    Функция преобразования текста во множество уникальных слов
    :param text: Исходный текст (строка)
    :param words_only: Флаг учета/не учета чисел: (True - числа не учитываются)
    :param unique: Флаг 'уникальности' возвращаемых данных (True - возвращаем только уникальные слова)
    :return: Выходное множество уникальных слов или список всех слов
    """

    # Получаем все слова исходного текста
    words = [word.lower() for word in text.split() if word.isalpha()] if words_only == True \
            else [word.lower() for word in text.split()]

    return set(words) if unique == True else words

def get_vow_cons(text: str, alph="EN") -> tuple[int, int]:
    """
    Функция подсчета гласных и согласных букв в тексте
    :param text: Исходный текст
    :param alph: Язык
    :return: Количество гласных и согласных букв в тексте
    """

    vowels, consonants = 0, 0
    for letter in text:
        if letter.lower() in alphabet.get(alph).get("vowels"):
            vowels += 1
        elif letter.lower() in alphabet.get(alph).get("consonants"):
            consonants +=1
            #print(letter)

    return vowels, consonants

def get_sent(text: str) -> dict:
    """
    Функция подсчета числа предложений в тексте
    :param text: Исходный текст
    :return: Словать, где key - предложение, value - его длина
    """

    # Разбиваем на предложения
    sentences = re.split(r'[.!?]', text)

    # Убираем лишние символы и пустые строки
    sentences = [s.strip() for s in sentences if s]
    #print(sentences)

    return {sentence:len(sentence) for sentence in sentences}


def words_cnt(words: list, crit_lev_val: int) -> dict:
    d = dict()
    print(words)

    for ind1, word1 in enumerate(words):
        if word1 not in d.keys():
            for ind2, word2 in enumerate(words):
                #if ind2 >= ind1:
                # Находим расстояние Левенштейна
                ratio = fuzz.ratio(word1, word2)

                if ratio >= crit_lev_val:
                    # d[word1] = d.get(word1) + 1 if word1 in d else d[word1] = -1
                    if word1 in d.keys():
                        d[word1] = d.get(word1) + 1
                    else:
                        d[word1] = 1

    return d



if __name__ == '__main__':

    # 1) Считываем данные в файл
    f = "../data/test_data_02.txt"
    test_data = read_data(f)
    #print(test_data)
    print(f"1. Данные файла '{f}' успешно импортированы.")

    # 2) Подготовливаем данные: удаляем знаки препинания
    test_data_1 = remove_punctuation(test_data)
    #print(test_data_1)

    # 3) Преобразуем строку во множество и находим его длину (кол-во уникальных слов)
    uniq_words = str_2_words(test_data_1)
    # Выводим количество уникальных слов в тексте
    print(f"2. Количество уникальных слов в тексте: {len(uniq_words)}.")

    # 4) Подсчитываем число гласных и согласных букв
    gl, sogl = get_vow_cons(test_data_1, alph="EN")
    print(f"3. Количество гласных букв: {gl}; согласных букв: {sogl}.")

    # 5) Разбиваем текст из фала на предложения
    sentences = get_sent(test_data)
    print(f"4. Общее число предложений в тексте: {len(sentences)}.")
    print(f"\tНиже приводится информация о длине каждого предложения:")
    for ind, sent in enumerate(sentences):
        print(f"\tSentence #{ind+1}: length: {sentences.get(sent)}; data: {sent}.")

    # 6) Считаем число повторений каждого слова в тексте (с критерием схожести)
    words_stat = words_cnt(str_2_words(test_data_1, unique=False), crit_lev_val=100)
    print(f"5. Ниже приводится информация о частоте использования каждого слова в тексте:")
    for word, cnt in words_stat.items():
        print(f"\tWord: '{word}': number of entries: {cnt}.")




