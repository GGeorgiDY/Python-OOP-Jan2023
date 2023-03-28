# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
#
# closure = outer_function(10)
# print(closure(5))
## 15

# ///////////////////////////////////////////////////////////////////////////////////////

# def print_message(message):
#     def message_sender():
#         "Nested Function"
#         print(message)
#     message_sender()
#
#
# print_message("Some random message")
# # Some random message

# ///////////////////////////////////////////////////////////////////////////////////////

# def uppercase(function):
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#
#     return wrapper

# ///////////////////////////////////////////////////////////////////////////////////////

# def my_decorator(func):
#     def wrapper():
#         print('before the functions is called')
#         func()
#         print('after the functions is called')
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print('Hello!')
#
#
# say_hello()


# ///////////////////////////////////////////////////////////////////////////////////////

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
#
#
# @uppercase_decorator
# def say_hi():
#     return 'hello there'
#
#
# print(say_hi())

# ///////////////////////////////////////////////////////////////////////////////////////

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
#
#
# def split_string(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string
#     return wrapper
#
#
# @split_string
# @uppercase_decorator
# def say_hi():
#     return 'hello there'
#
#
# print(say_hi()) # ['HELLO', 'THERE']

# ///////////////////////////////////////////////////////////////////////////////////////

# def decorator_with_arguments(function):
#     def wrapper_accepting_arguments(arg1, arg2):
#         print(f"My arguments are: {arg1}, {arg2}")
#         function(arg1, arg2)
#     return wrapper_accepting_arguments
#
#
# @decorator_with_arguments
# def cities(city_one, city_two):
#     print(f"Cities I love are {city_one} and {city_two}")
#
#
# cities("Nairobi", "Accra")

# # Ще принтира:
# # My arguments are: Nairobi, Accra
# # Cities I love are Nairobi and Accra

# ///////////////////////////////////////////////////////////////////////////////////////

# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
#         print('The positional arguments are', args)
#         print('The keyword arguments are', kwargs)
#         function_to_decorate(*args)
#     return a_wrapper_accepting_arbitrary_arguments
#
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print("No arguments here.")
#
#
# function_with_no_argument()

# Ще принтира:
# The positional arguments are ()
# The keyword arguments are {}
# No arguments here.

# ///////////////////////////////////////////////////////////////////////////////////////

# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
#         print('The positional arguments are', args)
#         print('The keyword arguments are', kwargs)
#         function_to_decorate(*args)
#     return a_wrapper_accepting_arbitrary_arguments
#
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)
#
#
# function_with_arguments(1,2,3)

# Ще принтира:
# The positional arguments are (1, 2, 3)
# The keyword arguments are {}
# 1 2 3

# ///////////////////////////////////////////////////////////////////////////////////////

# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
#         print('The positional arguments are', args)
#         print('The keyword arguments are', kwargs)
#         function_to_decorate(*args)
#     return a_wrapper_accepting_arbitrary_arguments
#
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_keyword_arguments():
#     print("This has shown keyword arguments")
#
#
# function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")

# Ще принтира:
# The positional arguments are ()
# The keyword arguments are {'first_name': 'Derrick', 'last_name': 'Mwiti'}
# This has shown keyword arguments

# ///////////////////////////////////////////////////////////////////////////////////////

# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
#     def decorator(func):
#         def wrapper(function_arg1, function_arg2, function_arg3):
#             "This is the wrapper function"
#             print(f"The wrapper can access all the variables\n"
#                   f"\t- from the decorator maker: {decorator_arg1} {decorator_arg2} {decorator_arg3}\n"
#                   f"\t- from the function call: {function_arg1} {function_arg2} {function_arg3}\n"
#                   "and pass them to the decorated function")
#             return func(function_arg1, function_arg2, function_arg3)
#         return wrapper
#     return decorator
#
#
# pandas = "Pandas"
#
#
# @decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
# def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
#     print(f"This is the decorated function and it only knows about its arguments: {function_arg1} {function_arg2} {function_arg3}")
#
#
# decorated_function_with_arguments(pandas, "Science", "Tools")

# Ще принтира:
# The wrapper can access all the variables
# 	- from the decorator maker: Pandas Numpy Scikit-learn
# 	- from the function call: Pandas Science Tools
# and pass them to the decorated function
# This is the decorated function and it only knows about its arguments: Pandas Science Tools

# ///////////////////////////////////////////////////////////////////////////////////////

# def my_decorator(cls):
#     class NewClass(cls):
#         def new_method(self):
#             print("This is the new method added by the decorator")
#     return NewClass
#
# @my_decorator
# class MyClass:
#     def original_method(self):
#         print("This is the original method of the class.")
#
#
# my_object = MyClass()
# my_object.original_method()
# my_object.new_method()

# Ще принтира:
# This is the original method of the class.
# This is the new method added by the decorator

# ///////////////////////////////////////////////////////////////////////////////////////

# да приемем че имаме уеб сайт, чрез който потребителите могат да си създават профили като подават име, имейл и
# дата на раждане. Можем да използва декоратор, за да ни помогне да валидираме данните.

# from datetime import datetime, timedelta
#
#
# def validate_profile(func):
#     def wrapper(name, email, dob):
#         try:
#             # check that dob is in the correct format (YYYY-MM-DD)
#             dob = datetime.strptime(dob, "%Y-%m-%d")
#
#             # check that user is at least 18 years old
#             eighteen_years_ago = datetime.now() - timedelta(days=365 * 18)
#             if dob > eighteen_years_ago:
#                 raise ValueError("You must be at least 18 years old to create profile")
#
#         except ValueError as e:
#             return str(e)
#
#         # if dob is valid call the original function with the arguments
#         return func(name, email, dob)
#
#     return wrapper
#
#
# @validate_profile
# def create_profile(name, email, dob):
#     # code create user profile
#     return "Profile created successfully"
#
#
# result = create_profile('Ivan Ivanov', 'ivan@gmail.com', '2012-03-21')
# print(result)

# ///////////////////////////////////////////////////////////////////////////////////////

# import functools
#
#
# def uppercase(func):
#     @functools.wraps(func)
#     def wrapper():
#         return func().upper()
#     return wrapper
#
#
# @uppercase
# def say_hi():
#     """Saying Hi"""
#     return "hello there"
#
#
# print(say_hi.__name__)
# print(say_hi.__doc__) # връща док стринга

# ///////////////////////////////////////////////////////////////////////////////////////

# import functools
#
#
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Before function execution")
#         result = func(*args, **kwargs)
#         print("Before function execution")
#         return result
#     return wrapper
#
#
# @my_decorator
# def my_function():
#     """This is my function"""
#     return "Function execution"
#
#
# print(my_function.__name__)                     # my_function
# print(my_function.__doc__) # връща док стринга  # This is my function

# ///////////////////////////////////////////////////////////////////////////////////////

class Cached:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result


@Cached
def example(x):
    result = x ** 2 + 3 * x + 1
    return result


print(example(2)) # slow, защото не е направено такова изчисление
print(example(2)) # fast, защото ще проверим дали това изчисление го имаме вече в кеша и ако го имаме няма да имаме
# нужда го изчисляваме наново
print(example(3)) # slow
print(example(3)) # fast