"""7. Дана строка
Сначала выведите третий символ этой строки. 
Во второй строке выведите предпоследний символ этой строки. 
В третьей строке выведите первые пять символов этой строки. 
В четвертой строке выведите всю строку, кроме последних двух символов. 
В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, 
поэтому символы выводятся начиная с первого). 
В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки. 
В седьмой строке выведите все символы в обратном порядке. 
В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего. 
В девятой строке выведите длину данной строки."""


my_string = input("Введите строку: ")

print ("Третий символ строки: ", my_string[2])
print ("Последний символ строки: ", my_string[-1])
print ("Первые пять символов строки: ", my_string[:5])
print ("Строка за исключением последних двух символов: ", my_string[:-2])
print ("Символы строки с четными индексами: ", my_string[0::2])
print ("Символы строки с нечетными индексами: ", my_string[1::2])
print ("Зеркальное отображение строки: ", my_string[::-1])
print ("Символы строки через один в обратном порядке: ", my_string[-1::-2])
print ("Длина строки: ", len(my_string))
