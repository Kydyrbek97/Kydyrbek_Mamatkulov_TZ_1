# Типы данных ->  Числа int(), float()

#  = -> оператор присваивания
# number = 5 # variable (переменная)
# print (number)
# number = 51 
# print (number)
# tommorow_day -> snake case
# tommorowDay -> Camel case
# abc -> нижний регистр
# ABC -> верхний регистр
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#  + 
# num1 = 5
# num2 = 15
# result = num1 + num2
# print (result)

# print('Результат суммы чисел 5 и 15:', 5+15)

# a = 100
# b = 1000
# c = 500 # int
# d = 56.25 # float
# print(a+b+c+d)
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# # - 
# num1 = 996
# num2 = 67.55
# print(num1 - num2)
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# # *
# num1 = int(input(('Введите число 1:')))
# num2 = int(input(('Введите число 2:')))
# result = num1 * num2
# print('Результат произведения чисел', num1, 'и', num2, 'равно:', result)
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# num1 = input('Введите число') 
# print(num1)
# print(type(num1))

# num = '15'
# num = int(num) # '15' -> 15
# print(type(num))

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# # / and // and %
# / -> обычное деление 
# // -> Целочисленное деление (деление без остатка)
# % -> Модульное деление (остаток от деления)

# num1 = 25 
# num2 = 12
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#  ** -> возведение в степень 
# num1 = 5 
# print(num1**3)
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# pow(a,b) - функция возведения числа а в степень b 

# print(pow(2,2,5)) #  2 ** 5 % 5 -> 2
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# divmod (a,b) -> Она выводит два числа, первое чиcла это результат целочисленного деления (//), 
# а второе число это модульное деление (%) двух чисел
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# res = divmod(4,5)
# print(res)
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# round() -> функция округления числа

# res = 24/13
# print(round(res, 2))
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# abs () - абсолютное значение -> abs(-5) = 5 -> |-5| = 5

# print (abs(-101))
# print(abs(50))
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# import math
# from math import pi, sqrt
# print (pi)
# print(sqrt(25))

# print(math.pi)
# #  math.sqrt -> корень числа
# print(math.sqrt (25))
# print(math.sqrt (101))
# print(math.sqrt (6))

# dir () - возвращает  методы обьекта или функции
# определенного модуля
# import math
# print (dir(math)

"""
Множественное присваивание
"""
# a = 5
# a, b, c = 1,2,3
# v = 5
# n = 7
# d = 3
# v, n, d = d, v, n
# print (v, n, d)

"""
1. Даны две переменные num1 со значением 10 и num2 
"""
# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1,num2)

# print('hello' *3) # дублирование строк

# str1 = '12'
# num1 = 2
# print (str1+str(num1))

"""
Инкремент и Дикремент
"""

#  Инкремент - увеличение значения какой либо переменной Пример: a = 1 (a += 1 -> 
# a = a +1 )

# a = 10 
# a += 1
# print(a)

#  Дикремент  - уменьшение значения какой либо переменной. (a -= 1 -> a = a -1)

# a = 8
# a -= 1
# print(a)

# *

# a = 5
# a *= 3
# print(a)

# /

# a = 15
# a /= 3
# print(a)

'''
id() -> номер в ячейке памяти
'''

# a = 2
# b = 1
# print(id(a))
# print(id(b))

# type () -> выводит тип заданной переменной

# a = 9
# b = 'hello'
# print (type(a), type(b))

# var = int(input('Введите число:'))

"""

"""
# num1 = int(input("Введите число:"))
# num2 = int(input("Введите степень:"))
# print(num1 ** num2)

"""
Модуль random - предоставляет функции для генерации 
случайных чисел, буквы, символы
"""
# import random

# print (dir(random))

# num = random.randint(1111,9999)
# print(num)

# from random import choice
# import string
# print(string.ascii_letters_letters)
# a = choice (string.ascii_letters)
# print(a)
 
# from math import pi
# r = int (input('введите радиус:'))
# result_P = 2 * r * pi
# result_S = pi * (r ** 2)
# print('площадь окружности', round(result_S))
# print('периметр окружности', round(result_P))

