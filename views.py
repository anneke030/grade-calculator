from flask import Blueprint, render_template, redirect, request, url_for
from EM306web import quiz, midterm, final, grade, letter
from M427Jweb import quiz, midterm, final, grade, letter
from markupsafe import escape

views = Blueprint(__name__,"views")

@views.route("/")
def index():
    return render_template('index.html')

@views.route('/EM-306', methods=['POST','GET'])
def EM306():
    if request.method == 'POST':
        q0 = str(request.form["q0"])
        q1 = str(request.form["q1"])
        q2 = str(request.form["q2"])
        q3 = str(request.form["q3"])
        q4 = str(request.form["q4"])
        q5 = str(request.form["q5"])
        q6 = str(request.form["q6"])
        q7 = str(request.form["q7"])
        q8 = str(request.form["q8"])
        q9 = str(request.form["q9"])
        q10 = str(request.form["q10"])
        q11 = str(request.form["q11"])
        q12 = str(request.form["q12"])
        q13 = str(request.form["q13"])
        
        m1 = str(request.form["m1"])
        m2 = str(request.form["m2"])
        m3 = str(request.form["m3"])

        f = str(request.form['f'])

        q_result = round(quiz(q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13),2)
        m_result = round(midterm(m1,m2,m3),2)
        f_result = round(final(f),2)

        invalid = 'Invalid input; only values between 0 and 100 are acceptable.'
        nga = 'No Grade Available.'

        grade_average = round(grade(q_result, m_result, f_result),2)
        letter_grade = letter(grade_average)
        
        if q_result == -1:
            q_result = invalid
        elif q_result == -2:
            q_result = nga

        if m_result == -1:
            m_result = invalid
        elif m_result == -2:
            m_result = nga

        if f_result == -1:
            f_result = invalid
        elif f_result == -2:
            f_result = nga

        if q_result == m_result == f_result == nga or q_result == m_result == f_result == invalid:
            grade_average = letter_grade = nga
        
        return render_template('EM-306.html', q_result_text=q_result, m_result_text=m_result,grade_average_text=grade_average, letter_grade_text=letter_grade)
    else:
        return render_template('EM-306.html')
    
@views.route('/M-427J', methods=['POST','GET'])
def M427J():
    if request.method == 'POST':
        q1 = str(request.form["q1"])
        q2 = str(request.form["q2"])
        q3 = str(request.form["q3"])
        q4 = str(request.form["q4"])
        q5 = str(request.form["q5"])
        q6 = str(request.form["q6"])
        q7 = str(request.form["q7"])
        q8 = str(request.form["q8"])
        q9 = str(request.form["q9"])
        q10 = str(request.form["q10"])
        
        m1 = str(request.form["m1"])
        m2 = str(request.form["m2"])
        m3 = str(request.form["m3"])

        f = str(request.form['f'])

        q_result = round(quiz(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10),2)
        m_result = round(midterm(m1,m2,m3),2)
        f_result = round(final(f),2)

        invalid = 'Invalid input; only values between 0 and 100 are acceptable.'
        nga = 'No Grade Available.'

        grade_average = round(grade(q_result, m_result, f_result),2)
        letter_grade = letter(grade_average)
        
        if q_result == -1:
            q_result = invalid
        elif q_result == -2:
            q_result = nga

        if m_result == -1:
            m_result = invalid
        elif m_result == -2:
            m_result = nga

        if f_result == -1:
            f_result = invalid
        elif f_result == -2:
            f_result = nga

        if q_result == m_result == f_result == nga or q_result == m_result == f_result == invalid:
            grade_average = letter_grade = nga
        
        return render_template('M-427J.html', q_result_text=q_result, m_result_text=m_result,grade_average_text=grade_average, letter_grade_text=letter_grade)
    else:
        return render_template('M-427J.html')

@views.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
       user = request.form["nm"]
       return redirect(url_for('user', usr=user))
    else:
       return render_template("login.html")