from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATH = 5

    def __init__(self, name: str, oxygen: int = 70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.BREATH
