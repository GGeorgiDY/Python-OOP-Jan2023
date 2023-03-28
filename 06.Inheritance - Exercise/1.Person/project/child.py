from project.person import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age) #извиквайки super() ние проверяваме кой клас наследяваме, отиваме в него
        # и с __init__ отиваме върху __init__ метода на класа който наследяваме
        # с (name, age) казваме кои са инстанциите които искаме да наследим


person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__) # проверяваме дали Child наследява Person, като влизаме в класовете, които
    # наследява с __class__. След това влизаме в __bases__ където взимаме нулевия индекс, защото __class__ ни връща списък
    # със всички класове които наследяваме. В този случай ние взимаме първия клас който наследяваме (който е и единствен).
    # Накрая с __name__ взимаме името на въпросния клас.
