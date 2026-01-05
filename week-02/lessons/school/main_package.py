from people import Student, Instructor, Person  # from package
from courses.learning import Course  # directly from module


def run():
    student = Student("Tedra Farrar", 12345)
    print(student.name)

    instructor = Instructor("Say Stopher", "Prof", "11-529-A")
    print(instructor.name)

    p = Person("Jobie Mapletoft")
    print(p.name)

    students = [
        Student("Katusha Barette", 87294),
        Student("Webb Drains", 273618),
        Student("Chance Olekhov", 12),
    ]

    instructors = [instructor]

    course = Course(
        "Demystifying the Hipster", students, instructors
    )  # Tufts University

    message = f"""{course.title}
{[s.name for s in course.students]}
{[i.name for i in course.instructors]}"""

    print(message)


if __name__ == "__main__":
    run()
