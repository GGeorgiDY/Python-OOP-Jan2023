# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         return f'{self.name} is {self.age} years old.'
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def get_id(self):
#         return self.student_id
#
# p = Person("John", 25)
# print(p.get_info())
#
# s = Student("Leo", 20, 10035464)
# print(s.get_info())
#
# print(s.get_id())

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class A:
#     def f_a(self):
#         return f'f from A'
#
# class B:
#     def f_b(self):
#         return f'f from B'
#
# class C(A, B):
#     pass
#
# c = C()
# print(c.f_a())
# print(c.f_b())

# връща
# f from A
# f from B

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class A:
#     def __init__(self, a):
#         self.a = a
#     def f_a(self):
#         return f'f from A ({self.a})'
#
# class B:
#     def __init__(self, b):
#         self.b = b
#     def f_b(self):
#         return f'f from B ({self.b})'
#
# class C(A, B):
#     def __init__(self, a, b):
#         A.__init__(self, a)
#         B.__init__(self, b)
#
# c = C('a', 'b')
# print(c.f_a())
# print(c.f_b())

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class A:
#     def f_a(self):
#         return f'f from A'
#
# class B(A):
#     def f_b(self):
#         return f'f from B'
#
# class C(B):
#     def f_c(self):
#         return f'f from C'
#
# c = C()
# print(c.f_a())
# print(c.f_b())
# print(c.f_c())

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class A:
#     def f_a(self):
#         return f'f from A'
#
# class B:
#     def f_b(self):
#         return f'f from B'
#
# class C(A, B):
#     pass
#
#
# c = C()
# print(c.f_a())
# print(c.f_b())
# print(C.mro())
# print(str(c))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class StrMixin:
#     def __str__(self):
#         items = self.__dict__.items()
#         return ';'.join([f'{k} = {v}' for k, v in items])
#
#
# class Animal(StrMixin):
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Vet(StrMixin):
#     def __init__(self, location,  price):
#         self.location = location
#         self.price = price
#
#
# a = Animal('Sharo', 2, 'male')
# v = Vet('Al. Malinov', '1000')
#
# print(str(a))
# print(str(v))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class EqualMixin:
    def __eq__(self, other):
        self_items = self.__dict__
        other_items = other.__dict__

        for k in self_items:
            if k not in other_items or self_items[k] != other_items[k]:
                return False
            return True


class StrMixin:
    def __str__(self):
        items = self.__dict__.items()
        return ';'.join([f'{k} = {v}' for k, v in items])


class Animal(StrMixin, EqualMixin):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Vet(StrMixin):
    def __init__(self, location,  price):
        self.location = location
        self.price = price


a1 = Animal('Sharo', 2, 'male')
a2 = Animal('Sharo', 2, 'male')

print(a1 == a2)

