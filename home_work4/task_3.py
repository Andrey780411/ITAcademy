"""Даны два списка чисел. Посчитайте, сколько различных чисел содержится 
одновременно как в первом списке, так и во втором."""

list_numbers1 = [int(num) for num in input('Введите первый список чисел через пробел ').split()]
list_numbers2 = [int(num) for num in input('Введите второй список чисел через пробел ').split()]

print("Pазличных чисел в двух списках: ", len(set(list_numbers1 + list_numbers2)))