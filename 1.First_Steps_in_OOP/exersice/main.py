# def choice_pattern():
#     pattern = input('Choice type of pattern ->\n- Triangle\n- Rombus\n- Square\n- Pattern choice: ')
#     size_of_pattern = int(input('Enter pattern size: '))
#     return pattern, size_of_pattern
#
#
# def print_pattern_data(space_data, stars_data):
#     print(' ' * space_data + '* ' * stars_data)
#
#
# def get_pattern_data(data):
#     pattern, size = data
#
#     if pattern == "Rombus":
#         for x in range(size):
#             space_data = size - x - 1
#             stars_data = x + 1
#             print_pattern_data(space_data, stars_data)
#
#         for x in range(size - 2, -1, -1):
#             space_data = size - x - 1
#             stars_data = x + 1
#             print_pattern_data(space_data, stars_data)
#
#     elif pattern == 'Triangle':
#         for x in range(size):
#             stars_data = x + 1
#             print_pattern_data(0, stars_data)
#
#     elif pattern == 'Square':
#         for x in range(size):
#             stars_data = size
#             print_pattern_data(0, stars_data)
#
#
# get_pattern_data(choice_pattern())

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# val = 'global'
#
#
# def func1():
#     def func2():
#         print(val)
#     func2()
#
#
# func1()

# ще върне
# global

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# val = 'global'
#
#
# def func1():
#     def func2():
#         value = 'local'
#         print(value)
#     func2()
#
#
# func1()

# ще върне
# local

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# value = 'global'
#
#
# def func1():
#     print(value)
#
#
# def func2():
#     value = 'Local value func_2'
#     print(value)
#
#
# func2()

# ще върне
# Local value func_2 защото първо търси дали в локалния scope (във функцията има такава променлива)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# value = 'global'
#
#
# def func1():
#     print(value)
#
#
# def func2():
#     value = 'Local value func_2'
#     print(value)
#
#
# def func3():
#     value = 'Local value func_3'
#     print(value)
#
#     def nested_func3():
#         value = 'Local value in nested func_3'
#         print(value)
#
#     nested_func3()
#
#
# func3()

# ще върне
# Local value func_3
# Local value in nested func_3

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# a = 1
#
# def add_func():
#     a += 2
#     print(a)
#
# add_func()

# ще върне
# Error

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# a = 1
#
# def add_func():
#     global a
#     a += 2
#     print(a)
#
# add_func()

# ще върне
# 3

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def func1():
#     x = 'SoftUni'
#
#     def func2():
#         x = 'Harvard'
#
#     func2()
#     return x
#
# print(func1())

# ще върне
# SoftUni

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def func1():
#     x = 'SoftUni'
#
#     def func2():
#         nonlocal x
#         x = 'Harvard'
#
#     func2()
#     return x
#
# print(func1())

# ще върне
# Harvard

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# x = 'UNWE'
#
# def func1():
#     x = 'SoftUni'
#
#     def func2():
#         nonlocal x
#         x = 'Harvard'
#
#     func2()
#     return x
#
# print(func1())

# ще върне
# Harvard

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# archi = Dog('Archi', 9)
# buddy = Dog('Buddy', 3)
#
# print(f'Dog name is: {archi.name}\nDog age is: {archi.age}')
# print(f'Dog name is: {buddy.name}\nDog age is: {buddy.age}')

# ще върне
# Dog name is: Archi
# Dog age is: 9
# Dog name is: Buddy
# Dog age is: 3

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def show(self):
#         return f'Model is:, {self.model}/nColor is:, {self.color}'
#
#
# audi = Car('Audi A8/B7', 'Black')
# mercedes = Car('Mercedes S500', 'White')
#
# print(audi.show())


# ще върне
# Model is:, Audi A8/B7/nColor is:, Black

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||