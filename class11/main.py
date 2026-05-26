from course import Course
from student import Student
from status import CourseStatus, DeliveryMode, StudentLevel

print("\n======Courses Test MAIN ======")
print("\n")

course4 = Course("Physics 104 ", 40, CourseStatus.OPEN, DeliveryMode.ONLINE)
course4.display_info() 
course5 = Course("Physics 105 ", 50, CourseStatus.CANCELED, DeliveryMode.IN_PERSON)
course5.display_info() 
course6 = Course("Physics 106 ", 60, CourseStatus.CLOSED, DeliveryMode.HYBRID)
course6.display_info() 

print("\n ====Course ACTIONS======")
course4.close_registration()
course4.display_info()

try:
    course5.reopen_course()
    print("Course5 responded successfully")
except ValueError as e:
    print("Course 5 Error :", e)

course5.display_info()

print("\n ===CHECK OPEN STATUS ============")
course7 = Course("Physics 107 ", 10, CourseStatus.OPEN, DeliveryMode.ONLINE)
course7.display_info() 
course8 = Course("Physics 105 ", 20, CourseStatus.CANCELED, DeliveryMode.IN_PERSON)
course8.display_info() 
print("Course4 open?", course7.is_open_for_registration())
print("Course5 open?", course8.is_open_for_registration())

print("\n ========TESTING Student in main ========")
        
student4 = Student("steff", StudentLevel.BEGINNER)
student4.display_info()
student5 = Student("Sarah", StudentLevel.INTERMEDIATE)
student5.display_info()
student7 = Student("Jennifer", StudentLevel.ADVANCED)
student7.display_info()

print("\n=======rorr Testing in Main ==============")
#INVALID COURSE (string instead of enum)
try:
    bad_course = Course("Bad Course", 20, "open", DeliveryMode.ONLINE)
except ValueError as e:
    print("Course Erorr: ", e)

#INVALID STUDENT (string instead of enum)
try:
    bad_student = Student("Stephanie", "expert") 
except ValueError as e:
    print("Course Erorr: ", e)
    
#INVALID REOPEN (cancled course)
print("\n ============CANCLED COURSE TEST=============   ")

course9 = Course("Chemistry", 40, CourseStatus.CANCELED, DeliveryMode.IN_PERSON)
course9.display_info()

try:
    course9.reopen_course()
    print("Course reopened Successfully.")
except ValueError as e:
    print("Course 9 Erorr: ", e)

course9.display_info()

#a tets to undertsnad opening and closing the course

print("\n ===re-opening and closing a course test for better undertsanding=== \n")
print("===Opening the course===")
course10 = Course("Math", 30, CourseStatus.OPEN, DeliveryMode.ONLINE)
course10.display_info()

print("\n ===Closing Course====\n")
course10.close_registration()
course10.display_info()

print("\n ====reopning the course====\n")
course10.reopen_course()
course10.display_info()


