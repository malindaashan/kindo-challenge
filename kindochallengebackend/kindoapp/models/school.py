from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from kindoapp.config.database import Base


class School(Base):
    __tablename__ = "school"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    school_name = Column(String)
