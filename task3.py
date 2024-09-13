from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)
mydb= conn.connect(
        host="localhost",
        user="root",
        password="Database@123"
    )
# created database and table in mysql workbench
cursor= mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS tasksql;")
cursor.execute("CREATE TABLE IF NOT EXISTS tasksql.mysqltable (name VARCHAR(30),number INT);")
@app.route('/inserttablevalues', methods = ['GET'])
def insert():
    if request.method =='GET':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.mysqltable values(%s, %s)",(name, number))
        mydb.commit()
        return jsonify('sucessfully inserted')