from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    # PORTION = 200 # може и така да се напише, като в супера ще е self.PORTION

    @property
    def get_portion(self):
        return 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.get_portion, price)

    def details(self):
        return f"Gingerbread {self.name}: {self.get_portion}g - {self.price:.2f}lv."

