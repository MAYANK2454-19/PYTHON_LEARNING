student_score = input("Enter the list of scores \n").split()
for i in range (0 , len(student_score)):
    student_score[i] = int(student_score[i])
print(student_score)
max = student_score[0]
for j in range (0, round(len(student_score))):
    if student_score[j]> max :
        max = student_score[j]
print(max)