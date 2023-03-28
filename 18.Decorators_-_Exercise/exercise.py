# def repeat_n_times(func): # това е декоратора
#     def wrapper(*args): # нещото което ще се изпълни когато извикаме def repeat_n_times(func)
#         for _ in range(3):
#             func(*args)
#     return wrapper
#
#
# @repeat_n_times
# def hello(name):
#     print(f'Hello, {name}')
#
#
# hello('Alice')

# //////////////////////////////////////////////////////////////////////

# # горния пример може да се направи и така
# def repeat_n_times(n):
#     def decorator(func):
#         def wrapper(*args): # нещото което ще се изпълни когато извикаме def repeat_n_times(func)
#             for _ in range(n):
#                 func(*args)
#         return wrapper
#     return decorator
#
#
# @repeat_n_times(3)
# def hello(name):
#     print(f'Hello, {name}')
#
#
# hello('Alice')

# //////////////////////////////////////////////////////////////////////

# подобно на 7ма задача, само че ако в @store_results имаме вкарано число (аргумент).
# В този случай изместваме всичко един път надолу.

# class store_results:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(*args):
#             print(f"Function '{func.__name__}' was called. Result: {func(*args)}")
#             print("The argument is", self.arg)
#         return wrapper
#
#
# @store_results(6)
# def add(a, b):
#     return a + b
#
#
# @store_results(5)
# def mult(a, b):
#     return a * b
#
#
# add(2, 2)
# mult(6, 4)

# //////////////////////////////////////////////////////////////////////