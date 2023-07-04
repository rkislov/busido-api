from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocoomit=False, autoflush=False, bind=engine)
