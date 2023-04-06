from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician_exist = False
        for musician in self.musicians:
            if musician.name == musician_name:
                musician_exist = True
        if not musician_exist:
            raise Exception(f"{musician_name} isn't a musician!")

        band_exist = False
        for band in self.bands:
            if band.name == band_name:
                band_exist = True
        if not band_exist:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda x: x.name == musician_name, self.musicians))
        band = next(filter(lambda x: x.name == band_name, self.bands))

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band_exist = False
        for band in self.bands:
            if band.name == band_name:
                band_exist = True
        if not band_exist:
            raise Exception(f"{band_name} isn't a band!")

        band = next(filter(lambda x: x.name == band_name, self.bands))
        musician_exist = False
        for band_member in band.members:
            if band_member.name == musician_name:
                musician_exist = True
        if not musician_exist:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = next(filter(lambda x: x.name == musician_name, self.musicians))
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        # The concert place and the band name will always be valid.
        concert = next(filter(lambda x: x.place == concert_place, self.concerts))
        band = next(filter(lambda x: x.name == band_name, self.bands))

        copied_valid_musician_types = self.VALID_MUSICIAN_TYPES.copy()

        for band_member in band.members:
            if band_member.__class__.__name__ in copied_valid_musician_types:
                del copied_valid_musician_types[band_member.__class__.__name__]

        if len(copied_valid_musician_types) > 0:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for band_member in band.members:
                if band_member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                elif band_member.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                elif band_member.__class__.__name__ == "Guitarist":
                    if "play rock" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for band_member in band.members:
                if band_member.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                elif band_member.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                elif band_member.__class__.__name__ == "Guitarist":
                    if "play metal" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for band_member in band.members:
                if band_member.__class__.__name__ == "Drummer":
                    if "play the drums with drum brushes" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                elif band_member.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in band_member.skills or "sing low pitch notes" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

                elif band_member.__class__.__name__ == "Guitarist":
                    if "play jazz" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
