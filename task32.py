
# Задача 32: Определить индексы элементов массива (списка),значения которых принадлежат
# заданному диапазону (т.е. неменьше заданного минимума и не больше заданного максимума)

import random

ls = [random.randint(-20, 20) for i in range(int(input('введите кол-во эл-тов: ')))]
min_ls, max_ls = [int(i) for i in input('введите минимум и максимум: ').split()]
print(ls)

if max_ls < min_ls:
    max_ls, min_ls = min_ls, max_ls
print(f'min = {min_ls}, max = {max_ls}')

count = 0  # если не найдем ни одного элемента в заданном диапазоне
for i in range(len(ls)):
    if min_ls <= ls[i] <= max_ls:
        print(i, end=' ')
        count += 1

if not count:
    print('нет чисел в заданном диапазоне')