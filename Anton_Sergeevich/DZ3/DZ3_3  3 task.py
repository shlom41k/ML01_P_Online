"""Составить программу, которая считает число гласных и согласных букв. 


Анализ: создадим две строки, одну с гласными, вторую с согласными

Будем каждую букву проверять на принадлежность к одной и ко второй.
Так мы исключим знаки препинания и другие символы.

Также посчитаем общее количество символов.
"""

f = open('text5.txt', 'r',encoding='utf-8')
# text2.txt -full book, text4.txt 15lines, text5.txt 1 line, text6.txt 2 line
vowels = "EeYyUuIiOoAa"
consonant = "QqWwRrTtPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
vowels_count=0
consonant_count=0
full_count = 0
for line in f:
    for character in line:
        full_count+=1
        if character in vowels:
                vowels_count+=1                
        elif character in consonant:
                consonant_count+=1                
        
                
print("количество гласных", vowels_count)
print("количество согласных",consonant_count)
print("общее количество букв",full_count)