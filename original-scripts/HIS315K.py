print("This is a grade calculator for the course M 427J with Professor Lomeli in Fall 2024. Enter your grades for the assignments as follows. Please be sure to enter your grades on the 100-point scale for all assignments. For assignments not yet reached, press enter. Additionally, for assignments that have passed but will not count towards your final grade, please enter '-'.")

def lecture():
    lectures = []
    week_num = list(range(1,15))
    lecture_grade = 0
    n = 0 # for week number labels
    wn = 0 # for weekly calculations

    # creating list of weekly grades
    while n < len(week_num):
        current_w = input(f"Grade for Quiz #{week_num[n]}: ")
        if current_w.isnumeric():
            current_w = float(current_w)
            if 0 <= current_w <= 100:
                lectures.append(current_w)
            else:
                print("The input is invalid. Please enter a grade value between 0 and 100.")
                n -= 1
                wn -= 1
        elif current_w == '':
            break
        elif current_w == '-':
            wn-=1
        else:
            print("The input is invalid. Please enter a grade value between 0 and 100.")
            n -= 1
            wn -= 1
        n+=1
        wn+=1

    # lecture grade calculation (stand-alone)
    if len(lectures) > 0:
        lecture_grade = (sum(lectures))/(len(lectures))
        print(f"Lecture grade: {round(lecture_grade,2)}")
        return lecture_grade     
    else:
        print("No lecture grade available.")  
        return -1


def quiz():
    quizzes = []
    quiz_num = list(range(1,13))
    quiz_grade = 0
    n = 0 # for quiz number labels
    qn = 0 # for quiz calculations

    # creating list of quiz grades
    while n < len(quiz_num):
        current_q = input(f"Grade for Quiz #{quiz_num[n]}: ")
        if current_q.isnumeric():
            current_q = float(current_q)
            if 0 <= current_q <= 100:
                quizzes.append(current_q)
            else:
                print("The input is invalid. Please enter a grade value between 0 and 100.")
                n -= 1
                qn -= 1
        elif current_q == '':
            break
        elif current_q == '-':
            qn-=1
        else:
            print("The input is invalid. Please enter a grade value between 0 and 100.")
            n -= 1
            qn -= 1
        n+=1
        qn+=1

    # quiz grade calculation (stand-alone)
    if len(quizzes) > 0:
        quiz_grade = (sum(quizzes))/(len(quizzes))
        print(f"Quiz grade: {round(quiz_grade,2)}")
        return quiz_grade     
    else:
        print("No quiz grade available.")  
        return -1
    

def writing():
    writings = []
    writing_num = list(range(1,4))
    writing_grade = 0
    n = 0 # for writing number labels
    wrn = 0 # for writing calculations

    while n < len(writing_num):
        current_m = input(f"Grade for writing #{writing_num[n]}: ")

        if current_m.isnumeric():
            current_m = float(current_m)
            if 0 <= current_m <= 100:
                writings.append(current_m)
            else:
                print("The input is invalid. Please enter a grade value between 0 and 100.")
                n -= 1
                wrn -= 1
        elif current_m == '':
            break
        elif current_m == '-':
            wrn-=1
        else:
            print("The input is invalid. Please enter a grade value between 0 and 100.")
            n -= 1
            wrn -= 1
        n += 1
        wrn += 1

    if len(writings) > 0:
        writing_grade = (sum(writings))/(len(writings))
        print(f"writing grade: {round(writing_grade,2)}")
        return writing_grade     
    else:
        print("No writing grade available.")  
        return -1
    
    
# function to calculate weighted average of grade categories (lecture, quiz, writing)
def output():
    lecture_grade = lecture()
    quiz_grade = quiz()
    writing_grade = writing()

    grade_list = [lecture_grade, quiz_grade , writing_grade]
    grade_list_a = []

    weight_list = [.35,.35,.3]
    weight_list_a = []

    grade_total = 0
    
    s = 0
    for x in grade_list:
        if grade_list[s] != -1:
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
        print(f"Calculated Grade Average: {round(grade_total, 2)}")
        if grade_total >= 90:
            print("Letter Grade: A")
        elif 80 <= grade_total < 90:
            print("Letter Grade: B")
        elif 70 <= grade_total < 80:
            print("Letter Grade: C")
        elif 60 <= grade_total < 70:
            print("Letter Grade: D")
        elif grade_total < 60:
            print("Letter Grade: F")
        return grade_total
    else:
        print("No total grade available.")

output()