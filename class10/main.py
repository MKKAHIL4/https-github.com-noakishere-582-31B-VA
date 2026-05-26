from student_record import StudentRecord
from course_section import Course_Section

#Student tests

print("----Valid Student tests----")

student1 = StudentRecord("alice", 3.5, 50)
student1.display_info()

student1.add__credits(2)
student1.update_gpa(3.9)
print("\n ---Student record After Updates:")
student1.display_info()
print("Academic Status: ",student1.academic_status)

print("\n ---Invalid Student Tests ---")
try:
    bad_student = StudentRecord("", 3.0, 10)
except ValueError as e:
        print("error", e)

try:
    student1.update_gpa(5.0)
except ValueError as e:
        print("error", e)
        
try:
    student1.add__credits(-5)
except ValueError as e:
        print("error", e)


#course test

course  = Course_Section("Physics 101", 2, 1, 0)

course.display_info()
print("\n registering students.....")

course.register_student()
course.display_info()

print("\n dropping a student ......")

course.drop_student()
course.display_info()

print("\n ====-----Invalid Course Test -----=====" )
try:
    bad_course = Course_Section("", 5)
except ValueError as e:
    print("Error:", e)

try:
    bad_course2 = Course_Section("Math", 0)
except ValueError as e:
    print("Error:", e)

course = Course_Section("Physics 101 ", 2, 0)

print("Initial state:")
course.display_info()
print("\n registering a student...")
course.register_student()

print("After 1st registration :")
course.display_info()

print("\n Registering another student")
course.register_student()

print("\n Registering a 2nd student ....")
course.display_info()
print("\n-- trying to overfill the course --- ")
try:
    course.register_student()
except ValueError as e:
    print("Error:", e)
    
# waitng list
print("\n ---------waiting list------------")
course.add_to_waitlist()
course.add_to_waitlist()

course.display_info()

course.remove_from_wailist()

print("\n After removing waitlist:")
course.display_info()
