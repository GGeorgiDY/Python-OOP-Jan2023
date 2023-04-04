from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    VALID_SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args):
        successfully_added_players_names = []
        for player in args:
            if player not in self.players:
                successfully_added_players_names.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(successfully_added_players_names)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        # player = ""
        # for p in self.players:
        #     if p.name == player_name
        #         player = p
        # if player == "":
        #     return
        #
        # if sustenance_type not in self.VALID_SUSTENANCE_TYPES:
        #     return
        #
        # if player.stamina == player.MAX_STAMINA:
        #     return f"{player_name} have enough stamina."
        #
        # for supply in range(len(self.supplies) -1, 0, -1):
        #     if self.supplies[supply].__class__.__name__ == sustenance_type
        #         if player.stamina + self.supplies[supply] > player.MAX_STAMINA:
        #             player.stamina = player.MAX_STAMINA
        #             s = self.supplies.pop()
        #         else:
        #             player.stamina += self.supplies[supply]
        #             s = self.supplies.pop()
        #         return f"{player_name} sustained successfully with {s.name}."
        # raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player = ""
        for p in self.players:
            if p.name == player_name:
                player = p

        if not player:
            return

        if sustenance_type not in self.VALID_SUSTENANCE_TYPES:
            return

        if player.stamina == player.MAX_STAMINA:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                supply = self.supplies.pop(i)

                if player.stamina + supply.energy > Player.MAX_STAMINA:
                    player.stamina = Player.MAX_STAMINA
                else:
                    player.stamina += supply.energy

                return f"{player_name} sustained successfully with {supply.name}."
        raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next(filter(lambda x: x.name == first_player_name, self.players))
        player2 = next(filter(lambda x: x.name == second_player_name, self.players))

        if player1.stamina == 0 and player2.stamina == 0:
            result = f"Player {first_player_name} does not have enough stamina." + "\n"
            result += f"Player {second_player_name} does not have enough stamina."
            return result

        elif player1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        player_with_lower_value_stamina = player1 if player1.stamina < player2.stamina else player2
        player_with_higher_value_stamina = player1 if player1.stamina > player2.stamina else player2

        taken_damage1 = player_with_lower_value_stamina.stamina / 2
        if player_with_higher_value_stamina.stamina - taken_damage1 <= 0:
            player_with_higher_value_stamina.stamina = 0
            return f"Winner: {player_with_lower_value_stamina}"
        else:
            player_with_higher_value_stamina.stamina -= taken_damage1

        taken_damage2 = player_with_higher_value_stamina.stamina / 2
        if player_with_lower_value_stamina.stamina - taken_damage2 <= 0:
            player_with_lower_value_stamina.stamina = 0
            return f"Winner: {player_with_higher_value_stamina.name}"
        else:
            player_with_lower_value_stamina.stamina -= taken_damage2

        if player_with_lower_value_stamina.stamina > player_with_higher_value_stamina.stamina:
            return f"Winner: {player_with_lower_value_stamina.name}"
        else:
            return f"Winner: {player_with_higher_value_stamina.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}" + "\n"
        for supply in self.supplies:
            result += f"{supply.__class__.__name__}: {supply.name}, {supply.energy}" + "\n"

        return result[:-1]


