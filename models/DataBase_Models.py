from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Float,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    city = Column(String)

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)

class Target(Base):
    __tablename__ = 'targets'
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), primary_key=True)
    ontime_target_percent = Column(Float)
    infull_target_percent = Column(Float)
    otif_target_percent = Column(Float)

class OrderLine(Base):
    __tablename__ = 'order_lines'
    order_id = Column(String(50), primary_key=True)
    order_placement_date = Column(Date)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    order_qty = Column(Integer)
    agreed_delivery_date = Column(Date)
    actual_delivery_date = Column(Date)
    delivery_qty = Column(Integer)
    in_full = Column(Boolean)
    on_time = Column(Boolean)
    on_time_in_full = Column(Boolean)

class OrderAggregate(Base):
    __tablename__ = 'order_aggregate'
    order_id = Column(String(50), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    order_placement_date = Column(Date)
    on_time = Column(Boolean)
    in_full = Column(Boolean)
    otif = Column(Boolean)