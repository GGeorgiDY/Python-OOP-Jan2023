from project.booths.booth import Booth


class PrivateBooth(Booth):
    # нарочно се прави така, а не като клас атрибут, защото:
    # да не може да се промени от глобалния скоуп
    # така кода става по сигурен.
    @property
    def get_price_per_person(self):
        return 3.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.get_price_per_person
        self.is_reserved = True
