import hashlib
import secrets

class Hash:
    SALT = 'RamirAbdulov'

    def get_hash(self, password: str) -> str:
        return hashlib.md5(password.encode() + self.SALT.encode()).hexdigest()

    def check_password(self, hashed_password: str, password: str) -> bool:
        return self.get_hash(password) == hashed_password

    @staticmethod
    def get_token() -> str:
        return secrets.token_hex(32)
