from typing import List

from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_TYPES_OF_ASTRONAUTS = {"Biologist": Biologist,
                                 "Geodesist": Geodesist,
                                 "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_mission_count = 0
        self.not_successful_mission_count = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                return f"{name} is already added."

        if astronaut_type not in self.VALID_TYPES_OF_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")

        new_astronaut = self.VALID_TYPES_OF_ASTRONAUTS[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for p in self.planet_repository.planets:
            if p.name == name:
                return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items.split(', '))
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut_exist = False
        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                astronaut_exist = True
        if not astronaut_exist:
            raise Exception(f"Astronaut {name} doesn't exist!")

        astronaut = next(filter(lambda x: x.name == name, self.astronaut_repository.astronauts))
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet_exist = False
        for p in self.planet_repository.planets:
            if p.name == planet_name:
                planet_exist = True
        if not planet_exist:
            raise Exception("Invalid planet name!")

        astronauts_dict = {}
        for a in self.astronaut_repository.astronauts:
            if a.oxygen > 30:
                astronauts_dict[a.name] = a.oxygen

        if len(astronauts_dict) < 1:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts_dict = sorted(astronauts_dict.items(), key=lambda x: -x[1])
        if len(sorted_astronauts_dict) > 5:
            sorted_astronauts_dict = sorted_astronauts_dict[:5]
        sorted_astronauts_dict = dict(sorted_astronauts_dict)

        planet = next(filter(lambda x: x.name == planet_name, self.planet_repository.planets))

        for a, o in sorted_astronauts_dict.items():
            astronaut = next(filter(lambda x: x.name == a, self.astronaut_repository.astronauts))
            while astronaut.oxygen > 0:
                if len(planet.items) > 0:
                    astronaut.backpack.append(planet.items.pop())
                    astronaut.breathe()
                else:
                    break

        if len(planet.items) == 0:
            self.successful_mission_count += 1
            return f"Planet: {planet_name} was explored. {len(sorted_astronauts_dict)} astronauts participated in collecting items."
        self.not_successful_mission_count += 1
        return f"Mission is not completed."

    def report(self):
        output = [f"{self.successful_mission_count} successful missions!",
                  f"{self.not_successful_mission_count} missions were not completed!",
                  "Astronauts' info:"]

        for x in self.astronaut_repository.astronauts:
            output.append(f'Name: {x.name}')
            output.append(f"Oxygen: {x.oxygen}")
            output.append(f"Backpack items: " + str(', '.join(x.backpack) if x.backpack else "none"))

        return "\n".join(output)


