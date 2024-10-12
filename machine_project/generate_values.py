import pandas as pd
import random
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String  # Ensure this line is included

# Load the Excel file
df = pd.read_excel('Backend Developer Task.xlsx', sheet_name='AXIS')

# Generate values for 5 axes (X, Y, Z, A, C) for 20 machines
axis = ['X', 'Y', 'Z', 'A', 'C']
num_machines = 20

# Example logic to generate random values for each axis
def generate_values():
    values = {}
    for ax in axis:
        values[ax] = [random.uniform(0, 100) for _ in range(num_machines)]
    return values

# Create SQLAlchemy engine
engine = create_engine('sqlite:///machine_data.db')  # SQLite for simplicity

# Define schema
metadata = MetaData()

machine_data = Table('machine_data', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('machine_id', Integer),
                     Column('axis', String),
                     Column('value', Float))

metadata.create_all(engine)

# Insert generated values into the database
def insert_values():
    conn = engine.connect()
    values = generate_values()
    for machine_id in range(1, num_machines+1):
        for ax in axis:
            conn.execute(machine_data.insert(), {"machine_id": machine_id, "axis": ax, "value": values[ax][machine_id-1]})

insert_values()
print("Values generated and inserted into the database.")
