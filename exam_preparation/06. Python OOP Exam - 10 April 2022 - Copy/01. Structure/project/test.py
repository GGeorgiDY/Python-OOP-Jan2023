from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)

# print(first_player.stamina)

second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))

# print(len(controller.supplies))
# print(', '.join(x.name for x in controller.supplies))

first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)

# print(len(controller.supplies))
# print(', '.join(x.name for x in controller.supplies))
# print(', '.join(x.details() for x in controller.supplies))

controller.next_day()

# print(len(controller.supplies))
# print(', '.join(x.name for x in controller.supplies))
# print(', '.join(x.details() for x in controller.supplies))

print(controller)


# None
# Successfully added: Peter, Lilly
# Winner: Lilly
# Successfully added:
# Lilly sustained successfully with water.
# Player Peter does not have enough stamina.
# Player: Peter, 15, 0, True
# Player: Lilly, 12, 82.5, True
# Player: Peter, 15, 37, True
# Player: Lilly, 12, 98.5, True
# Food: cheese, 25
# Food: apple, 22



# None
# Successfully added: Peter, Lilly
# Winner: Lilly
# Successfully added:
# Lilly sustained successfully with water.
# Player Peter does not have enough stamina.
# Player: Peter, 15, 0, True
# Player: Lilly, 12, 82.5, True
# Player: Peter, 15, 37, True
# Player: Lilly, 12, 98.5, True
# Food: cheese, 25
# Food: apple, 22

