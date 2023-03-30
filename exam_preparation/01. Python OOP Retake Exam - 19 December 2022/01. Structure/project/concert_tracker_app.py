from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        valid_musician_types = ["Guitarist", "Drummer", "Singer"]

        if musician_type not in valid_musician_types:
            raise ValueError("Invalid musician type!")

        if name in [x.name for x in self.musicians]:
            raise ValueError(f"{name} is already a musician!")

        #create the musician
        if musician_type == valid_musician_types[0]:
            musician = Guitarist(name, age)

        if musician_type == valid_musician_types[1]:
            musician = Drummer(name, age)

        if musician_type == valid_musician_types[2]:
            musician = Singer(name, age)

        # add it to the musicians' list
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [x.name for x in self.bands]:
            raise Exception(f"{name} band is already created!")

        # create a new band
        band = Band(name)
        # add it to the bands' list
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in [x.name for x in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")
        if band_name not in [x.name for x in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        # add the musician to the band
        band = [x for x in self.bands if x.name == band_name][0]
        musician = [x for x in self.musicians if x.name == musician_name][0]
        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        # If there isn't a band with the given name
        if band_name not in [x.name for x in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        # If there isn't a musician with the given name who is a member of the given band
        band = [x for x in self.bands if x.name == band_name][0]
        if musician_name not in [x.name for x in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        # remove the musician from the band
        musician = [x for x in self.musicians if x.name == musician_name][0]
        band.members.remove(musician)

    def start_concert(self, concert_place: str, band_name: str):
        # The concert place and the band name will always be valid

        # If there is NOT at least one member of each type (at least 1 singer, at least 1 drummer, and at least
        # 1 guitarist), raise an Exception
        band = [x for x in self.bands if x.name == band_name][0]
        type_members = [type(x).__name__ for x in band.members]
        if "Guitarist" not in type_members or "Singer" not in type_members or "Drummer" not in type_members:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [x for x in self.concerts if x.place == concert_place][0]
        if concert.genre == "Rock":
            needed_skills = ["play the drums with drumsticks", "sing high pitch notes", "play rock"]
        elif concert.genre == "Metal":
            needed_skills = ["play the drums with drumsticks", "sing low pitch notes", "play metal"]
        elif concert.genre == "Jazz":
            needed_skills = ["play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes", "play jazz"]

        members = band.members
        for member in members:
            needed_skills_copy = needed_skills.copy()
            for skill in needed_skills_copy:
                if skill in member.skills:
                    needed_skills.remove(skill)

        if needed_skills:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."


