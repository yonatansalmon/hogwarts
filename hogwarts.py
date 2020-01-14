import threading
import time
from flask import Flask, jsonify, render_template, request, redirect, url_for
from student_list import students, courses


count = 5

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_students():
    students_list = students
    return render_template('show_student.html', students_list=students_list)


@app.route('/add_student', methods=['POST', 'GET'])
def add_students():
    students_list = students
    courses_list = courses
    if request.method == 'POST':
        fname = request.form.get('First_Name')
        lname = request.form.get('Last_Name')
        course = request.form.get('Course_Interest')
        magic_skillz = request.form.getlist('Magic_skillz[]')
        desired_skillz = request.form.getlist('Desired_skillz[]')
        last_id = str(int(students_list[-1]["id"]) + 1)
        students_list.append({"id": last_id, "first_name": fname, "last_name": lname, \
                              "creation_time": time.ctime(), "last_update": time.ctime(), \
                              "existing_skills": magic_skillz, "desired_skills": desired_skillz,
                              "course_interest": [course], })
        return redirect('/')
    else:
        return render_template('add_student.html', courses_list=courses_list)


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
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        cinterest = request.form.get('course_interest')
        cinterest_split = cinterest.split(",")
        dskills = request.form.get('desired_skills')
        dskills_split = dskills.split(",")
        eskills = request.form.get('existing_skills')
        eskills_split = eskills.split(",")
        student['first_name'] = fname
        student['last_name'] = lname
        student['course_interest'] = cinterest_split
        student['desired_skills'] = dskills_split
        student['desired_skills'] = eskills_split
        return render_template('student.html', student=student)


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    time.sleep(0.5)
    threading.Thread(target=app.run).start()
