# from abc import abstractmethod, ABC
#
#
# class Person(ABC):
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def have_birthday(self):
#         self.age += 1
#
#     @abstractmethod
#     def work(self):
#         pass
#
#
# class Employee(Person):
#     def work(self):
#         print("working")
#
#
# class Boss(Person):
#     def work(self):
#         print("taking risks")
#
#
# e1 = Employee("Ivan", 19)
# print(e1.name)          # Ivan
#
# instances = [Boss("ivan", 20), Employee("peter", 19)]
# for instance in instances:
#     instance.work()     # taking risks; working



