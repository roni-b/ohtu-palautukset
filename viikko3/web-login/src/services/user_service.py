import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def check_password(self, password, pass_confirmation):
        if len(password) < 8:
            raise UserInputError("Password too short")

        if password.isalpha():
            raise UserInputError("Invalid password")

        if password != pass_confirmation:
            raise UserInputError("Passwords are different")

    def check_username(self, username):
        if self._user_repository.find_by_username(username):
            raise(UserInputError(f"User with username {username} already exists"))

        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Invalid username")

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        self.check_username(username)
        self.check_password(password, password_confirmation)



user_service = UserService()
