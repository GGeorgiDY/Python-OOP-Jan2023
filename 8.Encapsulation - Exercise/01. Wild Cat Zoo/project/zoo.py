from typing import List
from project.animal import Animal
from project.worker import Worker
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: float, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: List[Animal] = [] # пазим инстанции
        self.workers: List[Worker] = [] # пазим инстанции

    def add_animal(self, animal: Animal, price: float):
        if price > self.__budget:
            return "Not enough budget"
        elif len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        # salaries = sum(w.salary for w in self.workers) # може и така

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_animals = sum(a.money_for_care for a in self.animals)
        if self.__budget >= money_for_animals:
            self.__budget -= money_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        all_lions = [repr(lion) for lion in self.animals if isinstance(lion, Lion)]
        all_tigers = [repr(tiger) for tiger in self.animals if isinstance(tiger, Tiger)]
        all_cheetahs = [repr(cheetah) for cheetah in self.animals if isinstance(cheetah, Cheetah)]

        output = f"You have {len(self.animals)} animals\n"
        output += f"----- {len(all_lions)} Lions:\n"
        output += "\n".join(all_lions) + "\n"

        output += f"----- {len(all_tigers)} Tigers:\n"
        output += "\n".join(all_tigers) + "\n"

        output += f"----- {len(all_cheetahs)} Cheetahs:\n"
        output += "\n".join(all_cheetahs)

        return output

    def workers_status(self):
        all_keepers = [repr(x) for x in self.workers if isinstance(x, Keeper)]
        all_caretakers = [repr(x) for x in self.workers if isinstance(x, Caretaker)]
        all_vets = [repr(x) for x in self.workers if isinstance(x, Vet)]

        output = f"You have {len(self.workers)} workers\n"
        output += f"----- {len(all_keepers)} Keepers:\n" + "\n".join(all_keepers) + "\n"
        output += f"----- {len(all_caretakers)} Caretakers:\n" + "\n".join(all_caretakers) + "\n"
        output += f"----- {len(all_vets)} Vets:\n" + "\n".join(all_vets)

        return output.strip()


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
