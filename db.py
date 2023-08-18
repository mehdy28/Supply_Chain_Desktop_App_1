import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.DataBase_Models import Base
from schemas.DataBase_Schemas import *
from config import Config

DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI

# Create the engine and session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Create tables in the database
Base.metadata.create_all(engine)

# Load CSV files into DataFrames
customers_df = pd.read_csv('Data/dim_customers_clean.csv')
products_df = pd.read_csv('Data/dim_products_clean.csv')
targets_df = pd.read_csv('Data/dim_targets_orders_clean.csv')
order_lines_df = pd.read_csv('Data/fact_order_lines_clean.csv')
order_aggregate_df = pd.read_csv('Data/fact_orders_aggregate_clean.csv')

# Insert data into the database using SQLAlchemy and Pandas
session = Session()
customers_df.to_sql('customers', con=engine, if_exists='append', index=False)
products_df.to_sql('products', con=engine, if_exists='append', index=False)
targets_df.to_sql('targets', con=engine, if_exists='append', index=False)
order_lines_df = order_lines_df.drop_duplicates(subset=['order_id'])
order_lines_df.to_sql('order_lines', con=engine, if_exists='append', index=False)
order_aggregate_df.to_sql('order_aggregate', con=engine, if_exists='append', index=False)
session.close()

print("Data inserted into the database.")
