# class Shape:
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * 3.14 * 2
#
#
# # създаваме списък от обекти, който включва правоъгълник и кръг.
# # когато извикаме метода area за всеки обект Python използва имплементацията дефинирана в подкласа за да си изчисли
# # area-та за дадената фигура.
# # това е някакъв пример за полиморфизъм в пайтън, защото може да третираме обекти от различни типове сякаш са
# # от един и същ тип.
#
# shapes = [Rectangle(3, 4), Circle(5)]
# for shape in shapes:
#     print(shape.area())


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# как става без полиморфизъм

# class Shape:
#     def area(self):
#         pass
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * 3.14 * 2
#
#
# def area(shape):
#     if isinstance(shape, Rectangle):
#         return shape.width * shape.height
#     elif isinstance(shape, Circle):
#         return shape.radius * 3.14 * 2
#     else:
#         raise TypeError('Invalid shape type')
#
#
# rectangle = Rectangle(3, 4)
# circle = Circle(5)
# print(area(rectangle))
# print(area(circle))

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class MyList:
#     def __init__(self, items):
#         self.items = items
#
#     def __len__(self):
#         return len(self.items)
#
#
# my_list = MyList([1, 2, 3, 4, 5])
# print(len(my_list))

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2
# print(p1)
# print(p2)
# print(p3)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# p1 = Vector(1, 2)
# p2 = Vector(3, 4)
# p3 = p1 - p2
# print(p1)
# print(p2)
# print(p3)
# print(p3.x)
# print(p3.y)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __mul__(self, other):
#         return Vector(self.x * other.x, self.y * other.y)
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# p1 = Vector(1, 2)
# p2 = Vector(3, 4)
# p3 = p1 * p2
# print(p1)
# print(p2)
# print(p3)
# print(p3.x)
# print(p3.y)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __floordiv__(self, other):
#         return Vector(self.x // other.x, self.y // other.y)
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# p1 = Vector(1, 2)
# p2 = Vector(3, 4)
# p3 = p1 // p2
# print(p1)
# print(p2)
# print(p3)
# print(p3.x)
# print(p3.y)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#
# person1 = Person('Gosho', 20)
#
# person2 = Person('Ivan', 19)
# print(person1 < person2) # щом види "<" автоматично ще го върже към def __lt__

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# duck typing

# тук двата класа споделят един сходен интерфейс - метода get_area
# въпреки това двата класа не са от един тип
# duck typing ни дава гъвкавост, тъй като кода може да работи с повече типове обекти, стига те да имат необходимите
# методи и поведение, които да са сходни. Позволява на обектите да взаимодействат помежду си възоснова на тяхно поведение,
# а не на изричен тип или клас. Тук си взаимодействат посредством някакво общо поведение - метода get_area.

# duck typing-a опростява кода, тъй като позволява на програмиста да пише по общ като смисъл и контекст код, който работи
# с различни типове обекти, вместо да се налага да пишат специфичен код за всеки тип.


# def print_area(obj):
#     print(obj.get_area())
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return 3.14 * self.radius ** 2
#
#
# rect = Rectangle(10, 5)
# circle = Circle(7)
# print_area(rect)
# print_area(circle)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# абстракция

# from abc import ABC, abstractmethod
# # abc е едно модулче което използваме за да си дефинираме абстрактни класове
#
# # дефинираме абстрактен клас 'Shape', който има абстрактен метод 'area'. Всеки клас, който наследява този Shape трябва
# # да имплементира метода area или в противен случай той също ще бъде абстрактен клас
# class Shape(ABC): # казваме че той е някакъв абстрактен клас
#     @abstractmethod
#     def area(self):
#         pass
#
# # След това дефинираме два подкласа, които наследяват 'Shape'. И двата подкласа прилагат метода за area с някаква собствена
# # логика. Ако се опитаме да създадеме инстанция на 'Shape' директно, ще върне грешка.
# class Rectangle(Shape):
#     def __init__(self, width, lenght):
#         self.width = width
#         self.lenght = lenght
#
#     def area(self):
#         return self.width * self.lenght
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# my_rectangle = Rectangle(5, 3)
# my_circle = Circle(4)
# print('Area of rectangle:', my_rectangle.area())
# print('Area of circle:', my_circle.area())
#
# # my_shape = Shape()              # ще върне грешка

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#     def perimeter(self):
#         return 3.14 * self.radius * 2
#
#
# my_rectangle = Rectangle(5, 3)
# my_circle = Circle(4)
# print('Area of rectangle:', my_rectangle.area())
# print('Area of circle:', my_circle.area())
# print('Perimeter of rectangle', my_rectangle.perimeter()) # ще даде грешка. Това е така защото, конструкцията на
# # абстрактния клас налага на подкласовете да имат имплементация на всички сетнати абстрактни методи.
#
# # За това дефинирахме два метода perimeter - по един за всеки клас, и вече сработи.
#
# # my_shape = Shape()              # ще върне грешка

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

