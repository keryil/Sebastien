from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

UNITS = ["Volume", "Weight", "Quantity"]

# ORM base
Base = declarative_base()


# ORM types
class Product(Base):
    """
    I am any product you can put on a list.
    """
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    units = Column(String, nullable=False)
    unit_price = Column(Float)

    def __repr__(self):
        return "<Product(name='%s', units='%s', unit_price='%f')>" % (self.name, self.units, self.unit_price)
