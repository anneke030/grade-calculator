print("This is a grade calculator for the course ME 316T with Professor Hall in Fall 2024. Enter your grades for the assignments as follows. Please be sure to enter your grades on the 100-point scale for all assignments. For assignments not yet reached, press enter. Additionally, for assignments that have passed but will not count towards your final grade, please enter '-'.")

def hw():
    hws = []
    hw_num = list(range(1,12))
    hw_grade = 0
    n = 0 # for hw number labels
    hwn = 0 # for hw calculations

    # creating list of hw grades
    while n < len(hw_num):
        current_hw = input(f"Grade for Quiz #{hw_num[n]}: ")
        if current_hw.isnumeric():
            current_hw = float(current_hw)
            if 0 <= current_hw <= 100:
                hws.append(current_hw)
            else:
                print("The input is invalid. Please enter a grade value between 0 and 100.")
                n -= 1
                hwn -= 1
        elif current_hw == '':
            break
        elif current_hw == '-':
            qn-=1
        else:
            print("The input is invalid. Please enter a grade value between 0 and 100.")
            n -= 1
            hwn -= 1
        n+=1
        hwn+=1

    # hw grade calculation (stand-alone)
    if len(hws) > 0:
        hw_grade = (sum(hws))/(len(hws))
        print(f"Homework grade: {round(hw_grade,2)}")
        return hw_grade     
    else:
        print("No homework grade available.")  
        return -1

def quiz():
    quizzes = []
    quiz_num = list(range(1,11))
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
        midterm_grade = (sum(midterms))/(len(midterms))
        print(f"Midterm grade: {round(midterm_grade,2)}")
        return midterm_grade     
    else:
        print("No midterm grade available.")  
        return -1
    

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
            return -1
        else:
            print("The input is invalid. Please enter a grade value between 0 and 100.")
            n -= 1
        n += 1
    
# function to calculate weighted average of grade categories (hw, quiz, midterm, final)
def output():
    hw_grade = hw()
    quiz_grade = quiz()
    midterm_grade = midterm()
    final_grade = final()

    grade_list = [hw_grade, quiz_grade , midterm_grade , final_grade]
    grade_list_a = []

    weight_list = [.1,.1,.5,.3]
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
        if grade_total >= 94:
            print("Letter Grade: A")
        elif 90 <= grade_total < 94:
            print("Letter Grade: A-")
        elif 87 <= grade_total < 90:
            print("Letter Grade: B+")
        elif 84 <= grade_total < 87:
            print("Letter Grade: B")
        elif 80 <= grade_total < 84:
            print("Letter Grade: B-")
        elif 77 <= grade_total < 80:
            print("Letter Grade: C+")
        elif 74 <= grade_total < 77:
            print("Letter Grade: C")
        elif 70 <= grade_total < 74:
            print("Letter Grade: C-")
        elif 67 <= grade_total < 70:
            print("Letter Grade: D+")
        elif 64 <= grade_total < 67:
            print("Letter Grade: D")
        elif 60 <= grade_total < 64:
            print("Letter Grade: D-")
        elif grade_total < 60:
            print("Letter Grade: F")
    else:
        print("No total grade available.")

output()