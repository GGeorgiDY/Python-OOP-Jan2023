# class Person:
#     kind = "mammal"
#
#     def __init__(self, age: int):
#         self.age = age
#
#     def increase_age(self, age):
#         self.age += age
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
#
# person = Person(18)
# print(person.is_adult(20))
# print(Person.is_adult(20))

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def pepperoni(cls): # това cls е буквално нашия клас. Все едно взимаме Pizza
#         return cls(["tomato sauce", "parmesan", "pepperoni"])
#
#     @classmethod
#     def quattro_formaggi(cls):
#         return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])
#
#
# first_pizza = Pizza.pepperoni()
# second_pizza = Pizza.quattro_formaggi()

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

