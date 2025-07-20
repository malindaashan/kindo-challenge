from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# from kindoapp.main import app

DATABASE_URL = "postgresql://postgres:root@localhost:5432/kindo"  # Replace with your DB URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#
# @app.on_event("startup")
# def on_startup():
#     print("Creating tables if they don't exist...")
#     Base.metadata.create_all(bind=engine)
