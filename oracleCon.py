
#Python Script to load data to Oracle Database

import pandas as pd
from sqlalchemy import create_engine

# Oracle connection string: Replace placeholders with your actual database details
conn_string = 'oracle+cx_oracle://hr:hr@localhost:1521/?service_name=orclpdb'

# Create the engine and connect to the Oracle database
db = create_engine(conn_string)
conn = db.connect()
# For Single file
df = pd.read_csv('H:/artist.csv')

# Write the DataFrame to the Oracle database table 'artist'
df.to_sql('artist', con=conn, if_exists='replace', index=False)

# Print DataFrame information
print(df.info())

# For multiple files
files=['canvas_size','image_link','museum','museum_hours','product_size','subject','work']

for file in files:
    df = pd.read_csv(f'H:/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)
print(df.info)

