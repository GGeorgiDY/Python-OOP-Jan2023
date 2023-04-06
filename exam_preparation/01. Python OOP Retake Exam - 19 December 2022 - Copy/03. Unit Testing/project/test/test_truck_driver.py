from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):

    def setUp(self):
        self.test1 = TruckDriver('Ime1', 1.00)

    def test_initialization(self):
        self.assertEqual(self.test1.name, 'Ime1')
        self.assertEqual(self.test1.money_per_mile, 1)
        self.assertEqual(self.test1.available_cargos, {})
        self.assertEqual(self.test1.earned_money, 0)
        self.assertEqual(self.test1.miles, 0)

    def test_earned_money(self):
        with self.assertRaises(ValueError) as ve:
            self.test1.earned_money = -1
        self.assertEqual("Ime1 went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_ex(self):
        self.test1.available_cargos = {'Sofia': 100, 'Shumen': 300}
        with self.assertRaises(Exception) as ex:
            self.test1.add_cargo_offer('Sofia', 300)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer(self):
        self.test1.available_cargos = {'Sofia': 100, 'Shumen': 300}
        result = self.test1.add_cargo_offer('Varna', 400)
        self.assertEqual(self.test1.available_cargos, {'Sofia': 100, 'Shumen': 300, 'Varna': 400})
        self.assertEqual(result, "Cargo for 400 to Varna was added as an offer.")

    def test_drive_best_cargo_offer_ve(self):
        self.test1.available_cargos = {}
        result = self.test1.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer(self):
        self.test1.available_cargos = {'Sofia': 100, 'Shumen': 300, 'Varna': 10000}
        self.test1.money_per_mile = 2
        result = self.test1.drive_best_cargo_offer()
        self.assertEqual(self.test1.earned_money, 8250)
        self.assertEqual(self.test1.miles, 10000)
        self.assertEqual("Ime1 is driving 10000 to Varna.", result)

    def test_repr(self):
        result = self.test1.__repr__()
        self.assertEqual(result, "Ime1 has 0 miles behind his back.")


if __name__ == "__main__":
    main()