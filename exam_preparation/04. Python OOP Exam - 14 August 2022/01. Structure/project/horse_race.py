from typing import List
from project.jockey import Jockey


class HorseRace:
    # It will store the details for every race.
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys: List[Jockey] = [] # will store all the jockeys (objects) who will take part in the race.
        self.valid_race_types = ["Winter", "Spring", "Autumn", "Summer"]

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        # if value not in self.valid_race_types: #това не знам защо не работи
        if not(value == "Winter" or value == "Spring" or value == "Autumn" or value == "Summer"):
            raise ValueError("Race type does not exist!")
        self.__race_type = value
