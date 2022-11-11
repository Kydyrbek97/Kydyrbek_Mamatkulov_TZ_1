# sentence = input('Vvedite predlojeniye: ')


# if sentence [-1] == '?':
#     print('Предложение вопросительное')
# else:
#     print('Обычное предложение')

# sentence = input('Vvedite predlojeniye: ')
# print('Предложение вопросительное' if sentence[-1] == '?' else 'Обычное предложение')
# ------------------------------------------------------------------------------------

# Ternary operator (Тернарный оператор ) - конструкция 
# которая аналогична по своим и действию конструкции if/else но при этом 
# записывается в одну строчку кода.

# <выражение если в условии True> if <условие> 
# else <выражение если False>

# number = 18
# res = 'even' if number % 2 == 0 else 'odd number'
# print(res)

# from string import digits

# is_correct = True
# symbols = digits + '-' 
# print (symbols)
# number = input('Vvedite chislo: ')
# for i in number: # 567
#     if i not in symbols: #0123456789-
#         is_correct = False
# if is_correct:
#     print('Yes number')
#     number = int(number)
#     print ('Your number:', number)
#     result = number if number >= 0 else - number
#                                          #-(56)
#     print(result)
# else:
#     print('Invalid values!')

# if number.isdigit():
#     number = int(number)
#     print ('Да число')
# else:
#     print('Вы ввели не число!')
# ------------------------------

# from string import digits # digits


# flag = True
# symbols = digits + '-' + '.'

# while flag:
#     is_correct_number = True
#     num1 = input('Vvedite pervoe chislo: ')
#     if len(num1) <= 1 and (num1 == '.' or num1 == 
#     '-'):
#         print('Вы ввели не правильное число')
#         is_correct_number = False
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели не правильное число')
#             is_correct_number = False
#             break
#     if not is_correct_number: # 56 # 56y
#         continue
#     num2 = input('Vvedite vtoroe chislo: ')
#     if len(num2) <= 1 and (num2 == '.' or num2 == 
#     '-'):
#             print('Вы ввели не правильное число')
#             is_correct_number = False
#     for x in num2:
#         if x not in symbols:
#             print('Вы ввели не правильное число')
#             is_correct_number = False
#             break
#     if not is_correct_number: # 56 # 56y
#         continue
#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     print(num1)
#     print(num2)

#     operator = input('Vvedite operator(+, -, *, /):')
#     if operator == '+': 
#         print (f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print (f'Результат: {round(num1 - num2, 2)}')
#     elif operator == '*':
#         print (f'Результат: {num1 * num2}')
#     elif operator == '/':
#             if num2 == 0:
#                 print ('На ноль делить нельзя!')
#             else:
#                 print (f'Результат: {num1 / num2}')
#     else:
#         print('Вы ввели неправильный оператор!')
#     choice = input('Хотите остановить(yes)')
#     if choice.lower() == 'yes':
#         flag =False
#         print('Пока!')


