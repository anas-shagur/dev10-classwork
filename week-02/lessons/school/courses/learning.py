class Course:
    def __init__(self, title, students, instructors):
        self._title = title
        self._students = students
        self._instructors = instructors

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        self._students = students

    @property
    def instructors(self):
        return self._instructors

    @instructors.setter
    def instructors(self, instructors):
        self._instructors = instructors
