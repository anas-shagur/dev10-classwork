from .person import Person


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id


class Instructor(Person):
    def __init__(self, name, title, employee_id):
        super().__init__(name)
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
