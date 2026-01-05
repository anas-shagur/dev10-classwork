from people import Student, Instructor, Person  # from package
from courses.learning import Course  # directly from module


def print_person(person):
    if isinstance(person, Person):
        print("I'm a Person.")
    if isinstance(person, Student):
        print("I'm a Student.")
        print(f"Student ID: {person.student_id}")
    if isinstance(person, Instructor):
        print("I'm an Instructor.")
        print(f"Title: {person.title}")
        print(f"Employee ID: {person.employee_id}")
    print(f"My name is: {person.name}")


def run():
    person = Person("Jobie Mapletoft")
    student = Student("Bale Packmann", "100-A29-WER")
    instructor = Instructor("Letisha Pursey", "Dr.", "INS-COMPSCI-123")

    print_person(person)
    print_person(student)
    print_person(instructor)

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
