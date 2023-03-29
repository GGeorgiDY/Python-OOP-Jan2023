from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_default_fuel_consumption_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_car_without_enough_fuel(self):
        # it must raise an exception
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_car_with_enough_fuel(self):
        # it must decrease it's fuel
        # като караме два километра, горивото ни намалява
        # с 2*1.25=2.5 литра и става от 20.5 на 18 литра
        self.vehicle.drive(2)
        self.assertEqual(self.vehicle.fuel, 18)

    def test_refuel_car_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_correct(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, 1)

    def test_print_message(self):
        self.assertEqual(
            "The vehicle has 175.5 " +
            "horse power with 20.5 fuel left and 1.25 fuel consumption",
            str(self.vehicle.__str__())
        )


if __name__ == "__main__":
    main()