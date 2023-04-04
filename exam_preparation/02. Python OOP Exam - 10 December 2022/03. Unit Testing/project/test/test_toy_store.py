from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTests(TestCase):

    def setUp(self):
        self.toy_shelf = ToyStore()

    def test_initialization(self):
        self.assertEqual(
            self.toy_shelf.toy_shelf,
            {"A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None}
        )

    def test_add_toy_shelf_does_not_exist_ex(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.add_toy("Z", 'bear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_toy_already_in_shelf_ex(self):
        self.toy_shelf.toy_shelf = {"A": 'bear'}
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.add_toy("A", 'bear')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_shelf_already_taken_ex(self):
        self.toy_shelf.toy_shelf = {"A": 'bear'}
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.add_toy("A", 'cat')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        self.toy_shelf.add_toy("A", 'bear')
        self.assertEqual(
            self.toy_shelf.toy_shelf,
            {"A": 'bear',
             "B": None,
             "C": None,
             "D": None,
             "E": None,
             "F": None,
             "G": None}
        )

    def test_add_toy_successfully_return(self):
        result = self.toy_shelf.add_toy("A", 'bear')
        self.assertEqual(result, "Toy:bear placed successfully!")

    def test_remove_toy_shelf_does_not_exist_ex(self):
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.remove_toy("Z", 'bear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_toy_in_shelf_does_not_exist_ex(self):
        self.toy_shelf.add_toy("A", 'bear')
        with self.assertRaises(Exception) as ex:
            self.toy_shelf.remove_toy("A", 'cat')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.toy_shelf.add_toy("A", 'bear')
        self.toy_shelf.remove_toy("A", 'bear')
        self.assertEqual(
            self.toy_shelf.toy_shelf,
            {"A": None,
             "B": None,
             "C": None,
             "D": None,
             "E": None,
             "F": None,
             "G": None}
        )

    def test_remove_toy_successfully_return(self):
        self.toy_shelf.add_toy("A", 'bear')
        result = self.toy_shelf.remove_toy("A", 'bear')
        self.assertEqual(result, "Remove toy:bear successfully!")


if __name__ == "__main__":
    main()