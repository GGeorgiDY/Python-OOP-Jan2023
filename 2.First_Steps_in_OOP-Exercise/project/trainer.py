from project.pokemon import Pokemon # ако го пусна така не ми тръгва, а в Judge ми дава 100 от 100
# from pokemon import Pokemon #ако го пусна така кода върви правилно, но в Judge ми дава 14 от 100


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        # долния код може да стане и така
        # is_pokemon = list(filter(lambda p: p.name == pokemon_name, self.pokemons))
        # if is_pokemon:
        #     pokemon = is_pokemon[0] #<pokemon.Pokemon object at 0x000001E3261BFFD0>
        #     pokemon_name = pokemon.name #Pikachu
        #     self.pokemons.remove(pokemon)
        #     return f"You have released {pokemon_name}"
        # return f"Pokemon is not caught"

        # долния код може да стане и с комприхеншън
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0] #това маха списъка, иначе <pokemon.Pokemon object at 0x000001955B0CFFD0> щеше да е списък [<pokemon.Pokemon object at 0x000001955B0CFFD0>]
        #     # print(pokemon) #<pokemon.Pokemon object at 0x000001955B0CFFD0>
        # except IndexError:
        #     return f"Pokemon is not caught"


        # сега ще вземем инстанцията от списъка с покемоните горе
        # този филтър прави цикъл през списъка с покемоните и връща резултат ако името на покемона е еднакво на
        # името (забележи не търсим от инстанцията метода, а атрибута) на покемона, който търсим
        # Понеже ако оставим формулата само с филтър ще ни се върне един обект, който няма да ни върши работа
        # слагаме и функцията next, която ще ни върне първия елемент в колекцията. Ако след това го извикаме отново,
        # ще ни върне следващия елемент
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
            # print(pokemon) #<pokemon.Pokemon object at 0x000002C3192AFFD0>
            # обяснявам горното:
            # p ми е инстанцията "Pokemon("Pikachu", 90)"
            # p.name ми е от инстанцията името "Pikachu"
            # ние търсим дали p.name == pokemon_name(който е str - "Pikachu) в списъка self.pokemons
            # ако го намерим ни върни инстанцията "p" и направи "pokemon" да е равно на "p"

            # filter е итератор и той връща някакво място в паметта
            # next още не знам какво прави

        except StopIteration:
            return f"Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = []
        result.append(f"Pokemon Trainer {self.name}")
        result.append(f"Pokemon count {len(self.pokemons)}")
        [result.append(f"- {p.pokemon_details()}") for p in self.pokemons]

        return '\n'.join(result)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
