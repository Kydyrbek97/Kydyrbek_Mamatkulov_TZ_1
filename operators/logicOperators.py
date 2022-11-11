# Операторы сравнения
# Условные операторы
# Логические операторы

# Операторы сравнения
# == - Если значения двух сравниваемых операнд равны, то условие становится истиной.
# != - Если значения двух сравниваемых операнд НЕ равны, то условие становится истиной.
# > - Если значение левого операнда больше чем значение правого операнда, тогда условие становится истиной.
# < - Если значение левого операнда меньше чем значение правого операнда, тогда условие становится истиной.
# >= - Если значение левого операнда больше или равно значению правого операнда, тогда условие становится истиной.
# <= - Если значение левого операнда меньше или равно значению правого операнда, тогда условие становится истиной.

# <, >, == (равно) <=, >=, !=(не равно)
# 1 < 5 -> True
# 7 > 9 -> False

# num1 = 15 
# num2 = 15
# print (num1 != num2)

# stroka1 = 'hello'
# stroka2 = 'World'

# print(stroka1 > stroka2)
#        #104       #87

# print('Hello world')

# print(ord('H'))
# print(ord('а'))

# print(chr(1080), chr(1089))
# print(ord('И'))

# stroka1 = 'Hello!'
# stroka2 = 'World John Snow'

# print(len(stroka1) > len(stroka2))


# Условные операторы 
# if
# elif
# else

# if <condition>:
#      <body if> # сработает если выражении if  придет True
# [elif] <condition>:
#  <body else> 
# [else]:
#        <body else> #  срабатывает если во всех выше 
#        стоящих условиях пришло False

# string = input('Enter smt: ')
# if string.lower() == 'hello':
#     print('Hello stranger!')
# elif string.lower() =='john':
#     print('Welcome back John Snow! The King of North')
# elif string.lower() == 'abra-Cadabra':
#     print('Sim Salamon Kadabra!')
# else: 
#     print('Совпадений не найдено!')
# print(string)

# email = input('Enter email: ')
# password1 = input('Enter the password: ')
# if len(password1) < 8:
#     raise ValueError('Password to short!')

# password2 = input ('Enter the password confirmation:')

# if password2 != password1:
#     raise ValueError('Passwords didn\t match!')
# else:
#     print('Successfully signed up')

# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid values!')
# if age < 18:
#     print(f'Access Denied! Come again {18 - age} age!')
# else:
#     print('You can buy it')

#  Логические операторы

# and -> логическое и
# or -> логическое или
# not -> логическое отрицание

# my_age = 20 
# your_age = 18
# result = my_age == 20 and your_age == 19
# print(result)

# result = my_age == 21 or your_age == 19
# print(result)

# result = not my_age == 19 and not your_age == 21
# print(result)

# user = 'John'
# is_google_user = False
# is_github_user = True
# is_age_greater_21 = False
# user_coins = 9000

# либо юзер гугла или гитхаба и либо возраст 
# выше 21 либо бабки (8000)

# if (is_google_user or is_github_user)and (is_age_greater_21 or user_coins > 8000):
#     print(f'You can enter the system Mr/Ms {user}!')
# else:
#     print('Sorry, you couldn\'t enter!')

# Операторы идентификации

# in ->  проверяет наличие элемента внутри кого либо
# итерируемого обьекта (строки, списики итд)
# is -> сравнивает ячейки памяти двух обьектов
#   == -> сравнивает по значению
# is not -> отрицательное сравнение ячеек памяти

# str1 = 'Hello world'
# print(str1)
# choice = input('Enter the symbol: ')

# if choice in str1:
#     print(f'The symbol: {choice} exists!')
# else:
#     print(f'The symbol: {choice} does not exists!')



# str1 = 'Hello world'
# print(str1)
# choice = input('Enter the symbol: ')

# if choice not in str1:
#     print(f'The symbol: {choice} does not exists!')
# else:
#         print(f'The symbol: {choice} exists!')

