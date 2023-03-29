from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):

    # Arrange - преди всеки от долните 4 теста, този се изпълнява
    # като инциализира пробен self.mammal
    def setUp(self):
        self.mammal = Mammal('Sharo', "Dog", "bark")

    # Assert
    def test_initialization(self):
        self.assertEqual(self.mammal.name, 'Sharo')
        self.assertEqual(self.mammal.type, 'Dog')
        self.assertEqual(self.mammal.sound, 'bark')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Sharo makes bark")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_if_returns_correct_message(self):
        self.assertEqual(self.mammal.info(), "Sharo is of type Dog")


if __name__ == "__main__":
    main()