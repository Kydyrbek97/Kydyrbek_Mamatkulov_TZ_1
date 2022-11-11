# num = 1
# while num >= 0:
#     try:
#         num = int(input('Введите число: '))
#     except ValueError:
#         pass
# else:
    
#     print('Встретилось отрицательное число!')

#-------------------------------------------------------

# from random import randint

# ls = []

# for x in range(0,100):
#     ls.append(randint(1,50))

# print(ls)
# ls = list(set(ls))
# res = sorted(ls)
# print(res)

#-------------------------------------------------------

# def introduce(name, last_name, wife='холост', **kwargs):
#     print(f'Привет это {name} {last_name}')
#     print(f'Он {wife}!')
#     if kwargs:
#         print(f'Инициалы его жены {" ".join(kwargs.values())}')
# introduce('John', 'Snow')
# introduce('Tirion', 'Lanister', 'Женат', wife_name='Sansa', wife_last_name='Stark' )

#-------------------------------------------------------

# roles = {
#     0: 'Admin',
#     1: 'Customer',
#     2: 'Vendor',
# }

# users = [
#     {
#         'id': 1,
#         'username': 'John',
#         'role': roles[0]
#     },
#      {
#         'id': 3,
#         'username': 'Tirion',
#         'role': roles[2]
#     },
#     {
#         'id': 2,
#         'username': 'Raychel',
#         'role': roles[1]
#     }
# ]

# product = {
#     'id': 1,
#     'title': 'Iphone 14',
#     'description': 'Lorem Ipsum',
#     'price': 1200
# }

# print(f'Before: {product}')

# id_user = int(input('Vvedite svoi id: '))
# try:
#     user = list(filter(lambda x: x['id'] == id_user, users))[0]
#     print(f'Welcome {user}')
# except IndexError:
#     raise ValueError('Invalid id for user! User with this id does not exists!')

# if user['role'] == roles[0]:
#     choice = input('Vvedite chto izmenit\': ')
#     product[choice] = input('Vvedite novoe znacheniye: ')
# else:
#     raise Exception('Permission denied!')

# print(f'After: {product}')

#-------------------------------------------------------

# def deposit(money, period):
#     if money < 30000:
#         raise Exception('Min stavka 30 000 somov')
#     if period < 3:
#         raise Exception('Min srok 3 goda!')

#     i = 0
#     while i < period:
#         money += money * 0.1
#         # money = money * 1.1
#         # money = money + (money / 100 * 10)
#         i += 1
#     return money

# money = int(input('Vvedite summu deneg: '))
# year = int(input('Vvedite srok vashego deposita: ')) 

# print(deposit(money,year))

#-------------------------------------------------------

# ls = [[100,2,3], [300,3,5],[200,50,50,50], [45,45,6]]

# def find_max(ls):
#     return max (sum(x) for x in ls)

# print(find_max(ls))

#-------------------------------------------------------


# def get_reverse_string(text):
#     spisok = text.split()[::-1]
#     return ' '.join(spisok)
# print(get_reverse_string('Hello world! May name is John, last name is Snow. Nice too meet you'))
# print(get_reverse_string('hello john snow king'))



# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# res = [x for x in nums if x < 5]

# for i in nums:
#     if i < 5: 
#         res.append(i)
# print(res)