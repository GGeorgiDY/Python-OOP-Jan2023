from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TennisPlayerTests(TestCase):

    def setUp(self):
        self.test1 = TennisPlayer('TestName1', 28, 10)

    def test_initialization(self):
        self.assertEqual('TestName1', self.test1.name)
        self.assertEqual(28, self.test1.age)
        self.assertEqual(10, self.test1.points)
        self.assertEqual([], self.test1.wins)

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.test2 = TennisPlayer('T1', 28, 10)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age(self):
        with self.assertRaises(ValueError) as ve:
            self.test2 = TennisPlayer('TestName2', 17, 10)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_win_already_added(self):
        self.test1.wins = ['tournament1']
        result = self.test1.add_new_win('tournament1')
        self.assertEqual(result, "tournament1 has been already added to the list of wins!")

    def test_add_new_win(self):
        self.test1.add_new_win('tournament1')
        self.assertEqual(['tournament1'], self.test1.wins)

    def test_lt(self):
        self.test2 = TennisPlayer('TestName2', 28, 15)
        result = self.test1.__lt__(self.test2)
        self.assertEqual(result, 'TestName2 is a top seeded player and he/she is better than TestName1')

    def test_lt2(self):
        self.test2 = TennisPlayer('TestName2', 28, 5)
        result = self.test1.__lt__(self.test2)
        self.assertEqual(result, 'TestName1 is a better player than TestName2')

    def test_str(self):
        self.test1.wins = ['tournament1', 'tournament2']
        result = self.test1.__str__()
        result2 = "Tennis Player: TestName1" + "\n"
        result2 += "Age: 28" + "\n"
        result2 += "Points: 10.0" + "\n"
        result2 += "Tournaments won: tournament1, tournament2"
        self.assertEqual(result, result2)


if __name__ == "__main__":
    main()