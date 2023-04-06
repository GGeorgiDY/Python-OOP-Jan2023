from project.concert_tracker_app import ConcertTrackerApp

musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]
app = ConcertTrackerApp()
for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))
print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))
print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))
print(app.remove_musician_from_band(names[2], "RockName"))
print(app.add_musician_to_band(names[2], "RockName"))
print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))


# George is now a Singer.
# Alex is now a Drummer.
# Lilly is now a Guitarist.
# George learned to sing high pitch notes.
# Alex learned to play the drums with drumsticks.
# Lilly learned to play rock.
# RockName was created.
# George was added to RockName.
# Alex was added to RockName.
# Lilly was added to RockName.
# Rock concert in Sofia was added.
# ['Singer', 'Drummer', 'Guitarist']
# RockName gained 47.30$ from the Rock concert in Sofia.
