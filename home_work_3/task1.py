"""1. FizzBuzz 

Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz, 
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz."""

my_list = [int(i) for i in range(1, 101)]   # Создаем список чисел от 1 до 100
result_iist = []
for element in my_list:                     # Проходимся по списку от 1 до 100
    if element%3 == 0 and element%5 == 0:   # При целочисленном делении на 3 и на 5 добавляем в новый список элемент "FizzBuzz"
        result_iist.append("FizzBuzz")
    elif element%3 == 0:
        result_iist.append("Fizz")          # При целочисленном делении на 3 добавляем в новый список элемент "Fizz"
    elif element%5 == 0:
        result_iist.append("Buzz")          # При целочисленном делении на 5 добавляем в новый список элемент "Buzz"
    else: result_iist.append(element)       # При не выполнении вышеуказанных условий - добавляется исходный элемент

print(result_iist)