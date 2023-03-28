from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int): # щом в задачата пише from значи е classmethod
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        result = room.take_room(people)

        if result: # ако НЕ са взели стаята
            return result
        else: # ако са взели стаята ги направи гости на хотела
            self.guests += people

    def free_room(self, room_number: int):
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        # правим си променлива която да ни пази броя на гостите в стаята за да можем да ги подвадим от броя гости на хотела
        room_guests = room.guests
        result = room.free_room()

        if result: # ако не сме успяли да освободим стаята
            return result
        else: # ако сме успяли да освободим стаята
            self.guests -= room_guests

    def status(self):
        result = []
        result.append(f"Hotel {self.name} has {self.guests} total guests")
        result.append(f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}")
        result.append(f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")
        return '\n'.join(result)

