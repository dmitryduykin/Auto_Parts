from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	BigInteger,
	Boolean, 
	Date, 
	Time, 
	Float, 
	ForeignKey,
	create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .meta import Base


engine=create_engine('sqlite:///AutoParts.sqlite')
Session = sessionmaker()
Base=declarative_base(bind=engine)


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Client(Base):
	__tablename__ = 'client'
	id = Column(Integer, primary_key=True)
	login = Column(Text, nullable=False, unique=True)
	password = Column(Text, nullable=False)
	email = Column(Text, nullable=False, unique=True)
	name = Column(Text, nullable=False)	
	lastName = Column(Text, nullable=False)	
	middleName = Column(Text, nullable=False)
	phone = Column(Text, nullable=False)
	orders = Column(Text,ForeignKey("orderlist.id"))

class OrderList(Base):
	__tablename__= 'orderlist'
	id = Column(Integer, primary_key=True)
	orders = Column(Text,nullable=False)
	

class Part(Base):
	__tablename__= 'parts'
	id = Column(Integer, primary_key=True)
	info=Column(Text)
	price=Column(Text)
	available = Column(Boolean)
	model_id = Column(Integer, ForeignKey("carmodels.id"))
	manufacturer_id = Column(Integer, ForeignKey("manufacturer.id"))
	type_id = Column (Integer,ForeignKey("partsType.id"))
	body_id = Column(Integer, ForeignKey("bodies.id"))

class CarModel(Base):
	__tablename__= 'carmodels'
	id = Column(Integer, primary_key=True)
	name = Column(Text,nullable=False)

class Body(Base):
	__tablename__= 'bodies'	
	id = Column(Integer, primary_key=True)
	name = Column(Text,nullable=False)

class Manufacturer(Base):
	__tablename__= 'manufacturer'
	id = Column(Integer, primary_key=True)
	name = Column(Text,nullable=False)

class PartType(Base):
	__tablename__= 'partsType'
	id = Column(Integer, primary_key=True)
	name = Column(Text,nullable=False)
