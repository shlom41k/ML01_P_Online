from test_1 import read_data
import spacy


# Загружаем языковую модель
nlp = spacy.load("en_core_web_sm")

# Входной текст
text = read_data("../data/test_data_01.txt")
#print(text)

# Применяем токенизацию
doc = nlp(text)

# Выводим токены (слова и пунктуацию) из текста
for token in doc:
    if token.is_punct:
        continue
    print(token.text)

