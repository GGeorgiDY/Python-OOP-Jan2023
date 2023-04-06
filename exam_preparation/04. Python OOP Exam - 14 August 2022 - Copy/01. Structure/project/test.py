from project.horse_race_app import HorseRaceApp

horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))


# Appaloosa horse Spirit is added.
# Thoroughbred horse Rocket is added.
# Jockey Peter is added.
# Jockey Mariya is added.
# Race Summer is created.
# Jockey Peter will ride the horse Spirit.
# Jockey Peter already has a horse.
# Jockey Mariya will ride the horse Rocket.
# Jockey Mariya added to the Summer race.
# Jockey Peter added to the Summer race.
# Jockey Mariya has been already added to the Summer race.
# The winner of the Summer race, with a speed of 110km/h is Mariya! Winner's horse: Rocket.
