    # Оценка работы лекторов
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Выведение основной информации о студенте
    def __str__(self):
        self.avg()
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.avg_grades}\n'
               f'Курсы в процессе изучения: 'f'{", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res


# Класс Mentor (лекторы и эксперты)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс Lecturer (лекторы)
class Lecturer(Mentor, BaseMethod):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grades = 0

    # Выведение основной информации о лекторе
    def __str__(self):
        self.avg()
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.avg_grades}')
        return res

# Класс Reviewer (эксперты)
class Reviewer(Mentor):
    # Оценка работы студентов
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Выведение основной информации об эксперте
    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}')
        return res