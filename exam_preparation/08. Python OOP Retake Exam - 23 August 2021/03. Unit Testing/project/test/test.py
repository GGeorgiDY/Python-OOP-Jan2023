from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):

    def setUp(self):
        self.test1 = Library('Library1')

    def test_initialization(self):
        self.assertEqual('Library1', self.test1.name)
        self.assertEqual({}, self.test1.books_by_authors)
        self.assertEqual({}, self.test1.readers)

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.test1.name = ''
        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book(self):
        self.test1.books_by_authors = {'Avtor': ['Zaglavie']}
        self.test1.add_book('Avtor', 'Zaglavie')
        self.assertEqual(self.test1.books_by_authors, {'Avtor': ['Zaglavie']})

    def test_add_book2(self):
        self.test1.books_by_authors = {'Avtor': ['Zaglavie']}
        self.test1.add_book('Avtor', 'Zaglavie2')
        self.assertEqual(self.test1.books_by_authors, {'Avtor': ['Zaglavie', 'Zaglavie2']})

    def test_add_book3(self):
        self.test1.books_by_authors = {'Avtor': ['Zaglavie']}
        self.test1.add_book('Avtor2', 'Zaglavie2')
        self.assertEqual(self.test1.books_by_authors, {'Avtor': ['Zaglavie'], 'Avtor2': ['Zaglavie2']})

    def test_add_reader(self):
        self.test1.readers = {'klient1': []}
        self.test1.add_reader('klient2')
        self.assertEqual(self.test1.readers, {'klient1': [], 'klient2': []})

    def test_add_reader_already_exist(self):
        self.test1.readers = {'klient1': []}
        result = self.test1.add_reader('klient1')
        self.assertEqual(result, "klient1 is already registered in the Library1 library.")

    def test_rent_book_reader_name_not_registered(self):
        self.test1.readers = {'klient1': []}
        result = self.test1.rent_book('klient2', 'Avtor2', 'Zaglavie2')
        self.assertEqual(result, "klient2 is not registered in the Library1 Library.")

    def test_rent_book_reader_author_name_has_no_books(self):
        self.test1.readers = {'klient2': []}
        self.test1.books_by_authors = {'Avtor': ['Zaglavie2']}
        result = self.test1.rent_book('klient2', 'Avtor2', 'Zaglavie2')
        self.assertEqual(result, "Library1 Library does not have any Avtor2's books.")

    def test_rent_book_reader_author_name_has_no_this_books(self):
        self.test1.readers = {'klient2': []}
        self.test1.books_by_authors = {'Avtor2': ['Zaglavie2']}
        result = self.test1.rent_book('klient2', 'Avtor2', 'Zaglavie')
        self.assertEqual(result, """Library1 Library does not have Avtor2's "Zaglavie".""")

    def test_rent_book(self):
        self.test1.readers = {'klient2': []}
        self.test1.books_by_authors = {'Avtor2': ['Zaglavie2']}
        result = self.test1.rent_book('klient2', 'Avtor2', 'Zaglavie2')
        self.assertEqual(self.test1.readers, {'klient2': [{'Avtor2': 'Zaglavie2'}]})
        self.assertEqual(self.test1.books_by_authors, {'Avtor2': []})


if __name__ == "__main__":
    main()