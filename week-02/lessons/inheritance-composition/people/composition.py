class Person:
    def __init__(self, name, student_details=None, instructor_details=None):
        self._name = name
        # NEW CODE: composition
        self._student_details = student_details
        self._instructor_details = instructor_details

    @property
    def name(self):
        value = ""

        # am I an instructor?
        if self.instructor_details is not None:
            value += self.instructor_details.title + " "

        # plain old person
        value += self._name

        # am I a student?
        if self.student_details is not None:
            value += f", ID: {self.student_details.student_id}"

        return value

    @name.setter
    def name(self, name):
        self._name = name

    # NEW CODE
    @property
    def student_details(self):
        return self._student_details

    @student_details.setter
    def student_details(self, student_details):
        self._student_details = student_details

    @property
    def instructor_details(self):
        return self._instructor_details

    @instructor_details.setter
    def instructor_details(self, instructor_details):
        self._instructor_details = instructor_details


class StudentDetails:
    def __init__(self, student_id):
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id


class InstructorDetails:
    def __init__(self, title, employee_id):
        self._title = title
        self._employee_id = employee_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id


if __name__ == "__main__":
    p = Person("Jobie Mapletoft")

    s = Person("Bale Packmann")
    s.student_details = StudentDetails("100-A29-WER")

    i = Person("Letisha Pursey")
    i.instructor_details = InstructorDetails("Dr.", "INS-COMPSCI-123")

    both = Person("Pembroke Andrewartha")
    both.student_details = StudentDetails("245-GZ4-KLA")
    both.instructor_details = InstructorDetails("Prof.", "INS-LIT-532")

    print(p.name)
    print(s.name)
    print(i.name)
    print(both.name)
