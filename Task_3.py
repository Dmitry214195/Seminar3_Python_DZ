# Задание 3: Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

from random import uniform

number = int(input('Введите размер списка: '))
list = []

for i in range(number):
    list.append(uniform(1, 9))
    list=[round(v,1) for v in list]

print(list)  

list =  [round(i%1,2) for i in list if i%1 != 0]
print(max(list) - min(list)) 