from settings import alphabet, sent_punct
from string import punctuation
from stop_words import get_stop_words
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
"""


def read_data(filename: str) -> str:
    """
    Функция чтения данных из файла
    :param filename: имя файла (str)
    :return: содержимое файла (str)
    """

    # Считываем данные из файла
    with open(filename, 'r') as file:
        data = file.read()
    return data

def remove_punctuation(text: str) -> str:
    """
    Функция удаления знаков препинания из текста
    :param text: Исходный текст (str)
    :return: Текст без знаков препинания (str)
    """

    # Удаляем знаки препинания (через таблицу замен)
    return text.translate(str.maketrans('', '', punctuation))

def str_2_words(text: str, unique=True, words_only=True, ignore_stopwords=True) -> set or list:
    """
    Функция преобразования текста в список/множество
    :param text: Исходный текст (str)
    :param words_only: Флаг учета/не учета чисел как слов (boolean):
                        when True - числа не считаются за слова.
    :param unique: Флаг 'уникальности' возвращаемых данных (boolean):
                        when True - функция возвращает данные в виде множества.
    :param ignore_stopwords: Флаг учета/не учета стоп-слов (boolean):
                        when True - стоп-слова не учитываются.
    :return: Множество/список слов исходного текста
    """

    # Получаем все слова исходного текста
    stopwords = get_stop_words("en") if ignore_stopwords else list()
    #print(stopwords)
    words = [word.lower() for word in text.split() if (word.isalpha() and word.lower() not in stopwords)] if words_only == True \
            else [word.lower() for word in text.split() if word.lower() not in stopwords]

    return set(words) if unique == True else words

def get_vow_cons(text: str, alph="EN") -> tuple[int, int]:
    """
    Функция подсчета гласных и согласных букв в тексте
    :param text: Исходный текст (str)
    :param alph: Язык исходного текста (str)
    :return: Количество гласных и согласных букв в тексте (int, int)
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
    :param text: Исходный текст (str)
    :return: Словарь, где key - предложение, value - его длина (dict)
    """

    # Разбиваем на предложения
    sentences = re.split(sent_punct, text)

    # Убираем лишние символы и пустые строки
    sentences = [s.strip() for s in sentences if s]
    #print(sentences)

    return {sentence:len(sentence) for sentence in sentences}


def words_cnt(words: list, crit_lev_val: int) -> dict:
    """
    Функция подсчета частоты встречаемости слов с учетом критерия схожести.
    В качестве критерия используется расстояние Левенштейна
    :param words: Список слов исходного текста (list)
    :param crit_lev_val: Пороговый уровень расстояния Левенштейна (int)
    :return: Словарь, где key - слово, value - количество употреблений данных слов в тексте (dict)
    """
    d = dict()

    for ind1, word1 in enumerate(words):
        if word1 not in d.keys():
            for ind2, word2 in enumerate(words):
                # Находим расстояние Левенштейна
                ratio = fuzz.ratio(word1, word2)

                if ratio >= crit_lev_val:
                    # d[word1] = d.get(word1) + 1 if word1 in d else d[word1] = -1
                    if word1 in d.keys():
                        d[word1] = d.get(word1) + 1
                    else:
                        d[word1] = 1
    return d


def most_rep_words(words: dict, num=10) -> list[tuple[str, int]]:
    """
    Функция сортировки словаря 'words' по значению. Возвращает 'num' сортированных пар 'key: value'
    :param words: исходный словарь, где key - слово, value - количество его повторений в тексте
    :param num: число пар key: value словаря, которое необходимо вернуть
    :return: кортеж из N сортированных (по убыванию) пар key: value исходного словаря
    """

    return sorted(words.items(), key=lambda item: item[1], reverse=True)[:num]


def main():
    # 1) Считываем данные в файл
    f = "../data/test_data_01.txt"
    test_data = read_data(f)
    print(f"1. Данные файла '{f}' успешно импортированы. Полученный текст:\n")
    print(test_data)

    # 2) Подготавливаем данные: удаляем знаки препинания из текста
    test_data_1 = remove_punctuation(test_data)
    print(test_data_1)

    # 3) Преобразуем текст во множество слов и находим его длину (кол-во 'уникальных' слов без учета стоп-слов)
    uniq_words = str_2_words(test_data_1, ignore_stopwords=True)
    # Выводим количество уникальных слов в тексте
    print(f"2. Количество уникальных слов в тексте: {len(uniq_words)}.")
    print(uniq_words)

    # 4) Подсчитываем число гласных и согласных букв
    gl, sogl = get_vow_cons(test_data_1, alph="EN")
    print(f"3. Количество гласных букв: {gl}; согласных букв: {sogl}.")

    # 5) Разбиваем текст из фала на предложения и выводим статистику по каждому из них
    sentences = get_sent(test_data)
    print(f"4. Общее число предложений в тексте: {len(sentences)}.")
    print(f"\tНиже приводится информация о длине каждого предложения:")
    for ind, sent in enumerate(sentences):
        print(f"\tSentence #{ind + 1}: length: {sentences.get(sent)}; data: {sent}.")

    # 6) Считаем число повторений каждого слова в тексте (с учетом критерием схожести)
    words_stat = words_cnt(str_2_words(test_data_1, unique=False, ignore_stopwords=True), crit_lev_val=80)
    print(f"5. Ниже приводится информация о частоте использования каждого слова в тексте:")
    for word, cnt in words_stat.items():
        print(f"\tWord: '{word}': number of entries: {cnt}.")

    # 7) Выводим N наиболее часто встречаемых слов в тексте
    N = 10
    sorted_words = most_rep_words(words_stat, num=N)
    print(f"6. {N} наиболее часто встречаемых слов в тексте:")
    for word, cnt in sorted_words:
        print(f"\tWord: '{word}': number of entries: {cnt}.")


if __name__ == '__main__':
    main()
