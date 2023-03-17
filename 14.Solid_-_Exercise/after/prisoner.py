# тук е нарушено правилото за LSP(Liskov Substitution Principle)
# защото имаме функционалност в клас, която не трябва да бъде там
# Prisoner не може да обикаля като свобосния човек Person

# решението на проблема е да си направим един клас FreePerson, който да може да се движи в
# различни посоки, но в същото време да оставим това че Prisoner наследява Person.
# С други думи логиката от person (walk_north и walk_east) ще я изнесем в друг клас FreePerson,
# който да наследява Person

import copy


class Person:
    def __init__(self, position):
        self.position = position # [x, y]


class FreePerson(Person):
    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

