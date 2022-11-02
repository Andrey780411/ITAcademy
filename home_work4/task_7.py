"""Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель 
при помощи алгоритма Евклида (мы не знаем функции и рекурсию)."""

# ВАРИАНТ 1:
number1 = int(input("Введите первое целое число: "))
number2 = int(input("Введите второе целое число: "))
while number1 > 0 and number2 > 0:
    if number1 > number2:
        number1 = number1%number2
    else:
        number2 = number2%number1

print("Наибольший общий делитель равен: ", number1+number2 )

"""ВАРИАНТ 2
number1 = int(input("Введите первое целое число: "))
number2 = int(input("Введите второе целое число: "))
while number1 != number2:
    if number1 > number2:
        number1 = number1 - number2
    else:
        number2 = number2 - number1

print("Наибольший общий делитель равен: ", number1 )"""