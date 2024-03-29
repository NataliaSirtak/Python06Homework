import sys

# Задание 2.1 Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
# health = int(input('Введите уровень здоровья вашего персонажа: '))
# if health > 0:
#     print('True')
# else:
#     print('False')
# Задание 2.2 Напишите программу, которая проверяет является ли введенное число четным. Если да,
# выведите на экран текст “Четное”,а иначе - “Нечетное”
# number = int(input('Введите любое число: '))
# if number % 2:
#     print('Нечетное')
# else:
#     print('Четное')
# Задание 2.3 Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# С вложенными условиями
# year = int(input())
# if year%4 == 0:
#   if year%100 == 0:
#   if year%400 == 0:
#             print('Високосный')
# else:
#             print('Невисокосный')
# else:
#             print('Високосный')
# else:
#             print('Невисокосный')
# C логическими операторами
# year = int(input())
# if not year % 4 and year % 100 or not year % 400:
#     print('Високосный')
# else:
#     print('Невисокосный')
# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()
# С циклом while

# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# i = 1
# while i <= num:
#     print(text)
#     i += 1
# # С циклом for
# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# for i in range(1, num+1):
#     print(i, text)
# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
# C применением функции eval()
try:
    num1 = int(input('Пожалуйста, введите первое число: '))
    num2 = int(input('Пожалуйста, введите второе число: '))
except ValueError as e:
    print(f'Введенное значение не является числом: {e}')
    sys.exit()
operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
if operator not in '+-*/%':
    print("Вы ввели не правильный оператор!")
    sys.exit()
result = 0
if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
else:
    result = eval(f'{num1} {operator} {num2}')
    print(f'{num1} {operator} {num2} = {result}')
