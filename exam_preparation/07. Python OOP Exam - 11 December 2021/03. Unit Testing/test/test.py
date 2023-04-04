from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):

    def setUp(self):
        self.test1 = Team('Rambo')

    def test_initialization(self):
        self.assertEqual('Rambo', self.test1.name)
        self.assertEqual({}, self.test1.members)

    def test_initialization2(self):
        self.test1.members = {'Georgi': 28}
        self.assertEqual({'Georgi': 28}, self.test1.members)

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.test1.name = 'Georgi1'
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_name2(self):
        with self.assertRaises(ValueError) as ve:
            self.test1.name = 'Georgi@'
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member_already_exist(self):
        self.test1.members = {'Georgi': 28}
        self.test1.add_member(Georgi=30)
        self.assertEqual(self.test1.members, {'Georgi': 28})

    def test_add_member(self):
        result = self.test1.add_member(Georgi=30, Ivan=31)
        self.assertEqual(self.test1.members, {'Georgi': 30, "Ivan": 31})
        self.assertEqual(result, "Successfully added: Georgi, Ivan")

    # def test_add_member2(self):
    #     # self.test1.members = {'Georgi', 28}
    #     result = self.test1.add_member(Georgi=30, Ivan=31)
    #     self.assertEqual(self.test1.members, {'Georgi': 30, "Ivan": 31})
    #     self.assertEqual(result, "Successfully added: Ivan")

    def test_remove_member(self):
        self.test1.members = {'Georgi': 30, "Ivan": 31}
        result = self.test1.remove_member("Ivan")
        self.assertEqual(self.test1.members, {'Georgi': 30})
        self.assertEqual(result, "Member Ivan removed")

    def test_remove_member2(self):
        self.test1.members = {'Georgi': 30}
        result = self.test1.remove_member("Ivan")
        self.assertEqual(self.test1.members, {'Georgi': 30})
        self.assertEqual(result, "Member with name Ivan does not exist")

    def test_gt(self):
        self.test1.members = {'Georgi': 30, "Ivan": 31}
        self.test2 = Team('Roki')
        self.test2.members = {'Joro': 30}
        result = self.test1.__gt__(self.test2)
        self.assertEqual(result, True)

    def test_gt2(self):
        self.test1.members = {'Joro': 30}
        self.test2 = Team('Roki')
        self.test2.members = {'Georgi': 30, "Ivan": 31}
        result = self.test1.__gt__(self.test2)
        self.assertEqual(result, False)

    def test_add(self):
        self.test1.members = {'Georgi': 30}
        self.test2 = Team('Roki')
        self.test2.members = {'Joro': 30}
        result = self.test1.__add__(self.test2)
        self.assertEqual(result.name, 'RamboRoki')
        self.assertEqual(result.members, {'Georgi': 30, 'Joro': 30})

    def test_str(self):
        self.test1.members = {'Georgi': 30, "Ivan": 31, 'Joro': 30}
        result = self.test1.__str__()
        result2 = "Team name: Rambo" + "\n"
        result2 += "Member: Ivan - 31-years old" + "\n"
        result2 += "Member: Georgi - 30-years old" + "\n"
        result2 += "Member: Joro - 30-years old"
        self.assertEqual(result, result2)


if __name__ == "__main__":
    main()