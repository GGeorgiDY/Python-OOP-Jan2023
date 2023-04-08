from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_SUSTENANCE_TYPES = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player_exist = False
        for player in self.players:
            if player.name == player_name:
                player_exist = True
        if not player_exist:
            return

        if sustenance_type not in self.VALID_SUSTENANCE_TYPES:
            return

        player = next(filter(lambda x: x.name == player_name, self.players))
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food":
            food_exist = False
            for supply in self.supplies:
                if supply.__class__.__name__ == "Food":
                    food_exist = True
            if not food_exist:
                raise Exception("There are no food supplies left!")

        elif sustenance_type == "Drink":
            drink_exist = False
            for supply in self.supplies:
                if supply.__class__.__name__ == "Drink":
                    drink_exist = True
            if not drink_exist:
                raise Exception("There are no drink supplies left!")

        # supply = next(filter(lambda x: x.__class__.__name__ == sustenance_type, self.supplies))
        supply = ""
        for s in range(len(self.supplies) -1, -1, -1):
            if self.supplies[s].__class__.__name__ == sustenance_type:
                supply = self.supplies.pop(s)
                break

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

        supply_name = supply.name
        return f"{player_name} sustained successfully with {supply_name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = next(filter(lambda x: x.name == first_player_name, self.players))
        second_player = next(filter(lambda x: x.name == second_player_name, self.players))

        if first_player.stamina == 0 and second_player.stamina == 0:
            result = f"Player {first_player_name} does not have enough stamina." + "\n"
            result += f"Player {second_player_name} does not have enough stamina."
            return result

        elif first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        player_with_lower_stamina = first_player if first_player.stamina < second_player.stamina else second_player
        player_with_higher_stamina = first_player if first_player.stamina > second_player.stamina else second_player

        if player_with_higher_stamina.stamina - player_with_lower_stamina.stamina / 2 <= 0:
            player_with_higher_stamina.stamina = 0
            return f"Winner: {player_with_lower_stamina.name}"
        else:
            player_with_higher_stamina.stamina -= player_with_lower_stamina.stamina / 2

        if player_with_lower_stamina.stamina - player_with_higher_stamina.stamina / 2 <= 0:
            player_with_lower_stamina.stamina = 0
            return f"Winner: {player_with_higher_stamina.name}"
        else:
            player_with_lower_stamina.stamina -= player_with_higher_stamina.stamina / 2

        if player_with_higher_stamina.stamina > player_with_lower_stamina.stamina:
            return f"Winner: {player_with_higher_stamina.name}"
        else:
            return f"Winner: {player_with_lower_stamina.name}"

    def next_day(self):
        for player in self.players:
            reducer = player.age * 2
            if player.stamina - reducer < 0:
                player.stamina = 0
            else:
                player.stamina -= reducer

        # for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}" + "\n"
        for supply in self.supplies:
            result += f"{supply.__class__.__name__}: {supply.name}, {supply.energy}" + "\n"
        return result[:-1]
