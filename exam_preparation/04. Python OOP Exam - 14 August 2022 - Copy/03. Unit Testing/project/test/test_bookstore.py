from project.bookstore import Bookstore
from unittest import TestCase, main


class BookStoreTests(TestCase):

    def setUp(self):
        self.store1 = Bookstore(1000)

    def test_initialization(self):
        self.assertEqual(1000, self.store1.books_limit)
        self.assertEqual({}, self.store1.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store1.total_sold_books)

    def test_books_limit_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.store1 = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_books_limit_successfully(self):
        self.store1 = Bookstore(1)
        self.assertEqual(1, self.store1.books_limit)

    def test_book_counter(self):
        self.store1.availability_in_store_by_book_titles = {'ImeNaKniga1': 10, 'ImeNaKniga2': 10}
        result = self.store1.__len__()
        self.assertEqual(result, 20)

    def test_receive_book_not_enough_space_ex(self):
        self.store1.availability_in_store_by_book_titles = {'ImeNaKniga1': 999}
        with self.assertRaises(Exception) as ex:
            self.store1.receive_book('ImeNaKniga1', 10)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_put_in_dict(self):
        self.store1.receive_book('ImeNaKniga1', 10)
        self.assertEqual(self.store1.availability_in_store_by_book_titles, {'ImeNaKniga1': 10})

    def test_receive_book_print_result(self):
        self.store1.availability_in_store_by_book_titles = {'ImeNaKniga1': 10, 'ImeNaKniga2': 10}
        result = self.store1.receive_book('ImeNaKniga1', 10)
        self.assertEqual(result, "20 copies of ImeNaKniga1 are available in the bookstore.")

    def test_sell_book_not_available_book_ex(self):
        with self.assertRaises(Exception) as ex:
            self.store1.sell_book('ImeNaKniga1', 1)
        self.assertEqual(str(ex.exception), "Book ImeNaKniga1 doesn't exist!")

    def test_sell_book_not_available_copies_of_the_book_ex(self):
        self.store1.availability_in_store_by_book_titles = {'ImeNaKniga1': 1}
        with self.assertRaises(Exception) as ex:
            self.store1.sell_book('ImeNaKniga1', 10)
        self.assertEqual(str(ex.exception), "ImeNaKniga1 has not enough copies to sell. Left: 1")

    def test_sell_book_successfully(self):
        self.store1.availability_in_store_by_book_titles = {'ImeNaKniga1': 10}
        self.store1.sell_book('ImeNaKniga1', 1)
        self.assertEqual(self.store1.availability_in_store_by_book_titles, {'ImeNaKniga1': 9})

    def test_sell_book_successfully_print_result(self):
        self.store1.availability_in_store_by_book_titles = {'ImeNaKniga1': 10}
        result = self.store1.sell_book('ImeNaKniga1', 2)
        self.assertEqual(result, "Sold 2 copies of ImeNaKniga1")

    def test_print_result(self):
        self.store1.availability_in_store_by_book_titles = {'ImeNaKniga1': 10, 'ImeNaKniga2': 10}
        self.store1.sell_book('ImeNaKniga1', 2)
        result = self.store1.__str__()
        self.assertEqual(result,
                         "Total sold books: 2" + "\n"
                         "Current availability: 18" + "\n"
                         " - ImeNaKniga1: 8 copies" + "\n"
                         " - ImeNaKniga2: 10 copies"
                         )


if __name__ == "__main__":
    main()
