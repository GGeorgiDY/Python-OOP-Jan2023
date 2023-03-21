# my_list = [1, 2, 3, 4, 5]
#
# my_iterator = iter(my_list)
# print(next(my_iterator))    # 1
# print(next(my_iterator))    # 2
# print(next(my_iterator))    # 3
# print(next(my_iterator))    # 4
# print(next(my_iterator))    # 5
# # print(next(my_iterator))    # StopIteration
#
# try:
#     print(next(my_iterator))
# except StopIteration:
#     print("no more iterators") #no more iterators
#
# print("Bye")                # Bye

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class MyIterator:
#     def __init__(self, start=1, end=11):
#         self.current = start
#         self.end = end
#
#     def __iter__(self): # това просто връща самия обект
#         return self
#
#     def __next__(self): #
#         if self.current >= self.end:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current -1
#
#
# my_iterator = MyIterator()
# for num in my_iterator:
#     print(num)                  # връща числата от 1  до 10

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
#
# for el in my_list:
#     print(el, end=' ') # 1 2 3 4 5
#
# while True:
#     try:
#         el = next(my_iterator)
#         print(el, end=' ')
#     except StopIteration:
#         break

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         else:
#             result = self.start
#             self.start += 1
#             return result
#
#
# for i in MyRange(1, 11):
#     print(i)                # връща числата от 1 до 10

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def string_generator(string):
#     for char in string:
#         yield char
#
# my_string = 'Hello SoftUni'
# for char in string_generator(my_string):
#     print(char, end=' ')  # H e l l o   S o f t U n i

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
# sum_first_n = sum(first_n(5))
# print(sum_first_n) # 10

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def my_generator(n):
#     i = 0
#
#     while i < n:
#         yield i
#         i += 1
#
#
# gen = my_generator(5)
# for value in gen:
#     print(value, end = " ")

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def return_example():
#     return 1
#     return 2
#     return 3
#
#
# def yield_example():
#     yield 1
#     yield 2
#     yield 3
#
#
# print(return_example()) # 1
# print(yield_example()) # връща някаква памет
# for value in yield_example():
#     print(value, end=' ') # 1 2 3

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def count_up_to(n):
#     num = 1
#
#     while num <= n:
#          yield num
#          num += 1
#
#
# it = count_up_to(5)
# for num in it:
#     print(num, end=' ') #1 2 3 4 5

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def my_gen():
#     n = 1
#     print('This is printed first')
#     yield n
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n
#
# gen = my_gen()
# for i in gen:
#     print(i)
#
# gen = my_gen()
# x = [val for val in gen]
# print(x)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# squares = (x * x for x in [1, 2, 3, 4, 5])
# squares2 = [x * x for x in [1, 2, 3, 4, 5]]
# print(squares) # <generator object <genexpr> at 0x000001EA08A59BD0>
# print(squares2) # [1, 4, 9, 16, 25]

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class SumOfSquares:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return (x * x for x in range(self.start, self.end + 1))
#
#     def sum(self):
#         return sum(self)
#
#
# s = SumOfSquares(1, 5)
# for x in s:
#     print(x)
#
# print(s.sum())

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||