#Задача 30:  Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
#a1 = int(input('Введите первый эллемент: '))
#d = int(input('Введите разность: '))
#n = int(input('Введите количество элементов : '))
#for i in range(n):
 #   print(a1 + i * d, end=' ')
#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
max = int(input('Введите максимум: '))
min = int(input('Введите минимум: '))
for i in range(len(list_1)):
    if min <= list_1 [i] <= max:
        print(i, end=' ')