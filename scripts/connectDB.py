#### Imports ####

import sqlite3

import pandas as pd



#### Connecting to database ####

def get_db_connection():
    conn = sqlite3.connect('/Users/kevinzhou/Documents/GitHub/flask-with-db/patients.db')
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql




#### Saving data to a pandas dataframe ####

df = pd.DataFrame(patientListSql)

df

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'sex', 'dob', 'phone_number', 'address', 'pcp_id'] ## manually renaming the columns in the pd df

df