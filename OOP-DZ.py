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