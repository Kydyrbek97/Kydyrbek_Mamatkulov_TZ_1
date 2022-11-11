# import random
# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Oromo']
# p = 0
# m = 0
# k = 0
# l = 0
# o = 0
# for x in range (0, 1000):
#     # print(x)
#     choice =  random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#             p += 1
#     elif choice.lower() == 'manty':
#             m += 1
#     elif choice.lower() == 'kuurdak':
#             k += 1
#     elif choice.lower() == 'lagman':
#             l += 1
#     else: 
#         o += 1
        
   
# print('Результаты голодных игр:')
# print(f'Plov: {p}\nManty: {m}\nKuurdak: {k}\nLagman: {l}\nOromo: {o} \nПобедитель: {(random.choice(ls))} ')


# # Угадать кто будет победитель Д/З


# first = int(input('Введите число: '))
# second = int(input('Введите число: '))
# third = input('Выберите операцию из следующих +-*/%**// : ')
# if first and third == '+':
#     print(first + second)
# elif first and third == '-' :
#     print(first - second)
# elif first and third == '*' :
#     print(first * second)
# elif first and third == '/' :
#     print(first / second)
# elif first and third == '%' :
#     print(first % second)
# elif first and third == '**' :
#     print(first ** second)  
# elif first and third == '//' :
#     print(first // second)   
# else:
#     print('Данной операции нет в системе') 
  
# =========================================================================



"""
2.Объявите переменную со значением типа данных int и распечайте ее.
"""
# писать код здесь



"""
3.Примите от пользователя 2 целых числа и создайте ещё одну переменную со значением типа float. Найдите остаток от деления первых двух чисел, и затем умножьте его на третье число.
"""
# писать код здесь

"""
4.Даны две переменные со значением типа int. Найдите остаток от деления первого на второе и распечатайте результат.
"""
# писать код здесь

"""
5.Дана строка, распечатайте последние 2 символа.
"""
# писать код здесь


"""
6.Объявите строку "abracadabra", затем поменяйте шестую букву на "K". Например: "abracadabra" -> abracKdabra.
"""
# писать код здесь


"""
7.Даны несколько хэштегов, разделённых символом "#". Разделите их в отдельные строки. Например: #makers#bootcamp#программирование#it#курсы -> ['makers', 'bootcamp', 'программирование', 'it', 'курсы']
"""
# писать код здесь

# x = 33
# y = 0
# z = 36
# if y or z <= x:
#     print(y)
# else:

#     print(x)

# ------------------------------------------------------------------
"Check Yourself 4-week"

# 1) Дан список, со строками. Отфильтруйте
# этот список, оставив только те строки, длина
# которых больше 7 символов.

# list_ = ['Darika', 'Sanjar', 'Aizirek', 'Oleg', 'Nuraiym']
# list2 = [x for x in list_ if len(x) > 7]
# print(list2)

# list1 = []
# for x in list_:
#     if len(x) > 7:
#         list1.append(x)
# print(list1)

# 2) Вам дано три числа(имеется в виду создать
# 3 переменные с числовыми значениями),
# используйте условные операторы и выведите на
# экран наибольшее из них.

# a = 8
# b = 3
# c = 2

# if a > b and a > c:
#     print(a)
# elif b < a and c < a:
#     print(b)
# else:
#     print(c)

# 3) Дан список с числами. Посчитайте
# количество чётных и нечётных чисел в этом
# списке.

# c = [1,2,6,1,8,4]
# chet = 0
# nechet = 0
# for i in a:
#     if i % 2:
#         chet += 1
#     else:
#         nechet += 1
# print(f'Четных: {chet}, Нечетных: {nechet}')

# b = [x for x in c if x%2 == 0]
# c = [x for x in c if x%2]
# print(f'Четные: {len(b)}, нечетные: {len(c)} ')

# 4) Дана строка распечатать true если она является палиндромом и. false если не является
# (Палиндро́м, пе́ревертень — число,
# буквосочетание, слово или текст, одинаково
# читающееся в обоих направлениях. Например,
# число 101; слова "кок", "топот", "комок" и
# т.д.)

# a = ['pop','Pop',101,234,'sdsd']
# b = []
# if a == a[::-1]:
#     print(True)
# else:
#     print(False)

# for i in a:
#     i = str(i)
#     if i.lower() == i[::-1].lower():
#         b.append(True)
#     else:
#         b.append(False)
# print(b)


# 5) Дан список list_ = [-1, 2, 3, 0, 5, -3,
# 7,]. Если число в списке меньше 0, замените
# его на False, если больше, то на True

# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# list1 = []
# for i in list_:
#     if i < 0:
#         list1.append(False)
#     else:
#             list1.append(True)
# print(list1)

# for i in list_:
#     if i > 0:
#         list_.insert(list_.index(i),'True')
#         list_.remove(i)
#     else:
#         list_.insert(list_.index(i),'False')
#         list_.remove(i)

# print(list_)

# for i in range(len(list_)):
#     if list_[i] > 0:
#         list_[i] = True
#     else:
#         list_[i] = False
# print(list_)