from flask import Blueprint, render_template, redirect, request, url_for
from markupsafe import escape

views = Blueprint(__name__,"views")

@views.route("/")
def index():
    return render_template('index.html')

@views.route('/EM-306', methods=['POST','GET'])
def EM306():
    from EM306web import quiz, midterm, final, grade, letter
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
    from M427Jweb import quiz, midterm, final, grade, letter
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
    
@views.route('/ME-316T', methods=['POST','GET'])
def ME316T():
    from ME316Tweb import hw, quiz, midterm, final, grade, letter
    if request.method == 'POST':
        hw1 = str(request.form["hw1"])
        hw2 = str(request.form["hw2"])
        hw3 = str(request.form["hw3"])
        hw4 = str(request.form["hw4"])
        hw5 = str(request.form["hw5"])
        hw6 = str(request.form["hw6"])
        hw7 = str(request.form["hw7"])
        hw8 = str(request.form["hw8"])
        hw9 = str(request.form["hw9"])
        hw10 = str(request.form["hw10"])
        hw11 = str(request.form["hw11"])

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

        hw_result = round(hw(hw1,hw2,hw3,hw4,hw5,hw6,hw7,hw8,hw9,hw10,hw11),2)
        q_result = round(quiz(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10),2)
        m_result = round(midterm(m1,m2,m3),2)
        f_result = round(final(f),2)

        invalid = 'Invalid input; only values between 0 and 100 are acceptable.'
        nga = 'No Grade Available.'

        grade_average = round(grade(hw_result,q_result, m_result, f_result),2)
        letter_grade = letter(grade_average)
        
        if hw_result == -1:
            hw_result = invalid
        elif hw_result == -2:
            hw_result = nga

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
        
        return render_template('ME-316T.html', hw_result_text=hw_result, q_result_text=q_result, m_result_text=m_result,grade_average_text=grade_average, letter_grade_text=letter_grade)
    else:
        return render_template('ME-316T.html')

@views.route('/HIS-315K', methods=['POST','GET'])
def HIS315K():
    from HIS315Kweb import lecture, quiz, writing, grade, letter
    if request.method == 'POST':
        w1 = str(request.form["w1"])
        w2 = str(request.form["w2"])
        w3 = str(request.form["w3"])
        w4 = str(request.form["w4"])
        w5 = str(request.form["w5"])
        w6 = str(request.form["w6"])
        w7 = str(request.form["w7"])
        w8 = str(request.form["w8"])
        w9 = str(request.form["w9"])
        w10 = str(request.form["w10"])
        w11 = str(request.form["w11"])
        w12 = str(request.form["w12"])
        w13 = str(request.form["w13"])
        w14 = str(request.form["w14"])

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
        
        wr1 = str(request.form["wr1"])
        wr2 = str(request.form["wr2"])
        wr3 = str(request.form["wr3"])

        l_result = round(quiz(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14),2)
        q_result = round(quiz(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12),2)
        wr_result = round(writing(wr1,wr2,wr3),2)

        invalid = 'Invalid input; only values between 0 and 100 are acceptable.'
        nga = 'No Grade Available.'

        grade_average = round(grade(l_result, q_result, wr_result),2)
        letter_grade = letter(grade_average)
        
        if q_result == -1:
            q_result = invalid
        elif q_result == -2:
            q_result = nga

        if m_result == -1:
            m_result = invalid
        elif m_result == -2:
            m_result = nga

        if wr_result == -1:
            wr_result = invalid
        elif wr_result == -2:
            wr_result = nga

        if l_result == q_result == wr_result == nga or l_result == q_result == wr_result == invalid:
            grade_average = letter_grade = nga
        
        return render_template('HIS-315K.html', l_result_text=l_result, q_result_text=q_result, wr_result_text=wr_result, grade_average_text=grade_average, letter_grade_text=letter_grade)
    else:
        return render_template('HIS-315K.html')

@views.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
       user = request.form["nm"]
       return redirect(url_for('user', usr=user))
    else:
       return render_template("login.html")