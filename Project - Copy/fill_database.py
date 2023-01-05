from flask import Flask, render_template, url_for, request, redirect
from app import db, Post, app
from datetime import datetime
import sqlite3 

app = Flask(__name__) 

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

conn = create_connection("database.db")

def create_table(conn, guest):
    sql= """ INSERT INTO guests(firstName,lastName,email,date,time)
                VALUES(?,?,?,?,?,?)"""
    c= conn.cursor()
    c.execute(sql,guest)
    return c.lastrowid

def main():
    database = r"database.db"

    sql_create_guest_table = """ CREATE TABLE IF NOT EXISTS guests (
                                        firstName text NOT NULL
                                        lastName...); """
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_guest_table)


# index for the html page
@app.route('/')
def index():
    return render_template("Appointment.html")    

@app.route('/post',method=['POST'])    
def post():
        if request.method == 'POST':
            c = conn.cursor()
            firsName=request.form.get('firsName')
            lastName=request.form.get('lastName')
            email=request.form.get('email')
            date=request.form.get('date')
            time=request.form.get('time')
            service=request.form.get('service')

            sql = ("INSERT INTO databasename.tablename (columnName,columnName,columnName,columnName,columnName,columnName Ci) VALUES (%s, %s, %s, %s, %s,%s)")
            c.execute(sql,(firsName,lastName,email,date,time,service))
            conn.commit()
            return redirect('/')


# This is where I run the app 
if __name__ == '__main__':
    app.run(debug=True)
            

with app.app_context():
    db.create_all()
