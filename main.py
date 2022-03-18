student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_of_heights = 0  
for height in student_heights:
    sum_of_heights += height
no_of_student = 0    
for student in student_heights:
    no_of_student += 1  
    
average = round(sum_of_heights / no_of_student)

print(average)




