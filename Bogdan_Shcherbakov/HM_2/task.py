import spacy
import en_core_web_sm
import re

nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_sm.load()
doc = nlp("This is a sentence.")

def txt_reader():
    txt = open('test.txt', encoding='utf-8')
    return txt.read().lower().rstrip()

def num_of_unic_worlds():
    unic_worlds = set(get_clean_txt(txt_reader()).split())
    return len(unic_worlds)

def num_of_vowels():
    vowels = "aeiouy"
    num_of_vowel = sum(txt_reader().lower().count(vowel) for vowel in vowels)
    return num_of_vowel

def num_of_consonants():
    consonants = "bcdfghjklmnpqrstvwxz"
    num_of_consonants = sum(txt_reader().lower().count(consonant) for consonant in consonants)
    return num_of_consonants

def num_of_sentences():
    end_of_sentence_marks = ".!?"
    num_of_sentences = sum(txt_reader().lower().count(mark) for mark in end_of_sentence_marks)
    return num_of_sentences
    
def get_clean_txt(txt: str) -> str:
    #word = re.sub(r'"[^a-z\' \-\n]"gm', ' ', word)
    clean_txt = "".join(re.findall(r"[a-z' \-]", txt))
    return clean_txt
    
    
def num_of_sentences_spacy():
    s = list(spacy_tokenization().sents)
    return len(s)

def medium_len_of_sents():
    list_of_sents = spacy_tokenization().sents
    counter = 0
    for sents in list_of_sents:
        counter += len(list(str(sents).split()))
    medium_len = counter / len(list(spacy_tokenization().sents))
    return medium_len

def spacy_tokenization():
    tokens = nlp(txt_reader())
    return tokens

def spacy_tokenization_with_clean_txt():
    tokens = nlp(get_clean_txt(txt_reader()))
    return tokens

def top_wolds():
    tokens = spacy_tokenization_with_clean_txt()
    list_of_lemma = []
    for token in tokens:
        list_of_lemma.append(token.lemma_)
    lemas_dict = {}
    for lemma in list_of_lemma:
        if lemma in lemas_dict:
            lemas_dict[lemma] += 1
        else:
            lemas_dict[lemma] = 1
    worlds_top = dict(sorted(lemas_dict.items(), key=lambda x: x[1], reverse=True)[:10])
    return worlds_top

print(f"Колличество гласных: {num_of_vowels()}")
print(f"Колличество согласных: {num_of_consonants()}")
print(f"Колличество уникальных слов: {num_of_unic_worlds()}")
print(f"Колличество предложений : {num_of_sentences()}")

print(f"Колличество предложений от spacy : {num_of_sentences_spacy()}")

print(f"Средняя длинна предложения {medium_len_of_sents()}")

print(f"Топ 10 часто используемых слов: {list(top_wolds())}")