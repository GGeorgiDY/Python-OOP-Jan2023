# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#
# x = Dog("Max")
# x.change_name("Rex")
# print(x.name)
# print(x.__dict__)

# принтира
# Rex
# {'name': 'Rex'}


# //////////////////////////////////////////////////////////////////////////////


# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def change_year(self, new_year):
#         self.year = new_year
#
#     def __str__(self):
#         return f"{self.model} made {self.year}"
#
#
# nissan = Car("GT-R", 2012)
# toyota = Car("Supra", 1999)
# cars = [nissan, toyota]
#
# for car in cars:
#     print(car)

# принтира
# GT-R made 2012
# Supra made 1999


# //////////////////////////////////////////////////////////////////////////////


# class MyClass:
#     """This is MyClass."""
#
#     def example(self):
#         """This is the example module of MyClass."""
#
#
# print(MyClass.__doc__)
# print(MyClass.example.__doc__)


# //////////////////////////////////////////////////////////////////////////////

# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def change_year(self, new_year):
#         self.year = new_year
#
#
# nissan = Car("GT-R", 2012)
# toyota = Car("Supra", 1999)
# cars = [nissan, toyota]
#
# print(cars)
# print(cars[0])
# print(cars[0].model)
# print(cars[0].year)
# nissan.change_year(2018)
# print(cars[0].year)
# print(nissan.model)

# //////////////////////////////////////////////////////////////////////////////



# //////////////////////////////////////////////////////////////////////////////