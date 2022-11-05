"""Бинарные операции:
Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
Задачу поместите в файл task6.py в папке src/homework5."""

number = int(input("Введите целое число: "))
degree_divider = number.bit_length()-1

while degree_divider>=0:
    if number%2**degree_divider == 0:
        print(f"Максимальный делитель, являющийся степенью двойки, вашего числа: {2**degree_divider} это 2 в {degree_divider} степени")
        break
    else:
        degree_divider = degree_divider-1
