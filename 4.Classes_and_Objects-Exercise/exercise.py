# class Car:
#     def __init__(self, manufacturer, model):
#         self.manufacturer = manufacturer
#         self.model = model
#
#     def __repr__(self):
#         return f"This is a {self.manufacturer} {self.model}"
#
#
# nissan = Car("Nissan", "GT-R")
# print(nissan)

# ако нямеме нито __str__ нито __repr__ -> <__main__.Car object at 0x00000250C88260E0>
# ако имаме __str__ -> This is a Nissan GT-R
# ако имаме __repr__ -> This is a Nissan GT-R

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Vet:
#     animals = []
#     space = 5
#
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def register_animal(self, animal_name):
#         if len(Vet.animals) < Vet.space:
#             Vet.animals.append(animal_name)
#             self.animals.append(animal_name)
#             return f"{animal_name} registered in the clinic"
#         return "Not enough space"
#
#     def unregister_animal(self, animal_name):
#         if animal_name in self.animals:
#             Vet.animals.remove(animal_name)
#             self.animals.remove(animal_name)
#             return f"{animal_name} unregistered successfully"
#         return f"{animal_name} not in the clinic"
#
#     def info(self):
#         return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"
#
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
#
#     def next_second(self):
#         if self.seconds + 1 > Time.max_seconds:
#             if self.minutes + 1 > Time.max_minutes:
#                 if self.hours + 1 > Time.max_hours:
#                     self.hours = 0
#                 else:
#                     self.hours += 1
#                 self.minutes = 0
#             else:
#                 self.minutes += 1
#             self.seconds = 0
#         else:
#             self.seconds += 1
#
#         return self.get_time()
#
#
# time = Time(9, 30, 59)
# print(time.next_second())
#
# time = Time(10, 59, 59)
# print(time.next_second())
#
# time = Time(23, 59, 59)
# print(time.next_second())

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         return "Amount exceeded balance"
#
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"
#
#
# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class PizzaDelivery:
#     def __init__(self, name, price, ingredients=dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient:str, quantity:int, price_per_quantity:float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient in self.ingredients:
#             self.ingredients[ingredient] += quantity
#             self.price += quantity * price_per_quantity
#         else:
#             self.ingredients[ingredient] = quantity
#             self.price += quantity * price_per_quantity
#
#     def remove_ingredient(self, ingredient:str, quantity:int, price_per_quantity:float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#         else:
#             if quantity > self.ingredients[ingredient]:
#                 return f"Please check again the desired quantity of {ingredient}!"
#             else:
#                 self.ingredients[ingredient] -= quantity
#                 self.price -= quantity * price_per_quantity
#
#     def make_order(self):
#         self.ordered = True
#         ingredients = [f"{i}: {q}"for i, q in self.ingredients.items()]
#         return f"You've ordered pizza {self.name} prepared with {', '.join(ingredients)} and the price will be {self.price}lv."
#
#
# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

