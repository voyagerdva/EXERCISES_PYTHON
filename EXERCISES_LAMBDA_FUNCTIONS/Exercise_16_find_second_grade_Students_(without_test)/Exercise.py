students = []
sec_name = []
second_low = 0

n = int(input("\n Input number of students: "))

for _ in range(n):
    s_name = input("Name: ")
    score = float(input("Grade: "))
    students.append([s_name, score])
    
print(f"\nNames and Grade of all students: {students}")

order = sorted(students, key=lambda x: int(x[1]))

for i in range(n):
    if order[i][1] != order[0][1]:
        second_low = order[i][1]
        break
        
print(f"\n Second lowes grade: {second_low}")

sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()

print("\n Names: ")
for s_name in sec_student_name:
    print(s_name)


    