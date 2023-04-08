from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):

    def setUp(self):
        self.test1 = Movie('Rambo', 1988, 9.0)

    def test_initialization(self):
        self.assertEqual('Rambo', self.test1.name)
        self.assertEqual(1988, self.test1.year)
        self.assertEqual(9.0, self.test1.rating)
        self.assertEqual([], self.test1.actors)

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.test1 = Movie('', 1988, 9.0)
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year(self):
        with self.assertRaises(ValueError) as ve:
            self.test1 = Movie('Rambo', 1788, 9.0)
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor_already_added(self):
        self.test1.actors = ['Georgi']
        result = self.test1.add_actor('Georgi')
        self.assertEqual(result, "Georgi is already added in the list of actors!")

    def test_add_actor(self):
        self.test1.add_actor('Georgi')
        self.assertEqual(self.test1.actors, ['Georgi'])

    def test_add_actor2(self):
        self.test1.actors = ['Georgi']
        self.test1.add_actor('Ivan')
        self.assertEqual(self.test1.actors, ['Georgi', 'Ivan'])

    def test_rating_better_than_other_rating(self):
        self.test2 = Movie('Rambo2', 1990, 8.0)
        result = self.test1.__gt__(self.test2)
        self.assertEqual(result, '"Rambo" is better than "Rambo2"')

    def test_rating_less_than_other_rating(self):
        self.test2 = Movie('Rambo2', 1990, 9.0)
        result = self.test1.__gt__(self.test2)
        self.assertEqual(result, '"Rambo2" is better than "Rambo"')

    def test_rating_less_than_other_rating2(self):
        self.test2 = Movie('Rambo2', 1990, 9.1)
        result = self.test1.__gt__(self.test2)
        self.assertEqual(result, '"Rambo2" is better than "Rambo"')

    def test_repr(self):
        self.test1.actors = ['Georgi', 'Ivan', 'Pesho']
        result = self.test1.__repr__()
        result2 = "Name: Rambo" + "\n"
        result2 += "Year of Release: 1988" + "\n"
        result2 += "Rating: 9.00" + "\n"
        result2 += "Cast: Georgi, Ivan, Pesho"
        self.assertEqual(result, result2)


if __name__ == "__main__":
    main()