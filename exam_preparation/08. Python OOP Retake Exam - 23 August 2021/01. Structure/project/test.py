from project.space_station import SpaceStation

s = SpaceStation()
print(s.add_astronaut("Biologist", "Ime"))
print(s.add_planet("ime", "asd, 123, 456"))
print(s.planet_repository.planets[0].items)
print(s.add_planet("ime", "asd, 123, 456, 321313, 123, 456, asd, 123, 456, d, 123, 456, asd, 123, 456, asd, 123, 456, asd, asd, 123, 456, asd, asd, 123, 456, asd, 123, 456, asd, 123, 456, asd, 123"))
print(s.send_on_mission("ime"))
print(s.retire_astronaut("Ime"))
print(s.astronaut_repository.astronauts)
print(s.add_astronaut("Meteorologist", "Ime"))
print(s.astronaut_repository.find_by_name("Ime").oxygen)
s.recharge_oxygen()
print(s.astronaut_repository.find_by_name("Ime").oxygen)
print(s.planet_repository.find_by_name('ime').name)
print(s.add_astronaut("Geodesist", 'Ime2'))
print(s.add_astronaut("Geodesist", 'Ime3'))
print(s.add_astronaut("Geodesist", 'Ime4'))
print(s.add_astronaut("Geodesist", 'Ime5'))
print(s.add_astronaut("Biologist", 'Ime6'))
print("--------------")
print(s.send_on_mission('ime'))
print(s.planet_repository.find_by_name('ime').items)
print(s.astronaut_repository.astronauts[0].backpack)
print("--------------------------")
print(s.report())
print(s.astronaut_repository.astronauts[0].backpack)