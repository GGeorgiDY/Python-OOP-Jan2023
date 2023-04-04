class Player:
    player_names = []
    MAX_STAMINA = 100

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    # name validation
    @property
    def name(self):
        return self.__name

    @staticmethod
    def __check_if_name_is_unique(name):
        if name in Player.player_names:
            return True
        return False

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if self.__check_if_name_is_unique(value):
            raise Exception(f"Name {value} is already used!")
        Player.player_names.append(value)
        self.__name = value

    # age validation
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    # stamina validation
    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return True if self.stamina < Player.MAX_STAMINA else False

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


