class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student: {self.name}, Subject: {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return "Not enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name, "C", id)
            self.students.append(student)
            return f'{name} is enrolled with id:{id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print("--------- OUR Teachers----------")
        for teacher in self.teachers:
            print(teacher)
        print("---------OUR STUDENTS----------")
        for student in self.students:
            print(student)
        return 'All  done for now'


phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('Rani', 8000)
phitron.enroll('Sumi', 7000)


phitron.add_teacher('Tom Cruise', 'DS')
phitron.add_teacher('Tom Drtuei', 'Algorithm')
phitron.add_teacher('Rruise', 'DB')


print(phitron)
