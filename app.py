#### Terminal commands ####

'pip install -r requirements' ## ensures requirements are installed

'python3 app.py' ## runs the application

'sudo nohup python3 app.py > log.txt 2>&1 &' ## this terminal command ensures that the app runs in the background even when the client is shut down




#### Imports ####

from flask import Flask, render_template

import sqlite3

import os




#### Creating a connection that is called when users first access page ####

def get_db_connection():
    dir = os.getcwd() + '/patients.db'
    print('dir:', dir)
    conn = sqlite3.connect(dir) 
    conn.row_factory = sqlite3.Row 
    return conn

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/patients')
def patients():
    conn = get_db_connection()
    patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientListSql:', patientListSql)
    return render_template('patients.html', listPatients=patientListSql)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)