n=int(input())                                                      #Number of subjects
total_score=0
total_credit_points=0
for i in range(n):
    grade=input()                                                   #get the grade from the user
    credit_points=int(input())                                      #get the credit points from the user
    total_credit_points=(total_credit_points)+(credit_points)       #to calculate the sum of credit points
    if(grade=="O"):
        grade_points=10
    elif(grade=="A+"):
        grade_points=9
    elif(grade=="A"):
        grade_points=8
    elif(grade=="B+"):
        grade_points=7
    elif(grade=="B"):
        grade_points=6
    else:
        grade_points=0
    sub_score=grade_points*credit_points        
    total_score=sub_score+total_score
cgpa=total_score/total_credit_points
print(cgpa)
