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
