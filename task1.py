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
@app.route('/inserttablevalues', methods = ['POST'])
def insert():
    if request.method =='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.mysqltable values(%s, %s)",(name, number))
        mydb.commit()
        return jsonify('sucessfully inserted')
@app.route('/updatetable', methods = ['POST'])
def update():
    if request.method=='POST':
        get_name =request.json['get_name']
        cursor.execute("update tasksql.mysqltable set number = number+500 where name=%s", (get_name,))
        mydb.commit()
        return jsonify('sucessfully updated')
@app.route('/deletetablevalues', methods = ['POST'])

def delete():
     if request.method=='POST':
        name_del =request.json['name_del']
        cursor.execute("delete from tasksql.mysqltable where name = %s ",(name_del,))
        mydb.commit()
        return jsonify('sucessfully updated')
     
@app.route('/fetchvalues', methods = ['POST','GET'])     
def fetch_data():
    cursor.execute("select * from tasksql.mysqltable")
    l =[]
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))




if __name__ =='__main__':
    app.run()
