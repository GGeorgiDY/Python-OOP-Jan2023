from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    BREATH = 10

    def __init__(self, name: str, oxygen: int = 50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.BREATH
