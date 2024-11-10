"""  Составить программу, которая считает число уникальных слов в тексте
(без критерия схожести)
Вывести 10 наиболее часто встречаемых слов. 

Анализ:
Будем считывать файл по строкам,  делить строки на слова.
Для подсчета уникальных слов будем использовать словарь в формате слово- количество.
Будем вести подсчет полного количества слов.

Для вывода 10 наиболее часто встречаемых создадим словарь ordered_dict и выведем
10 первых записей.
"""

f = open('text2.txt', 'r',encoding='utf-8')
# text2.txt -full book, text4.txt 15lines, text5.txt 1 line, text6.txt 2 line
dict = {}

uniqe_words = 0
full_words = 0

for line in f:        
        i =0
        for word in line.split():
            full_words+=1
            if word not in dict:
                dict[word] =1
                uniqe_words+=1
                
            elif word in dict:
                dict[word] +=1                       
                                 
                
#print(dict)    
#print("lenth of dic of uniqe words  ",len(dict))  
print("\n uniqe words = ", uniqe_words)
print("\n full words = ", full_words)
print("\n Most used 10 words: ")
dict_sorted =(sorted(dict.items(), key=lambda item: item[1]))
print(dict_sorted[-9:])


                
            


    