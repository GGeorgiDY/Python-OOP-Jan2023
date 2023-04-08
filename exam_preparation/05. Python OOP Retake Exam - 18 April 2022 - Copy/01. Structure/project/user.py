from typing import List

from project.movie_specification.movie import Movie


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        movies_liked = '\n'.join(x.details() for x in self.movies_liked)
        movies_owned = '\n'.join(x.details() for x in self.movies_owned)

        result = f"Username: {self.username}, Age: {self.age}" + "\n"
        result += "Liked movies:" + "\n"
        if len(self.movies_liked) == 0:
            result += "No movies liked." + "\n"
        else:
            result += f"{movies_liked}" + "\n"
        result += "Owned movies:" + "\n"
        if len(self.movies_owned) == 0:
            result += "No movies owned." + "\n"
        else:
            result += f"{movies_owned}"
        return result
