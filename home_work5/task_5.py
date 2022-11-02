"""Бинарные операции:
Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
Задачу поместите в файл task5.py в папке src/homework5."""

number = int(input("Введите целое число: "))
def number_around():
    previous_number = 2 ** (number.bit_length() - 1)
    next_number = 2 ** (number.bit_length())
    if number - previous_number == next_number - number:
        print("Ваше число равноудалено от чисел степени двойки: ", previous_number, "и", next_number)
    elif number - previous_number < next_number - number:
        print("Ближайшая степень двойки к вашему числу: ", previous_number)
    else:
        print("Ближайшая степень двойки к вашему числу: ", next_number)
      
number_around()