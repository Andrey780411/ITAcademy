"""Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20, 
а значениями кубы этих чисел.
"""

my_dictionary = {key: key**3 for key in range(1,21)}
print(my_dictionary)