from sqlalchemy import create_engine, MetaData, Table, Integer,\
    String, Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, sessionmaker

from datetime import datetime

user_name_db = 'surglin'
password_db = 'Nusha230399'
db_name = 'sqlalchemy_test'

engine = create_engine(f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}", echo=True)

session = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    # orders = relationship("Order", backref='customer')


# class Item(Base):
#     __tablename__ = 'items'
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(200), nullable=False)
#     cost_price = Column(Numeric(10, 2), nullable=False)
#     selling_price = Column(Numeric(10, 2), nullable=False)
#     quantity = Column(Integer())


# class Order(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer(), primary_key=True)
#     customer_id = Column(Integer(), ForeignKey('customers.id'))
#     date_placed = Column(DateTime(), default=datetime.now)
#     line_items = relationship("OrderLine", backref='order')


# class OrderLine(Base):
#     __tablename__ = 'order_lines'
#     id = Column(Integer(), primary_key=True)
#     order_id = Column(Integer(), ForeignKey('orders.id'))
#     item_id = Column(Integer(), ForeignKey('items.id'))
#     quantity = Column(SmallInteger())
#     item = relationship("Item")

#session = Session()

db  = session()

Base.metadata.create_all(engine)



c1 = Customer(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko',
    username = 'Moseend',
    email = 'moseend@mail.com'
)

# c2 = Customer(
#     first_name = 'Valeriy',
#     last_name = 'Golyshkin',
#     username = 'Fortioneaks',
#     email = 'fortioneaks@gmail.com'
# )

print(c1.first_name)

db.add(c1)
#session.add(c2)

print(db.new)

#Base.metadata.create_all(engine)
db.commit()
db.close()