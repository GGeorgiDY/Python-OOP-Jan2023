# class CreditCard:
#     def __init__(self, number: str, name: str, cvv: str, expr_date: str, pin: str):
#         self.number = number
#         self.name = name
#         self.cvv = cvv
#         self.expr_date = expr_date
#         self.__pin = pin #слагайки тези 2 долни черти ние казваме на Python че този атрибут е прайвет и това означава,
#         # че ние няма да можем да го извикваме променяме и т.н. извън рамките на класа
#
#
# mastercard = CreditCard("1231231231231231", "Test name", "123", "2023-11", "0000")
# print(mastercard._CreditCard__pin) # само така може да достъпваме протектнат атрибут
# mastercard._CreditCard__pin = "1234" #само така може да го променяме
# print(mastercard._CreditCard__pin)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class CreditCard:
#     def __init__(self, number: str, name: str, cvv: str, expr_date: str, pin: str):
#         self.number = number
#         self.name = name
#         self.cvv = cvv
#         self.expr_date = expr_date
#         self.__pin = pin #private
#
#     def get_pin(self): #работи защото сме в класа
#         return self.__pin
#
#
# mastercard = CreditCard("1231231231231231", "Test name", "123", "2023-11", "0000")
# print(mastercard.get_pin()) # дава 0000

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# protected метода

# class CreditCard:
#     def __init__(self, number: str, name: str, cvv: str, expr_date: str, pin: str):
#         self.number = number # public
#         self.name = name # public
#         self.cvv = cvv # public
#         self.expr_date = expr_date # public
#         self._pin = pin # protected -> дава възможност да се използва и от класовете, които наследяват главния клас.
#         # Все пак не може да се променя и достъпва от вън както при private
#
#
# class ChildCreditCard(CreditCard):
#     def __init__(self, number: str, name: str, cvv: str, expr_date: str, pin: str):
#         super().__init__(number, name, cvv, expr_date, pin)
#         self._pin = pin

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# getter & setter

# class Car:
#     def __init__(self):
#         self.__max_speed = 200
#
#     def get_max_speed(self): # getter -> създаваме си метод който да връща въпросната ст-ст
#         return self.__max_speed
#
#     def set_max_speed(self, max_speed): # setter -> променяме private атрибута
#         if max_speed < 0: # setter-a се използва най-често с такива валидации
#             raise ValueError("max_speed must be positive")
#
#         self.__max_speed = max_speed
#
#
# nissan = Car()
# print(nissan.get_max_speed()) # връща 200
# nissan.set_max_speed(320)
# print(nissan.get_max_speed()) # връща 320
# nissan.set_max_speed(-1)
# print(nissan.get_max_speed()) # връща ValueError: max_speed must be positive

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Person:
#     def __init__(self, age=0):
#         self.age = age # преди да се случи този ред, Python проверява дали имаме някакви setter-и и ги изпълнява първо тях
#
#     @property #това се нарича декоратор. Това е функция която прави нещо вместо нас
#     def age(self):
#         return self.__age
#
#     @age.setter # щом има декоратор, преди Python да е инициализирал някаква ст-ст, той минава от тук за да я провери
#     def age(self, age):
#         if age < 18:
#             self.__age = 18 # ако ги нямаше тези две долни черти щяхме да влезем в безкраен цикъл
#         else:
#             self.__age = age # ако ги нямаше тези две долни черти щяхме да влезем в безкраен цикъл
#
#
# person = Person(10)
# print(person.age)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Employee:
    name = 'Diyan'
    salary = '25000'

    def show(self):
        print(self.name)
        print(self.salary)


employee = Employee()
print(getattr(employee, 'name'))   # Diyan
print(hasattr(employee, 'name'))   # True
setattr(employee, 'height', 152)
print(getattr(employee, 'height')) # 152
delattr(Employee, 'salary')

