from people import Student, Instructor  # from package
from courses.learning import Course  # from module
import console_io as cio  # from module
from console_io import read_int  # from module, explicit function


def run():
    instructor_name = cio.read_required_string("Instructor: ")
    employee_id = cio.read_required_string("Employee ID: ")
    title = cio.read_required_string("Honorary: ")
    instructor = Instructor(instructor_name, title, employee_id)

    students = []
    for _ in range(3):
        student_name = cio.read_required_string("Student: ")
        student_id = read_int("Student ID: ")
        student = Student(student_name, student_id)
        students.append(student)

    course_title = cio.read_required_string("Course Title: ")
    course = Course(course_title, students, [instructor])

    message = f"""{course.title}
{[s.name for s in course.students]}
{[i.name for i in course.instructors]}"""

    print(message)


if __name__ == "__main__":
    run()
