import jwt
from config import Config
import time, datetime
from datetime import timezone

class JwtGenerator:
    def __init__(self, algorithm: str = "HS256"):
        self.secret_key = Config.JWT_SECRET_KEY
        self.algorithm = algorithm

    def generate_token(self, payload: dict, validity_time: str) -> str:
        return jwt.encode({**payload, "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(hours=validity_time)}, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> dict:
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])