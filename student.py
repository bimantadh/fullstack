print("hello world!!")

name= "Ram"

print(name)

age=29

if age>20 and age<30 :
    print ("start thinking about future")

if age>20 or age<30 :
    print ("start thinking  about future again..")

# dictonary
student_1_info = {
	"name":"shyam",
	"age": 22
}
print(student_1_info)
print(student_1_info['age'])

student_2_info = {
	"name":"ram",
	"age": 23
}

students = [
	{"name": "ram", "age": 23, "marks":80},
	{"name": "shyam", "age": 22, "marks":50},
	{"name": "sita", "age": 20, "marks":85},
	{"name": "gita", "age": 21, "marks":25},
]
print(students)
print(len(students))

name_with_age_greater_than_20 = []
for student in students:
	if student['age'] > 20:
		print(student)
		name_with_age_greater_than_20.append(student)

print(name_with_age_greater_than_20)


# print student name who are passed
name_with_marks_greater_than_40 = []
for student in students :
     if student['marks'] > 40:
          print (student)
          name_with_marks_greater_than_40.append(student)
print(name_with_marks_greater_than_40)

# Write a function to add marks of all students
def total_marks(students):
        total=0
        for student in students:
            total = total + student["marks"]
            return total
print(total_marks(students))

# Write a function to get average mark of all students
def average_marks(students):
        average=0
        total= total_marks(students)
        average= total / len(students)
        return total
print(average_marks(students))

x = 1
y = 0
try:
	print ( x / y)
except Exception as ex:
	print("Error: ", ex)