def hw(hw1,hw2,hw3,hw4,hw5,hw6,hw7,hw8,hw9,hw10,hw11):
    hw_list = [hw1,hw2,hw3,hw4,hw5,hw6,hw7,hw8,hw9,hw10,hw11]
    hw_list2 = []
    inv = []
    for x in hw_list:
        if x.isnumeric():
            x = float(x)
            if x <= 100:
                hw_list2.append(x)
            else:
                inv.append(x)
        elif x == '':
            pass
        else:
            inv.append(x)
    if len(hw_list2) > 0 and len(inv) == 0:
        hw_grade = (sum(hw_list2))/(len(hw_list2))
        return hw_grade
    elif len(inv) > 0:
        return -1
    else:
        return -2
    

def quiz(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10):
    quiz_list = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
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


def midterm(m1,m2,m3):
    midterm_list = [m1,m2,m3]
    midterm_list2 = []
    inv = []
    for x in midterm_list:
        if x.isnumeric():
            x = float(x)
            if x <= 100:
                midterm_list2.append(x)
            else:
                inv.append(x)
        elif x == '':
            pass
        else:
            inv.append(x)
    if len(midterm_list2) > 0 and len(inv) == 0:
        midterm_grade = (sum(midterm_list2))/(len(midterm_list2))
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
    
def grade(hw_result,q_result,m_result,f_result):
    if hw_result >= 0 or q_result >= 0 or m_result >= 0 or f_result >= 0:
        grade_list = [q_result,m_result,f_result]
        grade_list_a = []

        weight_list = [.1,.1,.5,.30]
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
    if 94 <= grade_average <= 100:
        return 'A'
    elif 90 <= grade_average < 94:
        return 'A-'
    elif 87 <= grade_average < 90:
        return 'B+'
    elif 84 <= grade_average < 87:
        return 'B'
    elif 80 <= grade_average < 84:
        return 'B-'
    elif 77 <= grade_average < 80:
        return 'C+'
    elif 74 <= grade_average < 77:
        return 'C'
    elif 70 <= grade_average < 74:
        return 'C-'
    elif 67 <= grade_average < 70:
        return 'D+'
    elif 64 <= grade_average < 67:
        return 'D'
    elif 60 <= grade_average < 64:
        return 'D-'
    elif grade_average < 60:
        return 'F'