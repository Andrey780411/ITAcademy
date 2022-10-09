"""Напишите программу на Python, чтобы получить одну строку из двух заданных строк, 
разделенных пробелом, и поменять местами первые два символа каждой строки

Sample String : 'abc', 'xyz'

Expected Result :
'xyc abz'"""

string1 = "abc"
string2 = "xyz"
part1_string1 = string1[0:2]
part2_string1 = string1[-1:]
part1_string2 = string2[0:2]
part2_string2 = string2[-1:]
print(part1_string2, part2_string1, " ", part1_string1, part2_string2, sep = "")


"""Напишите программу на Python для удаления n-го символа индекса из непустой строки."""

string = input("Введите строку: ")
num = int(input("Введите номер символа, который хотите удалить: ")) - 1
if len(string) < num:
    print("Такого символа нет в данной строке")
else:
    p1_string = string[:num] 
    p2_string = string[num+1:]
    print("Новая строка: ", p1_string + p2_string)