from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_ADD = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.MAX_SPEED = speed
        self.is_taken = False

    def train(self):
        self.speed += self.MAX_SPEED if self.speed + self.SPEED_ADD > self.MAX_SPEED else self.speed + self.SPEED_ADD
