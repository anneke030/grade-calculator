def lecture(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14):
    lecture_list = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14]
    lecture_list2 = []
    inv = []
    for x in lecture_list:
        if x.isnumeric():
            x = float(x)
            if x <= 100:
                lecture_list2.append(x)
            else:
                inv.append(x)
        elif x == '':
            pass
        else:
            inv.append(x)
    if len(lecture_list2) > 0 and len(inv) == 0:
        lecture_grade = (sum(lecture_list2))/(len(lecture_list2))
        return lecture_grade
    elif len(inv) > 0:
        return -1
    else:
        return -2


def quiz(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12):
    quiz_list = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
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



def writing(wr1,wr2,wr3):
    writing_list = [wr1,wr2,wr3]
    writing_list2 = []
    inv = []
    for x in writing_list:
        if x.isnumeric():
            x = float(x)
            if x <= 100:
                writing_list2.append(x)
            else:
                inv.append(x)
        elif x == '':
            pass
        else:
            inv.append(x)
    if len(writing_list2) > 0 and len(inv) == 0:
        writing_grade = (sum(writing_list2))/(len(writing_list2))
        return writing_grade
    elif len(inv) > 0:
        return -1
    else:
        return -2
    
def grade(l_result,q_result,wr_result):
    if l_result >= 0 or q_result >= 0 or wr_result >= 0:
        grade_list = [l_result,q_result,wr_result]
        grade_list_a = []

        weight_list = [.35,.35,.3]
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
    elif 70 <= grade_average < 80:
        return 'C'
    elif 60 <= grade_average < 70:
        return 'D'
    elif grade_average < 60:
        return 'F'