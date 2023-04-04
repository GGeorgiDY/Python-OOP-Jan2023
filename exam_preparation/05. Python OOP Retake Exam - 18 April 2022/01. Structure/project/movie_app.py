from typing import List
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                return "User already exists!"

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        usernames_collection = [x.username for x in self.users_collection]
        if username not in usernames_collection:
            raise Exception("This user does not exist!")

        user = next(filter(lambda x: x.username == username, self.users_collection))
        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        movie.owner = user
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        # Only the owner of the movie given can edit it. You will always be given usernames of registered users.
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            if k == "title":
                movie.title = v
            elif k == "year":
                movie.year = v
            elif k == "age_restriction":
                movie.age_restriction = v
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        # Only the owner of the movie given can delete it. You will always be given usernames of registered users.
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = next(filter(lambda x: x.username == username, self.users_collection))
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            user.movies_liked.remove(movie)
        movie.likes = 0

        title = movie.title
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {title} movie."

    def like_movie(self, username: str, movie: Movie):
        # Owners cannot like their own movies. You will always be given usernames of registered users and uploaded movies.
        user = next(filter(lambda x: x.username == username, self.users_collection))

        if user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        # Only the user who has liked the movie can dislike it. You will always be given usernames of registered users and uploaded movies.
        user = next(filter(lambda x: x.username == username, self.users_collection))
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        # if not self.movies_collection:
        #     return "No movies found."
        #
        # my_dict = {}
        # counter = 1
        # for movie in self.movies_collection:
        #     my_dict[counter] = {'kind': movie.__class__.__name__, 'Title': movie.title, "Year": movie.year, "Age restriction": movie.age_restriction, "Likes": movie.likes, "Owned by": movie.owner.username}
        #     counter += 1
        #
        # # print(my_dict)
        # sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1]['Year'], x[1]['Title'])))
        # # print(sorted_dict)
        #
        # result = ""
        # list_result =[]
        # for k, v in sorted_dict.items():
        #     for smth, info in v.items():
        #         if smth == 'kind':
        #             result = f"{info} - "
        #         elif smth == 'Title':
        #             result += f"Title:{info}, "
        #         elif smth == 'Year':
        #             result += f"Year:{info}, "
        #         elif smth == 'Age restriction':
        #             result += f"Age restriction:{info}, "
        #         elif smth == 'Likes':
        #             result += f"Likes:{info}, "
        #         elif smth == 'Owned by':
        #             result += f"Owned by:{info}"
        #     list_result.append(result)
        # return '\n'.join(list_result)

        # Fantasy - Title: The Lord of the Rings, Year: 2003, Age restriction: 14, Likes: 0, Owned by: Alexandra
        # Action - Title: Die Hard, Year: 1988, Age restriction: 18, Likes: 1, Owned by: Martin

        if not self.movies_collection:
            return "No movies found."
        result = []
        for movie in sorted(self.movies_collection, key=lambda x: [-x.year, x.title]):
            result.append(movie.details())
        return "\n".join(result)

    def __str__(self):
        # usernames = [x.username for x in self.users_collection]
        # movies_titles = [x.title for x in self.movies_collection]
        #
        # if usernames:
        #     result = f"All users: {', '.join(usernames)}" + "\n"
        # else:
        #     result = f"All users: No users." + "\n"
        #
        # if movies_titles:
        #     result += f"All movies: {', '.join(movies_titles)}"
        # else:
        #     result += f"All movies: No movies."
        # return result

        users = "All users: "
        if not self.users_collection:
            users += "No users."
        else:
            users += (', '.join([user.username for user in self.users_collection]))

        movies = "All movies: "
        if not self.movies_collection:
            movies += "No movies."
        else:
            movies += (', '.join([movie.title for movie in self.movies_collection]))

        return users + "\n" + movies
