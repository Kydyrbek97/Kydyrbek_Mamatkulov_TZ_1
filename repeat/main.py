# Вам дан файл article.txt
# Требуется реализовать функцию longest_words(filename: str),
# которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).

# def longest_words(filename):
#     with open (filename) as file:
#         words = file.read().split()
#     words.sort(key=len, reverse=True)
#     max_len = len(words[0])
#     res = []
#     for i in words:
#         if len(i) == max_len:
#             res.append(i)
#         else:
#             break
#         return res if len(res) > 1 else res.pop()
# print (longest_words('test.txt'))

# ============================================================================================

# 1.Вам дан список accounts, элементами которого являются другие списки
# Каждый список представляет собой количество денег на счету клиента.
# Напишите функцию которая выводит максимальное количество денег на счету самого богатого клиента.

# Пример:
# accounts = [[1,5],[7,3],[3,5]]
# Ожидаемый вывод: 10

# accounts = [[1,5],[7,3],[3,5]]
# res = []
# for i in accounts:
#     res.append(sum(i))# [1,5] -> 6,10,8

# print(max(res))

# ------------------------------------------------------
# res = [sum(i) for i in accounts]

# --------------------------------------------------------

# 2.Вам даны две строки:
# Word - слово, ch - буква.
#  Напишите функцию которая будет переварачивать сегмент слова (word),который начинается с индекса 0 и
# заканчивается индексом первого вхождения ch(включительно).
# Если ch не существует в слове, возвратите переменную word.

# Пример:
# Ввод: word = "abcdefd", ch= "d"
# Ожидаемый вывод: "dcbaefd"
# Объяснение:
# Первое вхождение "d" находится в индексе 3.
# Переверните часть слова от 0 до 3 (включительно), в результате получится строка «dcbaefd».

# word = "abcdefd"  # -> "dcbaefd"
# ch = "d"


# def func(word, ch):
#     mid = word.index(ch)  # 3
#     s1 = word[0:mid+1]  # abcd [::-1]
#     s2 = word[mid+1:]  # efd
#     return s1[::-1]+s2


# print(func(word, ch))

# --------------------------------------------------------

# Напишите func которая фильтрует строковые данные в списке.
# Если строка является числом, то преобразуйте его в числовой тип и
# запишите в список, иначе пропустите строку.
# Ввод:
# ['123', '12sd', '54', 'das', '142']
# Вывод:
# [123, 54, 142]


# def func(l):
#     res = [int (i) for i in l if i.isdigit()] # list comprehensions
#     res = []
#     for i in l:
#         if i.isdigit():
#             res.append(int(i))
#     return res

# print(func(['123', '12sd', '54', 'das', '142']))

# --------------------------------------------------------

# Дан словарь, удалите из него все элементы с пустыми значениями.

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for i in a:
#     if a[i] != None:
#         b.update({i:a[i]})
# print(b)

# --------------------------------------------------------

# 1) Откройте файл task5.txt. В нём записаны целые числа.
# Прочтите эти числа, затем найдите максимальное затем минимальное число.
# Затем запишите эти числа в новый файл task6.txt через символ - (сначала минимальное, потом максимальное)

# with open('task5.txt', 'r') as f:
#     res = []
#     num = f.read()
#     for i in num.split():
#         res.append(int(i))
# with open('task6.txt', 'w') as fs:
#     print(max(res), file=fs)
#     print(min(res), file=fs)

# --------------------------------------------------------
# with open('task5.txt', 'r') as file:
#     res = []
#     for i in file.read():
#         if i.isdigit():
#             res.append(int(i))
#     with open('task6.txt', 'w') as file:
#         file.write(f'{min(res)}-{max(res)}')

# --------------------------------------------------------

# 2) Расчет премии сотрудникам
# salary- это заработная плата в месяц, overTime- количество часов,
# которое сотрудник взял сверхурочно, задача: создать функцию, которая будет
# добавлять к основной зарплате сверхурочное время(1час=200$), функция должна принимать список
# со словарями и возвращать также список, но уже с измененными данными пример:
# [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]

# res = []
# for i in employees:
#     name = i['name']
#     salary = i['salary']
#     overtime = i['overTime']
#     salary += overtime * 200
#     res.append({'name':name, 'salary': salary})
# print(res)

