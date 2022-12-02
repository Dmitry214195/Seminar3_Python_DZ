# Задание 1: Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint

number = int(input('Введите размер списка: '))
list = []

for i in range(number):
    list.append(randint(0, 9))

summ = 0

for i in range(1, len(list), 2):
    summ += list[i]

print(f"{list} сумма элементов на нечётных позициях: {summ}")