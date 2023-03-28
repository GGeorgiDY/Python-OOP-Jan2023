from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        # добавяме юзъра ако го няма в списъка с юзъри на библиотеката
        if user.user_id in [x.user_id for x in library.user_records]:
            return f"User with id = {user.user_id} already registered in the library!"
        else:
            library.user_records.append(user.user_id)

        # махаме юзър, ако съществува
    def remove_user(self, user: User, library: Library):
        if user.user_id in [x.user_id for x in library.user_records]:
            library.user_records.remove(user.user_id)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user = next(filter(lambda x: x.user_id == user_id, library.user_records))
        except StopIteration: #ако няма такъв потребител
            return f"There is no user with id = {user_id}!"

        # гледаме дали не подава същия юзърнейм като стария
        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        if user.username in library.rented_books:
            library.rented_books[new_username] = library.rented_books[user.username]
            del library.rented_books[user.username]
        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"