# --------------------------------------------------------

# Даны три переменные a, b и c. Изменить значения этих переменных так,
# чтобы в a хранилось значение a+b, в b хранилась разность старых значений c− b, а в c
# хранилось сумма старых значений a+b+c.
# Пример: a=0, b=2, c=5, тогда новые значения a=2, b=3 и c=7.

# a = 0
# b = 2
# c = 5
# a,b,c = a+b, c-b, a+b+c
# print(a,b,c)

# --------------------------------------------------------
# Написать функцию, которая выводит периметр, площадь и диагональ квадрата,
# после того как пользователь вводит сторону.

# from math import sqrt

# def func(a):
#     p = a*4
#     s = a**2
#     d = a*sqrt(2) # 2**0.5
#     return p,s,d
# print(func(4))

# --------------------------------------------------------

# Дано четырехзначное число.
# Поменяйте местами наименьшую и наибольшую цифры.
# Пример: 1234 => 4231

# a = 1234
# ref = list(str(a))
# min_num = min(ref)
# max_num = max(ref)
# idx1 = ref.index(min_num)
# idx2 = ref.index(max_num)
# ref[idx1] = max_num
# ref[idx2] = min_num
# print(int("".join(ref)))
# #ASCII

# --------------------------------------------------------

# Напишите программу, которая проходиться по числам в диапазоне от 1 до 50. Вывести “Fizz”
# для чисел в этом диапазоне, которые кратны 3, вывести “Buzz” для чисел,
# которые кратны 5 и вывести “FizzBuzz” для чисел которые делятся и на 3 и на 5.

# for i in range (1,51):
#     if i%3 == 0  and i%5 == 0:
#         print('FIZZBUZZ')
#     elif i%3 == 0:
#         print('FIZZ')
#     elif i%5 == 0:
#         print('BUZZ')

# --------------------------------------------------------

# Вывести все пятизначные числа, которые делятся на 2, у которых средняя цифра нечетная,
# и сумма всех цифр делится на 4.
# Пример: 33541, 73541 и тд.

# res = []
# for i in range(10000, 100150):
#     mid = len(str(i)) // 2
#     if i%2 == 0 and int(str(i)[mid]) % 2 !=0 and sum([int(i) for i in str(i)]) % 4 == 0:
#         res.append(i)
# print(res)

# --------------------------------------------------------

# Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs,
# содержащий только визиты из России. Считайте, что список geo_logs легко помещается в оперативной памяти.
# geo_logs = [{"visit2": ["Дели", "Индия"]}, {"visit3": ["Владимир", "Россия"]}, {"visit9": [“Курск", “Россия"]}]

# geo_logs = [{"visit2": ["Дели", "Индия"]}, {"visit3": ["Владимир", "Россия"]}, {"visit9": ["Курск", "Россия"]}]

# for i in geo_logs.copy():
#     # print(i.values())
#     key = list(i.keys())[0]
#     if not 'Россия' in list(i.values())[0]:
#         geo_logs.remove(i)
# print(geo_logs)

# --------------------------------------------------------

# Дана дата из трех чисел (день, месяц и год). Вывести Yes, если такая дата существует
#  (например, 12.02.1999 => yes, 22.12.2001 => no).
#  Примечание*(Считать количество дней в феврале как 28 дней)



# date_ = '22.12.2001'
# date_2 = '12.03.1999'
# def func(date_):
#     res = []
#     ref = date_.split('.')
#     date = ref[0]
#     month = ref[1]
#     year = ref[-1]
#     if int(month) <= 12:
#         if month not in ['02', '04', '09']:
#             if int(date) in range(1,32):
#                 res.append(True)
#             else:
#                 res.append(False)
#         elif month == '04' or month == '09':
#             if int(date) in range(1,31):
#                 res.append(True)
#             else:
#                 res.append(False)
#         elif month == '02':
#             if int(date) in range(1,29):
#                 res.append(True)
#             else:
#                 res.append(False)
#     else:
#         res.append(False)
#     if year != '0':
#         res.append(True)
#     else:
#         res.append(False)
#     return 'Yes' if all(res) else 'No'
# print(func(date_2))
        
def upper(string):
    return string(upper)

new_list = ['nwqe']

res = list(map(upper, new_list))
print(res)