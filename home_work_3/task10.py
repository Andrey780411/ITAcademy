"""Во входной строке записан текст. Словом считается последовательность непробельных символов, 
идущих подряд, слова разделены одним или несколькими пробелами, либо символами конца строки. 
Определите сколько различных слов содержится в этом тексте."""


import re
my_string = input("Введите текст: ")                 # Вводим текст со знаками препинания и пробелами
new_string = re.sub(r'[^\w\s]',' ', my_string)       # Удаляем все знаки препинания в тексте
words = new_string.split()                           # Делаем список слов введенного текста, разделенных пробелами
print(len(words))                                    # Количество слов в тексте - будет длина списка 