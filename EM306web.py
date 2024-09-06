def quiz(q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13):
    quiz_list = [q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
    quiz_list2 = []
    inv = []
    for x in quiz_list:
        if x.isnumeric():
            x = float(x)
            if x <= 100:
                quiz_list2.append(x)
            else:
                inv.append(x)
        elif x == '':
            pass
        else:
            inv.append(x)
    if len(quiz_list2) > 0 and len(inv) == 0:
        quiz_grade = (sum(quiz_list2))/(len(quiz_list2))
        return quiz_grade
    elif len(inv) > 0:
        return -1
    else:
        return -2

print(quiz('-1','1','1','1','1','1','1','1','1','1','1','1','1','1'))

def midterm(m1,m2,m3):
    midterm_list = [m1,m2,m3]
    midterms_sorted = []
    inv = []
    for x in midterm_list:
        if x.isnumeric():
            x = float(x)
            if x <= 100:
                midterms_sorted.append(x)
            else:
                inv.append(x)
        elif x == '':
            pass
        else:
            inv.append(x)

    # differential midterm grade calculations
    ## highest midterm score: 25% of overall grade
    ## middle midterm score: 20% of overall grade
    ## lowest midterm score: 15% of overall grade
    if len(midterms_sorted) > 0 and len(inv) == 0:
        midterms_sorted = list(reversed(sorted(midterms_sorted)))
        n = 0
        while True:
            midterm_grade = ((midterms_sorted[n])*.25)/.25
            n += 1
            if n == len(midterms_sorted):
                break
            midterm_grade = (midterm_grade*.25 + (midterms_sorted[n])*.2)/(.45)
            n += 1
            if n == len(midterms_sorted):
                break
            midterm_grade = (midterm_grade*.45 + (midterms_sorted[n])*.15)/.6
            n += 1
            if n == len(midterms_sorted):
                break
            return midterm_grade
    elif len(inv) > 0:
        return -1
    else:
        return -2



def final(f):
    if f.isnumeric():
        final_grade = float(f)
        if final_grade <= 100:
            return final_grade
        else:
            return -1
    elif f == '':
        return -2
    else:
        return -1
    
def grade(q_result,m_result,f_result):
    if q_result >= 0 or m_result >= 0 or f_result >= 0:
        grade_list = [q_result,m_result,f_result]
        grade_list_a = []

        weight_list = [.15,.6,.25]
        weight_list_a = []

        grade_total = 0
        
        s = 0
        for x in grade_list:
            if 0 <= grade_list[s] <= 100:
                grade_list_a.append(grade_list[s])
                weight_list_a.append(weight_list[s])
            else:
                pass
            s += 1

        n = 0
        if len(grade_list_a) != 0:
            grade_list_b = []
            weight_list_b = []
            while n < len(grade_list_a):
                grade_list_b.append((grade_list_a[n])*(weight_list_a[n]))
                weight_list_b.append(weight_list_a[n])
                n += 1

            grade_total = (sum(grade_list_b))/(sum(weight_list_b))
            return grade_total
        else:
            return -2
    else:
        return -2
    
def letter(grade_average):
    if 90 <= grade_average <= 100:
        return 'A'
    elif 80 <= grade_average < 90:
        return 'B'
    elif 65 <= grade_average < 80:
        return 'C'
    elif 50 <= grade_average < 65:
        return 'D'
    elif grade_average < 50:
        return 'F'

        
