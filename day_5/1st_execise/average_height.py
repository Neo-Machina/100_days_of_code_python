# You are going to write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
sum_heights = 0
count = 0
for height in student_heights:
    sum_heights += height
    count += 1
    
avg_heights = round(sum_heights / count)
    
print(avg_heights)