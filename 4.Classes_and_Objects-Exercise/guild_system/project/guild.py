from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name #името на гилд-а
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild." # пишем .name защото иначе ще е инстанция. А с това
            # .name отива в другия файл и взема името
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        #трябва първо да намерим играча
        try:
            player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        [result.append(x.player_info()) for x in self.players]
        return '\n'.join(result)