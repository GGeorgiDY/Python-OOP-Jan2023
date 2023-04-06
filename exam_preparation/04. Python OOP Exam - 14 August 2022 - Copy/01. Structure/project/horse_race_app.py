from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES:
            new_horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey_exist = False
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                jockey_exist = True
        if not jockey_exist:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        available_horse = False
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                available_horse = True
        if not available_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
        if available_horse:
            if jockey.horse is not None:
                return f"Jockey {jockey_name} already has a horse."

        horses_of_that_type = [x for x in self.horses if x.__class__.__name__ == horse_type and not x.is_taken]
        horse_to_add = horses_of_that_type.pop()
        jockey.horse = horse_to_add
        horse_to_add.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse_to_add.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race_exist = False
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                race_exist = True
        if not race_exist:
            raise Exception(f"Race {race_type} could not be found!")

        jockey_exist = False
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                jockey_exist = True
        if not jockey_exist:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        horse_race = next(filter(lambda x: x.race_type == race_type, self.horse_races))

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race_exist = False
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                race_exist = True
        if not race_exist:
            raise Exception(f"Race {race_type} could not be found!")

        horse_race = next(filter(lambda x: x.race_type == race_type, self.horse_races))

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner_jockey_name = ""
        winner_horse_name = ""
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner_jockey_name = jockey.name
                winner_horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner_jockey_name}! Winner's horse: {winner_horse_name}."

