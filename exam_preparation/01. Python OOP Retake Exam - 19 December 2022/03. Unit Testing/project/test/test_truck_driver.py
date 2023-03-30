from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):

    def setUp(self):
        self.truck_driver = TruckDriver('Gosho', 1.00)

    def test_initialization(self):
        self.assertEqual('Gosho', self.truck_driver.name)
        self.assertEqual(1.00, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_error(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1
        self.assertEqual("Gosho went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_exception(self):
        self.truck_driver.available_cargos = {'Sofia': 100}
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 10)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_successfully(self):
        result = self.truck_driver.add_cargo_offer("Sofia", 100)
        self.assertEqual(self.truck_driver.available_cargos, {'Sofia': 100})
        self.assertEqual(result, "Cargo for 100 to Sofia was added as an offer.")

    def test_drive_best_cargo_offer_ve(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer(self):
        self.truck_driver.available_cargos = {'Sofia': 100, 'Shumen': 50}
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(self.truck_driver.earned_money, 100)
        self.assertEqual(self.truck_driver.miles, 100)
        self.assertEqual(result, "Gosho is driving 100 to Sofia.")

    def test_bankrupt(self):
        self.truck_driver.money_per_mile = 0.1
        self.truck_driver.add_cargo_offer('Paris', 2000)

        with self.assertRaises(ValueError) as ve:
            self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("Gosho went bankrupt.", str(ve.exception))

    def test_eat(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.eat(250)
        self.assertEqual(self.truck_driver.earned_money, 80)

    def test_sleep(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.sleep(1000)
        self.assertEqual(self.truck_driver.earned_money, 55)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.pump_gas(1500)
        self.assertEqual(self.truck_driver.earned_money, 500)

    def test_repair_truck(self):
        self.truck_driver.earned_money = 10000
        self.truck_driver.repair_truck(10000)
        self.assertEqual(self.truck_driver.earned_money, 2500)

    def test_repr(self):
        result = self.truck_driver.__repr__()
        self.assertEqual(result, "Gosho has 0 miles behind his back.")


if __name__ == "__main__":
    main()