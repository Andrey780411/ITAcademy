"""Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
"""

list_numbers1 = [int(num) for num in input('Введите первый список чисел через пробел ').split()]
list_numbers2 = [int(num) for num in input('Введите второй список чисел через пробел ').split()]

print("Pазличных чисел в первом списке: ", len(set(list_numbers1)))
print("Pазличных чисел во втором списке: ", len(set(list_numbers2)))