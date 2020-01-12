import threading
import time
import json

from flask import Flask, jsonify, render_template, request
from student_list import students

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_students():
    students_list = students

    return render_template('show_student.html', students_list=students_list)


@app.route('/add_student', methods=['POST', 'GET'])
def add_students():
    students_list = students
    if request.method == 'POST':
        fname = request.form.get('First_Name')
        lname = request.form.get('Last_Name')
        course = request.form.get('Creation_Time')
        students_list.append({"first_name": fname, "last_name": lname, "creation_time": course})
        return "student added"
    else:
        return render_template('add_student.html')


@app.route('/edit_student', methods=["GET"])
def edit_student():
    students_list = students
    return render_template("edit_student.html", students_list=students_list)


@app.route("/students/<int:id>", methods=['GET'])
def get_student(id):
    students_list = students
    student = [student for student in students_list if student['id'] == id]
    return render_template("student.html", student=student[0])


@app.route("/students/<int:id>/edit", methods=['GET', 'POST'])
def get_student2(id):
    students_list = students
    student = [student for student in students_list if student['id'] == id][0]
    if request.method == 'GET':
        return render_template('edit_student.html', student=student)
    elif request.method == 'POST':
        a = request.form.get('last_name')
        student['last_name'] = a
        return render_template('student.html', student=student)




if __name__ == "__main__":
    time.sleep(0.5)
    threading.Thread(target=app.run).start()




