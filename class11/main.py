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
