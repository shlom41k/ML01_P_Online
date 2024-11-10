"""
 Предоставляет готовые функции для вычисления различных метрик сходства строк, включая расстояние Левенштейна.
"""

from fuzzywuzzy import fuzz

word1 = "belarus"
word2 = "belarusian"
ratio = fuzz.ratio(word1, word2)
print(f"Ratio of similarity: {ratio}")

