# Енкапсулация

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number #вече става прайвет
#         self._balance = balance #вече става прайвет
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         self._balance += amount
#
#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print('Insufficient balance!')
#
#
# account = BankAccount('12345', 1000)
# print(account.get_balance())
# account.deposit(500)
# print(account.get_balance())
# account.withdraw(2000)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Абстракция

# from abc import ABC, abstractmethod
#
#
# class Animal(ABC): # подсказваме че класа ни ще бъде абстрактен
#     @abstractmethod
#     def make_sounds(self):
#         pass # не е имплементиран в този клас, а в подкласове, които го наследяват
#
#
# class Dog(Animal):
#     def make_sounds(self):
#         print('bark')
#
#
# class Cat(Animal):
#     def make_sounds(self):
#         print('meow')
#
#
# class Bird(Animal):
#     def make_sounds(self):
#         print('brrrr')
#
#
# dog = Dog()
# cat = Cat()
# bird = Bird()
#
# dog.make_sounds() #принтира bark
# cat.make_sounds() #принтира meow
# bird.make_sounds() #принтира brrrr

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Полиморфизъм - третираме обекти от различни класове сякаш са от един и същ клас, стига да споделят един и същ интерфейс
# и едно и също поведение

# class Animal:
#     def speak(self):
#         print('Animal speaks')
#
#
# class Dog(Animal):
#     def speak(self):
#         print('Dog speaks')
#
#
# class Cat(Animal):
#     def speak(self):
#         print('Cat speaks')
#
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
#
# animal.speak() # принтира Animal speaks
# dog.speak() # принтира Dog speaks
# cat.speak() # принтира Cat speaks

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.hobbies = []
#
#     def add_hobby(self, hobby):
#         self.hobbies.append(hobby)
#
#     def __str__(self):
#         return f'{self.name} - has hobbies: {self.hobbies}'
#
#
# class FootballPlayer(Person): # наследява Person
#     def __init__(self, name):
#         super().__init__(name)
#         self.add_hobby('Football')
#         self.add_hobby('Fitness')
#
#
# mike = FootballPlayer('Mike')
# print(mike) #ще принтира     Mike - has hobbies: ['Football', 'Fitness']

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_details(self):
#         return f'Name {self.name}, Age: {self.age}'
#
#
# class Student(Person): # наследява Person
#     def __init__(self, name, age, rollno):
#         super().__init__(name, age)
#         self.rollno = rollno
#
#     def get_details2(self):
#         return f'Name {self.name}, Age: {self.age}, Roll No: {self.rollno}'
#
#
# person = Person('John', 30)
# student = Student('Mike', 20, '123')
#
# print(person.get_details()) # Name John, Age: 30
# # print(person.get_details2()) # ще даде грешка защото няма сложена достатъчно информация в обекта (липсва Roll No)
#
# print(student.get_details2()) # Name Mike, Age: 20, Roll No: 123
# print(student.get_details()) # Name Mike, Age: 20

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} makes a sound')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f'{self.name} barks')


dog = Dog('Balkan', 'Labrador')
dog.speak()

# ще принтира
# Balkan makes a sound
# Balkan barks

