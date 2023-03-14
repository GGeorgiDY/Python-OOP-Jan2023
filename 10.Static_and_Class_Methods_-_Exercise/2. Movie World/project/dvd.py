from calendar import month_name


class DVD:
    def __init__(self, name: str, id_number: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    # тук се иска от нас да ъпдейтнем горните инстанс атрибути с клас метод
    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int): # date format => dd.mm.yyyy
        day, month, year = [int(x) for x in date.split(".")]
        return cls(name, id_number, year, month_name[month], age_restriction) # month_name[1] = January

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"


# d = DVD('a', 1, 2021, 'January', 1)
# print(d)    # 1: a (January 2021) has age restriction 1. Status: not rented
# d = DVD.from_date(2, 'b', '02.02.2022', 2)
# print(d)    # 2: b (February 2022) has age restriction 2. Status: not rented