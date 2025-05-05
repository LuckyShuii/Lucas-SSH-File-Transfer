# managers/user_manager.py
from managers.base_manager import BaseManager
from db.repositories.user_repository import UserRepository
from db.schemas.user_schema import UserCreate
from db.models.user_model import User
from fastapi import HTTPException, status
import bcrypt

class UserManager(BaseManager, repository=UserRepository):

    # @user_create is a Pydantic model type that defines the structure of the data 
    # this method is used in /routes/user.py for user signup puposes
    async def signup_user(self, user_create: UserCreate) -> User:

        # Make sure the user checked the RGPD policy
        # This is a requirement for the user to be able to register
        if user_create.rgpd is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You must accept the RGPD policy"
            )

        # Check if the username already exists in the database
        existing_username = await self.repository.get_by(
            User.username == user_create.username,
            raise_error=False
        )

        # Check if the email already exists in the database
        existing_email = await self.repository.get_by(
            User.email == user_create.email,
            raise_error=False
        )

        # If the user already exists, raise an error
        if existing_username or existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already registered"
            )

        # convert the user_create object to a dictionary to remove the rgpd field
        data = user_create.dict(exclude={"rgpd"}, exclude_unset=True)

        # Hash the password using bcrypt
        # bcrypt requires the password to be in bytes, so we encode it
        pw_bytes = data["password"].encode("utf-8")

        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(pw_bytes, salt).decode("utf-8")
        data["password"] = hashed

        # Create a new user object with the hashed password
        user_obj = User(**data)

        # Create the user in the database
        return await self.repository.create(user_obj)
