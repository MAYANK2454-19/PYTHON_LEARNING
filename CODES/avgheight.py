students_height=input("Enter heights of the students : \n").split()
print("List of strings : ")
print(students_height)
#initialise variables for sum , average and no. of elements in the list
sum = 0
avg = 0
elements = 0

#length of list 
for i in  (students_height):
    
        elements +=1

for n in range(0,elements):
    students_height[n]=int(students_height[n])
print("List of integers : ")
print(students_height)


#sum of list
for j in range (0,elements):
    sum +=students_height[j]
     
# avg of list 
avg = round(sum / elements)
print("Average of given heights :")
print(avg)