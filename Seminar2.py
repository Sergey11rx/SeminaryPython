# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2


# n = int(input('Введите количество монет: '))
# orel = reshka = 0
# for i in range(n):
#     x = int(input('Орел(1) или решка(0)?: '))
#     if x == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(f'Переверните {orel} монеты с орла на решку, их меньше всего')
# elif orel == reshka:
#     print(f'Количество орлов и решек одинаково, по {orel} штук')
# else:
#     print((f'Переверните {reshka} монеты с решки на орла, их меньше всего'))


# Идеальное решение:
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


# Идеальное решение:
# x = int(input('Задай сумму двух чисел: \n'))
# y = int(input('Задай произведение чисел: \n'))
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(f'Первое число равняется {i}, второе число равняется {j} ')



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


# Идеальное решение:
n = int(input('Введи число N:'))
i = 0
while 2 ** i <= n:
    print(f' 2 в степени {i} равна {2 ** i}')
    i += 1
