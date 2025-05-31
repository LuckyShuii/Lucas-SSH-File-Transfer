# managers/user_manager.py
from managers.base_manager import BaseManager
from db.repositories.user_repository import UserRepository
from db.schemas.user_schema import UserCreate
from db.models.user_model import User
from fastapi import HTTPException, status
from utils.mailing import Mailer
from utils.jwt import JwtGenerator
import bcrypt

class UserManager(BaseManager, repository=UserRepository):

    # @user_create is a Pydantic model type that defines the structure of the data 
    # this method is used in /routes/user.py for user signup puposes
    async def signup_user(self, user_create: UserCreate):
        # Make sure the user checked the RGPD policy
        # This is a requirement for the user to be able to register
        if user_create.rgpd is False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You must accept the terms and conditions"
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
                detail="Username or email already exists"
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
        new_user = await self.repository.create(user_obj)

        if not new_user:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="User could not be created"
            )
        
        # Generate a JWT token for the user
        # This token will be used to activate the account
        # The token contains the user's UUID and is valid for 12 hours
        sign_up_jwt = JwtGenerator().generate_token(
            payload={"uuid": new_user.uuid},
            validity_time=12
        )
        
        # Send a welcome email to the user
        # The Mailer class is used to send emails
        # It uses the Mailjet API to send emails
        # The email contains a welcome message and a link to activate the account
        # The link is valid for 48 hours
        Mailer().send_email(
            target_email=new_user.email,
            username=new_user.username,
            message="Welcome to our service! Your account has been created successfully.",
            subject="Welcome to Our Service!",
            text_part="Thank you for signing up!",
            html_part="<h3>Dear {username}, welcome to our service!</h3><br />Thank you for signing up. We are excited to have you on board!<br /><br />Click on this link to activate your account (valid for 12 hours)<br />http://localhost:8080/activate-account?token={jwt}".format(username=data["username"], jwt=sign_up_jwt)
        )
        
        # Return a success message
        raise HTTPException(
            status_code=status.HTTP_201_CREATED,
            detail="User created successfully"
        )

    async def activate_account(self, token: str):
        try:
            decoded_token = JwtGenerator().decode_token(token)
        except Exception as e:
            print(f"Error decoding token: {e}")
            decoded_token = None

        if not decoded_token:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An error occured while activating your account, the link seems to be invalid or expired."
            )
        
        # Get the user by UUID from the decoded token
        user = await self.repository.get_by(
            User.uuid == decoded_token["uuid"],
        )        

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        # return user.is_activated
        if user.is_activated == 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Your account is already activated!"
            )
        
        # Activate the user account
        user.is_activated = 1

        updated_user = await self.repository.patch_where(user, User.uuid == user.uuid)

        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Your account could not be activated, please try again later or contact support."
            )
        
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Your account was activated successfully!"
        )
    