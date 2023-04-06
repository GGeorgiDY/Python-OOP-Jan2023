from project.band_members.musician import Musician


class Drummer(Musician):
    VALID_TYPES_OF_SKILLS = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.skills = []

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.VALID_TYPES_OF_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."
