print("This is a grade calculator for the course E M 306 with Professor Landis in Fall 2024. Enter your grades for the assignments as follows. Please be sure to enter your grades on the 100-point scale for all assignments. For assignments not yet reached, press enter. Additionally, for assignments that have passed but will not count towards your final grade, please enter '-'.")

def quiz():
    quizzes = []
    quiz_num = list(range(0,14))
    quiz_grade = 0
    n = 0 # for quiz number labels
    qn = 0 # for quiz calculations

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

    if len(quizzes) > 0:
        quiz_grade = (sum(quizzes))/(len(quizzes))
        print(f"Quiz grade: {round(quiz_grade,2)}")
        return quiz_grade     
    else:
        print("No quiz grade available.")  
        return 'n/a'
    

def midterm():
    midterms = []
    midterm_num = list(range(1,4))
    midterm_grade = 0
    n = 0 # for midterm number labels
    mn = 0 # for midterm calculations

    while n < len(midterm_num):
        current_m = input(f"Grade for Midterm #{midterm_num[n]}: ")

        if current_m.isnumeric():
            current_m = float(current_m)
            if 0 <= current_m <= 100:
                midterms.append(current_m)
            else:
                print("The input is invalid. Please enter a grade value between 0 and 100.")
                n -= 1
                mn -= 1
        elif current_m == '':
            break
        elif current_m == '-':
            mn-=1
        else:
            print("The input is invalid. Please enter a grade value between 0 and 100.")
            n -= 1
            mn -= 1
        n += 1
        mn += 1

    if len(midterms) > 0:
        midterms_sorted = list(reversed(sorted(midterms)))
        x = 0
        while True:
            midterm_grade = ((midterms_sorted[x])*.25)/.25
            x += 1
            if x == len(midterms_sorted):
                break
            midterm_grade = (midterm_grade*.25 + (midterms_sorted[x])*.2)/(.45)
            x += 1
            if x == len(midterms_sorted):
                break
            midterm_grade = (midterm_grade*.45 + (midterms_sorted[x])*.15)/.6
            x += 1
            if x == len(midterms_sorted):
                break
        
        print(f"Midterm grade: {round(midterm_grade,2)}")
        return midterm_grade
        
    else:
        print("No midterm grade available.")   
        return 'n/a'
    

def final():
    final_grade = 0
    n = 0
    while n == 0:
        final_grade = input("Final Exam Grade: ")
        if final_grade.isnumeric():
            final_grade = float(final_grade)
            if 0 <= final_grade <= 100:
                return final_grade
            else:
                print("The input is invalid. Please enter a grade value between 0 and 100.")
                n -= 1
        elif final_grade == '' or final_grade == '-':
            return 'n/a'
        else:
            print("The input is invalid. Please enter a grade value between 0 and 100.")
            n -= 1
        n += 1
    

def output():
    quiz_grade = quiz()
    midterm_grade = midterm()
    final_grade = final()
    grade_list = [quiz_grade , midterm_grade , final_grade]
    grade_list_a = []
    grade_total = 0

    weight_list = [.15,.6,.25]
    weight_list_a = []

    
    s = 0
    for x in grade_list:
        if grade_list[s] != 'n/a':
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
        print(f"Calculated Grade Average: {grade_total}")
    else:
        print("No total grade available.")

output()







