# Функции - это именнования часть программы, 
# которая может вызываться в других частях программы
# столько нужно

# def name_of_function(<a, b> параметры):
#     <body> код какая то логика которая будет
#     запускаться при обращении к функции
#     [<return>] оператор для возвращения результата

# name_of_functions(5,6 # аргументы)

#  Параметры функции - переменные которые будет принимать ваша 
# функция для того чтобы мы могли работать с данными которые попадают 
# в нашу функцию данные сохраняются
 
#  Аргументы - данные которые мы передаем для параметров при вызове функции

# return -  оператор который нужен чтобы функция возвращала результат,
# если нет return в функции, функция по умолчанию возвращает None

# res = print('Hello')
# print(res)

# res = max(range(1,100))
# print(res)

# def sum_two_nums(num1, num2):  # параметры
#     result = num1 + num2
#     return result

# res = (sum_two_nums(5, 6))
# print(res)

# def our_len(a):
#     try:
#         res = 0
#         for x in a:
#             res +=1
#         return res
#     except TypeError:
#         return 'Value is not iterable'

    
# ls = [1,2,3,4,5,6,7,8,9]
# str1 = "Hello world! My name is John Snow!"
# print(our_len(ls))
# print(our_len(str1))
# print(our_len(True))


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     return False
# print(isEven(16))

# b = int(input('Vvedite chislo: '))

# print(isEven(15))
# print(isEven(b))
# print(isEven(24))
# print(isEven(9))

# def get_polindorms(worlds):
#     result = []
#     for x in worlds:
#         if x.lower() == x[::-1].lower():
#             result.append(x)
#     return result

# some_words = ['John', 'ono', 'Kazak', 'peter', 'Dovod', 'tenet', 'anna', 'kak' 'piko']
# polindroms  = get_polindorms(some_words)
# print(polindroms)

# def get_string_length():
#     return 
# print(get_string_length('hello')) 