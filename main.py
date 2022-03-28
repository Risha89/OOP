class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя : {self.name}\nФамилия : {self.surname}' \
               f'\nСредняя оценка за домашние задания : {srs(self.grades)}' \
               f'\nКурсы в процессе изучения : {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {self.finished_courses}'

    def grades_for_lectur(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            if course in lectur.grades:
                lectur.grades[course] += [grade]

            elif course not in lectur.grades:
                lectur.grades[course] = [grade]
        elif course not in self.courses_in_progress:
            print('Студент не является слушателем курса {}'.format(course))
        else:
            print('Ошибка. Лектор не читает курс {}!'.format(course))
    def __lt__(self, other):
        var = srs(self.grades) > srs(other.grades)
        return var

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.courses_in_progress:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    def __str__(self):

        return f'Имя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за лекции: {srl(self.grades)}  '
    def __lt__(self, other):
        var = srl(self.grades) > srl(other.grades)
        return var

class Reviewer(Mentor):
    def __init__(self, name, surname,):
        super().__init__(name, surname)
        self.courses_attached = []

    def vo(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress\
                and course not in student.finished_courses:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('ОшибкаAAA')
    def __str__(self):
        return f'Имя : {self.name}\nФамилия : {self.surname}'


student1 = Student('R', 'S', 'male')
student1.courses_in_progress += ['Math']
student1.courses_in_progress += ['IT']
student1.finished_courses = 'Введение в программирование'
student3 = Student('A', 'A', 'male')
student3.courses_in_progress += ['Math']
student3.courses_in_progress += ['IT']
student3.finished_courses = 'Введение в программирование'
student2 = Student('P', 'Sabirova', 'female')
student2.courses_in_progress += ['Chemistry']
student2.courses_in_progress += ['Ecology']
student2.finished_courses = 'Введение в обществознание'
reviewer1 = Reviewer('Ivan', 'Ivanov')
reviewer1.courses_attached += ['Math', 'IT']
reviewer1.vo(student1, 'Math', 7)
reviewer1.vo(student1, 'Math', 5)
reviewer1.vo(student1, 'IT', 6)
reviewer1.vo(student1, 'IT', 8)
reviewer1.vo(student3, 'Math', 4)
reviewer1.vo(student3, 'Math', 3)
reviewer1.vo(student3, 'IT', 2)
reviewer1.vo(student3, 'IT', 1)
reviewer2 = Reviewer('Karl', 'Smith')
reviewer2.courses_attached += ['Chemistry', 'Ecology']
reviewer2.vo(student2, 'Chemistry', 7)
reviewer2.vo(student2, 'Chemistry', 9)
reviewer2.vo(student2, 'Ecology', 6)
reviewer2.vo(student2, 'Ecology', 5)
lectur1 = Lecturer('Anton', 'Big')
lectur1.courses_attached += ['Math', 'IT']
lectur2 = Lecturer('Tony', 'Howk')
lectur2.courses_attached += ['Chemistry', 'Ecology']
student1.grades_for_lectur(lectur1, 'Math', 10)
student1.grades_for_lectur(lectur1, 'Math', 4)
student1.grades_for_lectur(lectur1, 'IT', 8)
student1.grades_for_lectur(lectur1, 'IT', 7)
student2.grades_for_lectur(lectur2, 'Chemistry', 10)
student2.grades_for_lectur(lectur2, 'Chemistry', 8)
student2.grades_for_lectur(lectur2, 'Ecology', 8)
student2.grades_for_lectur(lectur2, 'Ecology', 7)

def srl(grades):
    a = 0
    c = 0
    for el in grades:
        a += sum(grades[el])
        c += len(grades[el])
    return a/c


def srs(grades):
    a = 0
    b = 0
    for el in grades:
        a += sum(grades[el])
        b += len(grades[el])
    return a/b

print(student1)
print(student2)
print(lectur1)
print(lectur2)
print(reviewer1)
print(reviewer2)

print(srl(lectur1.grades))
print(srl(lectur2.grades))
print(srl(lectur1.grades)<srl(lectur2.grades))

print(srs(student1.grades))
print(srs(student2.grades))
print(srs(student1.grades)>srs(student2.grades))
sl = [student1, student2, student3]
ll = [lectur1, lectur2]

def average_of_students(science, students_list):
    st = 0
    sr_oc = 0
    for el in students_list:
        if science in el.grades:
            st += 1
            a = sum(el.grades[science])
            b = len(el.grades[science])
            sr_oc += (a/b)
    print(f'Средняя оценка студентов по предмету {science} = {sr_oc/st}')

average_of_students('Math', sl)

def average_of_lecturs(science, lecturs_list):
    st = 0
    sr_oc = 0
    for el in lecturs_list:
        if science in el.grades:
            st += 1
            a = sum(el.grades[science])
            b = len(el.grades[science])
            sr_oc += (a/b)
    print(f'Средняя оценка лекторов за лекции по предмету {science} = {sr_oc/st}')

average_of_lecturs('Chemistry', ll)