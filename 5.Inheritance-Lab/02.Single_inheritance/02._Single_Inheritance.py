from project.animal import Animal
from project.dog import Dog

a = Animal()
d = Dog()

print(d.eat())
print(d.bark())
print(a.eat())
# print(a.bark()) #ще даде грешка, защото класа Animal няма метод bark