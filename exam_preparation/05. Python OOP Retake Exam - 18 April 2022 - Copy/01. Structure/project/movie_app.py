from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        for name in self.users_collection:
            if name.username == username:
                raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user_exist = False
        for name in self.users_collection:
            if name.username == username:
                user_exist = True
        if not user_exist:
            raise Exception("This user does not exist!")

        user = next(filter(lambda x: x.username == username, self.users_collection))
        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        # Only the owner of the movie given can edit it. You will always be given usernames of registered users.
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute, new_attribute in kwargs.items():
            if attribute == "title":
                movie.title = new_attribute
            elif attribute == "year":
                movie.year = new_attribute
            elif attribute == "age_restriction":
                movie.age_restriction = new_attribute

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        # Only the owner of the movie given can delete it. You will always be given usernames of registered users.
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        # Owners cannot like their own movies. You will always be given usernames of registered users and uploaded movies.
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        # Only the user who has liked the movie can dislike it. You will always be given usernames of registered users and uploaded movies.
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        my_dict = {}
        for movie in self.movies_collection:
            my_dict[movie] = movie.year, movie.title

        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1][0], x[1][1])))
        self.movies_collection = [x for x in sorted_dict.keys()]

        result = ""
        for movie in sorted_dict:
            result += f"{movie.details()}" + "\n"
        return result[:-1]

    def __str__(self):
        result = ""
        if len(self.users_collection) == 0:
            result = "All users: No users." + "\n"
        else:
            result = f"All users: {', '.join(x.username for x in self.users_collection)}" + "\n"

        if len(self.movies_collection) == 0:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join(x.title for x in self.movies_collection)}"

        return result
