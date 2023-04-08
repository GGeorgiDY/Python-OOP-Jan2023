from project.movie_app import MovieApp
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action

movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)

# movie4 = Action('CDie Hard', 1988, user, 18)
# movie5 = Action('FDie Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie4))
# print(movie_app.upload_movie('Martin', movie5))

print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)

print(user)

# Martin registered successfully.
# Martin successfully added Die Hard movie.
# Die Hard
# Alexandra registered successfully.
# Alexandra successfully added Free Guy movie.
# Alexandra successfully edited Free Guy 2 movie.
# Martin liked Free Guy 2 movie.
# Alexandra liked Die Hard movie.
# Martin disliked Free Guy 2 movie.
# Martin liked Free Guy 2 movie.
# Alexandra successfully deleted Free Guy 2 movie.
# Alexandra successfully added The Lord of the Rings movie.
# Fantasy - Title:The Lord of the Rings, Year:2003, Age restriction:14, Likes:0, Owned by:Alexandra
# Action - Title:Die Hard, Year:1988, Age restriction:18, Likes:1, Owned by:Martin
# All users: Martin, Alexandra
# All movies: Die Hard, The Lord of the Rings

