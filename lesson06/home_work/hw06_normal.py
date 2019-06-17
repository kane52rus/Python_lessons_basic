# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, teachers, students):
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                }


class People:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    @property
    def get_short_name(self):
        return f"{self.last_name} {self.first_name[0]}.{self.middle_name[0]}."



class Student(People):
    def __init__(self, first_name, middle_name, last_name, class_room, mother, father):
        People.__init__(self, first_name, middle_name, last_name)
        self._class_room = class_room
        self._parents = {
            'mother': mother,
            'father': father
        }
    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents

class Teacher(People):
    def __init__(self, first_name, middle_name, last_name, courses, classes):
        People.__init__(self, first_name, middle_name, last_name)
        self._courses = courses
        self._classes = classes
    @property
    def get_courses(self):
        return self._courses
    @property
    def get_classes(self):
        return self._classes


teachers = [
    Teacher('Lotov', 'Lil', 'Arty', 'Java',
            ['1J', '2J', '1P']),
    Teacher('Belkin', 'Vi', 'Va', 'Python',
            ['1P', '2P', '2J'])]


students = [
    Student('Lol', 'lili', 'lulu', '1P', 'lol О. А.', 'lol А. В.'),
    Student('Patter', 'pa', 'Ki', '1P', 'patter Т.В.', 'Patter А.В.'),
    Student('Mor', 'Mar', 'Mir', '1P', 'Mor А.E.', 'Mor С.А.'),
    Student('Ass', 'Oss', 'Iss', '1P', 'Ass А.К.', 'Ass Н.В.'),
    Student('Bob', 'Arr', 'Ass', '1P', 'Bob В.А.', 'Bob А.Т'),
    Student('Nikkk', 'No', 'Yes', '1P', 'Nikkk Н.А.', 'Nikk Н.С.'),
    Student('Mikky', 'No', 'Lal', '1J', 'Nikkk Н.А.', 'Nikk Н.С.')]

school = School(teachers, students)

print('\nClasses list:')
print(', '.join(school.get_all_classes()))

print('\nList "1J" class:')
print('\n'.join(school.get_students('1J')))

student = school.find_student('Nikkk No Yes')
print('\nStudent: {0}\nClass: "{1}"\n''Teacher: {2}\nSubject: {3}'.format(student['full_name'],
student['class_room'], ', '.join(student['teachers']), ', '.join(student['lessons'])))

print('Parents: {0}, {1}'.format(student['parents']['mother'], student['parents']['father']))

print('\nClass: "1J"\nTeacher: ''{0}'.format(', '.join(school.get_teachers('1J'))))




