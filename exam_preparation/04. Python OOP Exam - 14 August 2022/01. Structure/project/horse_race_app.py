from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


# class HorseRaceApp:
#     def __init__(self):
#         self.horses: List[Horse] = []
#         self.jockeys: List[Jockey] = []
#         self.horse_races: List[HorseRace] = []
#         self.valid_types_of_horses = ["Appaloosa", "Thoroughbred"]
#         self.valid_race_types = ["Winter", "Spring", "Autumn", "Summer"]
#
#     def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
#         for horse in self.horses:
#             if horse.name == horse_name:
#                 raise Exception(f"Horse {horse_name} has been already added!")
#
#         if horse_type == self.valid_types_of_horses[0]:
#             new_horse = Appaloosa(horse_name, horse_speed)
#             self.horses.append(new_horse)
#             return f"{horse_type} horse {horse_name} is added."
#
#         if horse_type == self.valid_types_of_horses[1]:
#             new_horse = Thoroughbred(horse_name, horse_speed)
#             self.horses.append(new_horse)
#             return f"{horse_type} horse {horse_name} is added."
#
#     def add_jockey(self, jockey_name: str, age: int):
#         for jockey in self.jockeys:
#             if jockey.name == jockey_name:
#                 raise Exception(f"Jockey {jockey_name} has been already added!")
#
#         # new_jockey = Jockey(jockey_name, age)
#         self.jockeys.append(Jockey(jockey_name, age))
#         return f"Jockey {jockey_name} is added."
#
#     def create_horse_race(self, race_type: str):
#         for horse_race in self.horse_races:
#             if horse_race.race_type == race_type:
#                 raise Exception(f"Race {race_type} has been already created!")
#
#         new_horse_race = HorseRace(race_type)
#         self.horse_races.append(new_horse_race)
#         return f"Race {race_type} is created."
#
#     def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
#         try:
#             jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
#         except StopIteration:
#             raise Exception(f"Jockey {jockey_name} could not be found!")
#
#         try:
#             horse = list(filter(lambda x: x.__class__.__name__ == horse_type and not x.is_taken, self.horses))[-1]
#         except StopIteration:
#             raise Exception(f"Horse breed {horse_type} could not be found!")
#
#         # if horse.is_taken:
#         #     raise Exception(f"Horse breed {horse_type} could not be found!")
#
#         if jockey.horse != None:
#             return f"Jockey {jockey_name} already has a horse."
#
#         jockey.horse = horse
#         horse.is_taken = True
#
#         horse_name = horse.name
#         return f"Jockey {jockey_name} will ride the horse {horse_name}."
#
#     def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
#         try:
#             horse_race = next(filter(lambda x: x.race_type == race_type, self.horse_races))
#         except StopIteration:
#             raise Exception(f"Race {race_type} could not be found!")
#
#         try:
#             jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
#         except StopIteration:
#             raise Exception(f"Jockey {jockey_name} could not be found!")
#
#         if jockey.horse == None:
#             return f"Jockey {jockey_name} cannot race without a horse!"
#
#         if jockey in horse_race.jockeys:
#             return f"Jockey {jockey_name} has been already added to the {race_type} race."
#
#         horse_race.jockeys.append(jockey)
#         return f"Jockey {jockey_name} added to the {race_type} race."
#
#     def start_horse_race(self, race_type: str):
#         # horse_race_types = [x.race_type for x in self.horse_races]
#         # if race_type not in horse_race_types:
#         #     raise Exception(f"Race {race_type} could not be found!")
#         try:
#             horse_race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
#         except StopIteration:
#             raise Exception(f"Race {race_type} could not be found!")
#
#         horse_race = next(filter(lambda x: x.race_type == race_type, self.horse_races))
#         if len(horse_race.jockeys) < 2:
#             raise Exception(f"Horse race {race_type} needs at least two participants!")
#
#         highest_speed = 0
#         jockey_winner = ""
#         horse_winner = ""
#         for jockey in horse_race.jockeys:
#             if jockey.horse.speed > highest_speed:
#                 highest_speed = jockey.horse.speed
#                 horse_winner = jockey.horse.name
#                 jockey_winner = jockey.name
#
#         return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_winner}! Winner's horse: {horse_winner}."


class HorseRaceApp:

    HORSE_TYPES_CLASSES_REF = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type in self.HORSE_TYPES_CLASSES_REF:
            self.horses.append(self.HORSE_TYPES_CLASSES_REF[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            horse_race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner = 0

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
