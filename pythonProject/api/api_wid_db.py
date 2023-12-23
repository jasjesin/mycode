import sqlite3
from flask import Flask, jsonify, request
import json
from student_details import Student

app = Flask(__name__)


@app.get("/")
def home():
    c = sqlite3.connect("student.db").cursor()
    c.execute("CREATE TABLE IF NOT EXISTS STUDENTS("
              "'sid' TEXT, 'fn' TEXT, 'ln' TEXT, 'dept' TEXT)")
    c.connection.close()
    return 'Student API'


@app.get("/students")
def students():
    c = sqlite3.connect("student.db").cursor()
    c.execute("SELECT * from STUDENTS")
    data = c.fetchall()
    return jsonify(data)


@app.get("/students/<sid>")
def get_student_by_id(sid):
    c = sqlite3.connect("student.db").cursor()
    c.execute("SELECT * from STUDENTS where sid=?", (sid,))
    data = c.fetchone()
    return json.dumps(data)


@app.post("/addStudent")
def add_student():
    db = sqlite3.connect("student.db")
    c = db.cursor()
    data_recd = request.get_json()
    student = Student(data_recd['fn'],
                      data_recd['ln'],
                      data_recd['dept'])
    print(student)
    c.execute("INSERT INTO STUDENTS VALUES(?, ?, ?, ?)",
              (student.sid, student.fn, student.ln, student.dept))
    db.commit()
    data = c.lastrowid
    return json.dumps(data), 201


@app.put("/updateStudent/<sid>")
def update_student(sid):
    db = sqlite3.connect("student.db")
    c = db.cursor()
    data_recd = request.get_json()
    student = Student(data_recd['fn'],
                      data_recd['ln'],
                      data_recd['dept'])
    print(student)
    c.execute("UPDATE STUDENTS SET fn = ?, ln = ?, dept = ? where sid = ?",
              (student.fn, student.ln, student.dept, sid))
    db.commit()
    return json.dumps("Record successfully updated"), 201


@app.delete("/deleteStudent/<sid>")
def delete_student(sid):
    db = sqlite3.connect("student.db")
    c = db.cursor()
    c.execute("DELETE FROM STUDENTS where sid = ?", (sid,))
    db.commit()
    return json.dumps("Record successfully deleted."), 204


if __name__ == '__main__':
    app.run(port=8080, debug=True)
