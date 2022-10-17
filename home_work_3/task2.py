# 2. List Practice

# Используйте генератор списков, чтобы получить следующий: [‘ab’, ‘ac’, ‘ad’, ‘bb’, ‘bc’, ‘bd’];

my_list = [x + y for x in "ab" for y in "bcd" ]
print(my_list)

# Используйте предыдущий список slice, чтобы получить следующий: [‘ab’, ‘ad’, ‘bc’];

new_list = my_list[::2]
print(new_list)

# Используйте генератор списков, чтобы получить следующий: [‘1a’, ’2a’, ‘3a’, ‘4a’];

my_list3 = [str(x) + "a" for x in range(1, 5)]
print(my_list3)

# Одной строкой удалите элемент ‘2a’ из прошлого списка и напечатайте его;

my_list3.remove("2a")
print(my_list3)

# Скопируйте список и добавьте в него элемент ‘2a’ так, чтобы в исходном списке этого элемента не было.

import copy
res_list = copy.deepcopy(my_list3) 
res_list.append("2a")
print("Исходный список: ", my_list3)
print("Требуемый список: ", res_list)