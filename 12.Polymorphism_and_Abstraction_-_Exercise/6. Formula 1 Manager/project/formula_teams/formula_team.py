from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget
    
    @property
    @abstractmethod
    def sponsors(self):
        pass
    
    @property
    @abstractmethod
    def expenses_for_one_race(self):
        pass
    
    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for k, v in self.sponsors.items():
            for pos, amount in v.items():
                if race_pos <= pos:
                    revenue += amount
                    break

        revenue -= self.expenses_for_one_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


