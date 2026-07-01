import hashlib

from app.auth.user_repository import UserRepository


class AuthService:

    def __init__(self):

        self.users = UserRepository()

    def hash_password(self, password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    def register(self, name, email, password):

        existing = self.users.get_user_by_email(
            email
        )

        if existing:

            return False, "User already exists."

        hashed = self.hash_password(
            password
        )

        self.users.create_user(
            name,
            email,
            hashed
        )

        return True, "Registration successful."

    def login(self, email, password):

        user = self.users.get_user_by_email(
            email
        )

        if not user:

            return False, None

        hashed = self.hash_password(
            password
        )

        if user["password"] != hashed:

            return False, None

        return True, user