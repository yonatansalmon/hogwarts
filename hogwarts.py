import threading
import time
from flask import Flask, jsonify, render_template, request, redirect, url_for
from student_list import students, courses, magic_skills, days, months

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
        magic_skills = request.form.getlist('magic_skills[]')
        magic_skills = [{'skill': skill} for skill in magic_skills]
        level = request.form.getlist("lvl[]")
        for i in range(len(magic_skills)):
            magic_skills[i]["level"] = level[i]
        desired_skills = request.form.getlist('desired_skills[]')
        try:
            last_id = int(students_list[-1]["id"] + 1)
        except IndexError:
            last_id = 1
        students_list.append({"id": last_id,
                              "first_name": fname,
                              "last_name": lname,
                              "creation_time": time.ctime(),
                              "last_update": time.ctime(),
                              "existing_skills": magic_skills,
                              "desired_skills": desired_skills,
                              "course_interest": [course],
                              })
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
        fname = request.form.get('First_Name')
        lname = request.form.get('Last_Name')
        course = request.form.get('Course_Interest')
        magic_skills = request.form.getlist('magic_skills[]')
        magic_skills = [{'skill': skill} for skill in magic_skills]
        level = request.form.getlist("lvl[]")
        for i in range(len(magic_skills)):
            magic_skills[i]["level"] = level[i]
        desired_skills = request.form.getlist('desired_skills[]')
        student["first_name"] = fname
        student["last_name"] = lname
        student["course_interest"] = [course]
        student["last_update"] = time.ctime()
        student["existing_skills"] = magic_skills
        student["desired_skills"] = desired_skills
        return redirect('/')

@app.route("/student_stats", methods=["GET"])
def student_stats():
    student_list = students
    existing_skills = []
    desired_skills = []
    existing_list = []
    desired_list = []
    day_stats = []
    day_list = []
    month_stats = []
    month_list = []
    student = [student for student in student_list]
    for skill in student:
        eskills = skill["existing_skills"]
        dskills = skill["desired_skills"]
        for skill in eskills:
            student_skills = skill["skill"]
            existing_skills.append(student_skills)
        for skill in dskills:
            desired_skills.append(skill)
    for skill in magic_skills:
        count_existing = existing_skills.count(skill)
        if count_existing:
            existing_list.append({'y': count_existing, 'label': skill})
    for skill in magic_skills:
        count_desired = desired_skills.count(skill)
        if count_desired:
            desired_list.append({'y': count_desired, 'label': skill})
    for added in student:
        cday = added["creation_time"].split()[0]
        cmonth = added["creation_time"].split()[1]
        day_stats.append(cday)
        month_stats.append(cmonth)
    for current_day in days:
        count_day = day_stats.count(current_day)
        day_list.append({"y": count_day, "label": current_day})
    for current_month in months:
        count_month = month_stats.count(current_month)
        month_list.append({"y": count_month, "label": current_month})
    return render_template("student_stats.html", counts_existing=existing_list,
                           counts_desired=desired_list, counts_day=day_list, counts_month=month_list)

@app.route("/students/<int:id>/delete", methods=["GET"])
def delete_student(id):
    student_list = students
    student = [student for student in student_list if student['id'] == id]
    student_list.remove(student[0])
    return redirect('/')

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
