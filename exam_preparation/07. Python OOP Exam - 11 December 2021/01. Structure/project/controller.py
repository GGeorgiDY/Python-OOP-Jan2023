from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for m in self.cars:
            if m.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type == self.VALID_CAR_TYPES[0]:
            new_car = MuscleCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

        if car_type == self.VALID_CAR_TYPES[1]:
            new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for d in self.drivers:
            if d.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for r in self.races:
            if r.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver_exist = False
        for d in self.drivers:
            if d.name == driver_name:
                driver_exist = True
        if not driver_exist:
            raise Exception(f"Driver {driver_name} could not be found!")

        car_exist = False
        for c in self.cars:
            if c.__class__.__name__ == car_type and car_type in self.VALID_CAR_TYPES and not c.is_taken:
                car_exist = True
        if not car_exist:
            raise Exception(f"Car {car_type} could not be found!")

        for c in range(len(self.cars) -1, -1, -1):
            new_car = self.cars[c]
            if new_car.__class__.__name__ == car_type and not new_car.is_taken:
                driver = next(filter(lambda x: x.name == driver_name, self.drivers))
                if driver.car is not None:
                    old_car = driver.car
                    driver.car = new_car
                    old_car.is_taken = False
                    new_car.is_taken = True
                    return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."
                driver.car = new_car
                new_car.is_taken = True
                return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race_exist = False
        for r in self.races:
            if r.name == race_name:
                race_exist = True
        if not race_exist:
            raise Exception(f"Race {race_name} could not be found!")

        driver_exist = False
        for d in self.drivers:
            if d.name == driver_name:
                driver_exist = True
        if not driver_exist:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race = next(filter(lambda x: x.name == race_name, self.races))
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race_exist = False
        for r in self.races:
            if r.name == race_name:
                race_exist = True
        if not race_exist:
            raise Exception(f"Race {race_name} could not be found!")

        race = next(filter(lambda r: r.name == race_name, self.races))
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_cars = {}
        for driver in race.drivers:
            car = driver.car.model
            speed = driver.car.speed_limit
            fastest_cars[car] = speed

        sorted_fastest_cars = sorted(fastest_cars.items(), key=lambda x: -x[1])
        winners = dict(sorted_fastest_cars[:3])

        result = ''
        for driver in self.drivers:
            for car, speed in winners.items():
                if driver.car.model == car:
                    driver.number_of_wins += 1
                    result += f"Driver {driver.name} wins the {race_name} race with a speed of {speed}." + "\n"

        return result[:-1]