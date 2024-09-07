class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Имя: {self.fullname} Возраст: {self.age} Женат/Не женат: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_rating(self):
        print(f'Средняя оценка: {round(sum(self.marks.values()) / len(self.marks), 2)}')


class Teacher(Person):
    base_salary = 2000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def bonus(self):
        while self.experience > 3:
            self.base_salary += self.base_salary * 0.05
            self.experience -= 1
        print(f'Зарплата: {self.base_salary}')


math_teacher = Teacher('Айгул', 30, 'женат',  5)
math_teacher.introduce_myself()
math_teacher.bonus()


def create_students():
    student_1 = Student('Асылбек', '16', 'не женат', {'Математика': 4, 'География': 5, 'Химия': 3})
    student_2 = Student('Макс', 18, 'не женат', {'Математика': 5, 'География': 5, 'Химия': 4})
    student_3 = Student('Канат', 23, 'женат', {'Математика': 5, 'География': 5, 'Химия': 5})
    return [student_1, student_2, student_3]


students = create_students()
for i in students:
    i.introduce_myself()
    print(i.marks)
    i.average_rating()