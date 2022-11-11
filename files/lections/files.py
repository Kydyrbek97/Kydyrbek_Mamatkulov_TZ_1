# Работа с файлами

# | -> каретка - указатель - курсор

# open(<путь до файла>)

# file = open('/home/User/Desctop/en/files/lections/files.py')# абсолютный путь
# file = open(files.py)# относительный путь (относительно к той директории в которой вы работаете)

# Режимы работы с файлами

# 1. чтения -> r/r+(read)
# 2. записи -> w/w + (write)
# 3. добавления -> a/a+(append)
# b x t

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(len(data))
# file.close

# контекстный менеджер

# with open('test.txt') as file:
#     print(file.tell())
#     data = file.read()
#     index = data.index('My')
#     print(file.tell())
#     file.seek(index)
#     print(file.read())
#     print(file.tell())

# file.tell() -> возвращает индекс где находится
# указатель (курсор/каретка)
# file.seek(index) -> перемещает каретку на индекс
# который вы передали

# with open('test.txt', 'r') as file:
#     print(file.readlines())
#     file.seek(0)
#     print(file.readline())
#     print(file.readline())

# print(file.read()) # Ошибка

# with open('test.txt', 'a+') as f:
#     f.write('\nHe is bastard of Ned Stark')
#     f.write('\nThis is lesson about files')
#     f.seek(0)
#     print(f.read())

# with open('test.txt', 'w') as file:
#     file.write('Hello, was opened with open!')

# ---------------------------------------------------
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re


# def get_imei_codes(image):
#     string = pytesseract.image_to_string(image)
#     print(string)
#     list_of_imei = re.findall(r'IME.\d.\s\d+', string)
#     print(list_of_imei)
#     with open('imei_codes.txt', 'w') as file:
#         for x in list_of_imei:
#             file.write(f'{x}\n')


# ls = 'imei.jpg'
# get_imei_codes(ls)
# -------------------------------------------------------------------------

# with open('test.txt', 'r') as f:
#     res = []
#     num = f.read()
#     for i in num.split():
#         res.append(int(i))
# with open('task6.txt', 'w') as fs:
#     print(max(res), file=fs)
#     print(min(res), file=fs)

# a = int(input("Зарплата за месяц: "))
# b = int(input("Количество отработанных в выходные часов: "))


# def salary():
#     if b <= 40:
#         salary = a * b
#     elif b > 40:
#         salary = a * (1.5 * (b - 40))
#     return salary


# print(salary("Размер премии: "))

# 2) Расчет премии сотрудникам
# salary- это заработная плата в месяц, overTime- количество часов, 
# которое сотрудник взял сверхурочно, задача: создать функцию, которая будет 
# добавлять к основной зарплате сверхурочное время(1час=200$), функция должна 
# принимать список со словарями и возвращать также список, но уже с измененными 
# данными пример: [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]


# with open('test.txt', 'r') as file:
#     file.seek(0)
#     data = file.read(9)
#     print(data)