#### Imports ####

import sqlite3



#### Connect to SQLite ####

connect = sqlite3.connect('/Users/kevinzhou/Documents/GitHub/flask-with-db/patients.db')

db = connect.cursor() ## opening our connection to object we have named db

db.execute("DROP TABLE IF EXISTS patient_table") ## deleting a patients table if there exists one. not necessary in this particular case since it's our first instance

connect.commit() ## committing our change



#### Creating our table ####

table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            sex VARCHAR(1) NOT NULL,
            dob DATE NOT NULL,
            phone_number NUMBER NOT NULL,
            address VARCHAR(255) NOT NULL,
            pcp_id NUMBER NOT NULL
        ); """


db.execute(table)

connect.commit()



#### Populating the table with data #### 

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('178493029', 'Gary', 'Stokes', 'M', '12/09/1990', '2063257635', '1237 Owagner Lane Seattle, WA 98122', '748392084')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('174746645', 'Samantha', 'Barnett', 'F', '09/20/1966', '6418333039', '1600 Morningview Lane Kanawha, IA 50447', '284738292')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('136743555', 'Neil', 'Adams', 'M', '03/26/1967', '2692006166', '1458 Garrett Street Grand Rapids, MI 49503', '274839202')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('163278949', 'Belinda', 'Franks', 'F', '08/10/1983', '2026890760', '2604 Massachusetts Avenue Washington, DC 20036', '111164789')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('112334345', 'Morty', 'Dickerson', 'M', '10/14/1979', '8056729373', '1683 Creekside Lane Ventura, CA 93004', '829374638')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('121431245', 'Vincent', 'Gonzales', 'M', '04/26/1971', '7322302882', '2772 Pooz Street Freehold, NJ 07728', '453627189')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('136132173', 'Jessica', 'Snowden', 'F', '01/22/1981', '5032146327', '4791 Karen Lane Portland, OR 97218', '453627189')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('137248901', 'Lois', 'Laramie', 'F', '12/10/1940', '7733480079', '3072 Oakmound Drive Chicago, IL 60657', '111164789')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('165849306', 'Joe', 'Swanson', 'M', '12/31/1980', '7017832615', '3906 Findley Avenue Guelph, ND 58447', '748392084')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, sex, dob, phone_number, address, pcp_id) values('167283949', 'Georgie', 'Garcia', 'M', '01/26/1983', '6128792919', '4035 Rocket Drive Minneapolis, MN 55404', '111164789')")

connect.commit()

connect.close()