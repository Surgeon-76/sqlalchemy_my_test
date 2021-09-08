from sqlalchemy import create_engine, MetaData, Table, Integer,\
    String, Column, DateTime, ForeignKey, Numeric, SmallInteger
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime

user_name_db = 'surglin'
password_db = 'Nusha230399'
db_name = 'sqlalchemy_test'

engine = sqlalchemy.create_engine(f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}")


Base = declarative_base()


class Cusomer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship('Order', backref='customer')


    