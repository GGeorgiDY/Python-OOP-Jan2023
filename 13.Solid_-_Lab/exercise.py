# пример за single responsibility

# class Calculator:
#     def add(self, x, y):
#         return x + y
#
#     def subtract(self, x, y):
#         return x - y
#
#     def multiply(self, x, y):
#         return x * y
#
#     def divide(self, x, y):
#         if y == 0:
#             raise ValueError("Cannot divide bby zero")
#         return x / y
#
#
# calc = Calculator()
# print(calc.multiply(5, 5))
# print(calc.divide(5, 5))
# print(calc.add(5, 5))

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# пример за single responsibility

# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password
#
#     def get_username(self):
#         return self.username
#
#     def get_email(self):
#         return self.email
#
#     def authenticate(self, password):
#         if password == self.password:
#             return True
#         else:
#             return False
#
#
# gosho = User("Gosho", "gosho@gmail.com", "TestPassword")
# print(gosho.authenticate("SuperGosho"))

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# пример за Open/Closed

# from abc import ABC, abstractmethod
#
#
# class PaymentMethod(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass
#
#
# class CreditCardPayment(PaymentMethod):
#     def process_payment(self, amount):
#         print(amount)
#
#
# class PayPallPayment(PaymentMethod):
#     def process_payment(self, amount):
#         print(amount)
#
#
# class BankTransferPayment(PaymentMethod):
#     def process_payment(self, amount):
#         print(amount)
#
#
# class PaymentProcessor:
#     def __init__(self, payment_method):
#         self.payment_method = payment_method
#
#     def process_payment(self, amount):
#         self.payment_method.process_payment(amount)
#
# # какво направихме до момента?
# # имаме някакъв клас "PaymentProcessor", който обработва плащания за някакви различни методи на плащане
# # може да си дефинираме абстрактен клас, който да се казва "PaymentMethod" със метод "process_payment"
# # класа "PaymentProcessor" зависи от абстрактния клас, а не от някакви конкретни имплементации
# # това ни позволява да добавяме нови методи за плащане без да се налага да променяме класа "PaymentProcessor"
#
# # класа "PaymentProcessor" приема обект "payment_method", като зависимост към своя конструктор. Това ни позволява да
# # предаваме всеки обект, който имплементира интерфейса "payment_method" без да се налага да променяме класа "PaymentProcessor"
#
#
# bank_transfer_payment = BankTransferPayment()
# processor = PaymentProcessor(bank_transfer_payment)
# processor.process_payment(100) # връща 100

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# пример за Liskov Substitution

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#
# # В случая класът Square наследява отрибутите width и height, които са на Rectangle. Тъй като Square е някакъв подтип клас
# # на Rectangle трябва да можем да използваме Square навсякъде където очакваме Rectangle обект
# # Тази заменямост може да я ползваме в този пример
#
# def print_area(rectangle):
#     print(rectangle.area())
#
#
# r = Rectangle(2, 3)
# s = Square(2)
# print_area(r) # 6
# print_area(s) # 4

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\

# Interface Segregation

# from abc import ABC, abstractmethod
#
# class Printable(ABC):
#     @abstractmethod
#     def print(self, document):
#         pass
#
# class Scannable(ABC):
#     @abstractmethod
#     def scan(self, document):
#         pass
#
# class Faxable(ABC):
#     @abstractmethod
#     def fax(self, document):
#         pass
#
#
# class MultiFunctionPrinter(Printable, Scannable, Faxable):
#     def print(self, document):
#         pass
#
#     def scan(self, scan):
#         pass
#
#     def fax(self, document):
#         pass
#
#
# class SimplePrinter(Printable):
#     def print(self, document):
#         pass

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Dependency Inversion

# class Database:
#     def save(self, data):
#         pass
#
# class Application:
#     def __init__(self, database):
#         self.database = database
#
#     def run(self):
#         data = self.fetch_data()
#         self.database.save(data)
#
#     def fetch_data(self):
#         pass

# горния код е грешен защото клас Application зависи от клас Database, който е low level модул
# за да го оправим правим следното

from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass


class Database(DatabaseInterface):
    def save(self, data):
        pass


class Application:
    def __init__(self, database):
        self.database = database

    def run(self):
        data = self.fetch_data()
        self.database.save(data)

    def fetch_data(self):
        pass


# какво се получава сега:
# класа Database вече имплементира абстрактния базов метод DatabaseInterface, който служи като абстракция от която зависи
# класа Application, вместо от клас Database.
# Това позволява доста повече гъвкъвост на кода, тъй като може да си създадеме алтернативни реализации на DatabaseInterface
# без да се налага да променяме класа Application