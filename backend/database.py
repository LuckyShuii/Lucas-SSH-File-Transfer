from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from db.models.base_model import metadata

class Database:
    engine = None
    Session = None
    name = None
    URL = None

    @staticmethod
    def init():
        Database.URL = Database.generate_url(Config.DB_DATABASE)

        Database.engine = create_engine(Database.URL)
        Database.Session = sessionmaker(bind=Database.engine, autocommit=False, autoflush=False)

        metadata.create_all(Database.engine)

    @staticmethod
    def generate_url(db_name: str):
        return f"postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{db_name}"

    @staticmethod
    def get_session():
        session = Database.Session()
        try:
            yield session
        finally:
            session.close()
