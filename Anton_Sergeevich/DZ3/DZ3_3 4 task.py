"""Составить программу, которая считает число предложений, их длину и число
(количество) раз использования каждого слова в тексте (с критерием схожести,
критерий схожести слов выбрать самостоятельно, например, spacy ( ) или расстояние
Левенштейна). 


Анализ.
Файл будем читать по строкам, далее делим на  слова. 
Если в конце слова стоит точка, считаем это за конец предложения, увеличиваем счетчик предложений

Приведить слова к простым формам будем библиотекой ntlk.stem
Упрощенные библиотекой nltk.stem слова добавляем в словарь.
"""


#import spacy 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
#nlp = spacy.load("en_core_web_sm") 

sentence_count = 0
distinct_words = 0
full_words = 0
dict = {}                  #словарь уникальных слов
dict_sentence_lenth = {}   #словарь количества предложений формата 1 - длина 7
sententh_lenth_current = 0
f = open('text2.txt', 'r',encoding='utf-8')
# text2.txt-full book, text4.txt 15lines, text5.txt 1 line, text6.txt 2 line
for line in f:
    line = line.replace('"', '')
    for word in line.split():
        if word[-1] in ",:;-/": #убираем спецсимволы в конце слова
            word = word[0:-1]
        sententh_lenth_current+=1 #увеличиваем счетчик предложения
         
        if word[-1] in  ".!?":  # Если точка, увеличиваем количество предложений, и убираем точку, чтобы далее работать чисто со словом
            sentence_count+=1
            word = word[0:-1]
            dict_sentence_lenth[sentence_count] =  sententh_lenth_current # пишем запись в словарь длин предложений
            sententh_lenth_current=0            
        
        stemmed_word = ps.stem(word) #приводим слово к простой форме      
        
        if stemmed_word not in dict:
            dict[stemmed_word] =1  #пишем запись в словарь
            distinct_words+=1
            full_words+=1
        elif stemmed_word in dict:
            dict[stemmed_word] +=1    #если слово уже есть, увеличиваем счетчик этого слова
            full_words+=1  
            
  
    
    
print("sentence count = ", sentence_count )
print(sorted(dict.items()))  

print(" ")
print("sentence lenth in format: Number sentence - quantity of words:  "),

print(dict_sentence_lenth)  