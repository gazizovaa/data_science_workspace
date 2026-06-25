# OOP
# number_of_students = 0
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Student created')
#         global number_of_students
#         number_of_students += 1
#         print('The number of students:' {number_of_students})
#
#     def about(self, car_color):
#         self.color = self.car_color(student1)
#         return f'Name: {self.name} and age: {self.age}'
#
#
# student1 = Student('Gulnara', 23)
# student2 = Student('Asmar', 20)
#
# # print(student1.name)
# # print(f'Name: {student1.name} and age: {student1.age}')
# #
# print(student1.about('Yashil'))
# Student.about(student2, 'Qara')
import charset_normalizer.constant

number_of_students = 0


class Student:
    global number_of_students
    grades = []

    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        Student.number_of_students += 1
        Student.grades.append(grade)

    def calc_avg_grade(self):
        return sum(Student.grades) / Student.number_of_students


student_1 = Student('Gulnara', 'Azizova', 100)
student_2 = Student('Samir', 'Orujov', 90)
student_3 = Student('Elnur', 'Aliyev', 75)

print(Student.calc_avg_grade(student_1))

global have_balance


class Bank:
    have_balance = 0

    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance
        Bank.have_balance += 1

    def mexaric(self, miqdar):
        if self.balance >= miqdar:
            self.balance -= miqdar
        else:
            print('There is no enough in balance')

    def medaxil(self, miqdar):
        # miqdar is not an attribute of an object
        self.balance += miqdar
        return self.balance

    def show_balance(self):
        return self.balance


x1 = Bank(34578, 'Javidan')
x2 = Bank(25678, 'Asmar')
Bank.medaxil(x1, str(1000))
Bank.show_balance(x2)
Bank.medaxil(x2, str(2000))


# tasks
# calculator
class Calculator:
    def __init__(self):
        print('Calculator is ready!')

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return 'Error: Division by Zero'
        return a / b


calculator = Calculator()
print(calculator.add(32, 8))
print(calculator.subtract(32, 8))
print(calculator.multiply(32, 8))
print(calculator.divide(32, 8))


# password
class Password:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if (self.length_of_characters() and
                self.have_uppercase_letter() and
                self.have_lower_letter() and
                self.contains_digit() and
                self.contain_special_character()):
            return 'Password is valid!'
        else:
            return self.get_invalid_requirements()

    def length_of_characters(self):
        return len(self.password) >= 8

    def have_uppercase_letter(self):
        for char in self.password:
            if char.isupper():
                return True
        return False

    def have_lower_letter(self):
        for char in self.password:
            if char.islower():
                return True
        return False

    def contains_digit(self):
        for char in self.password:
            if char.isdigit():
                return True
        return False

    def contain_special_character(self):
        special_chars = ['@', '#', '$', '%', '&', '!', '?', '.', ',', ':', ';']
        for char in self.password:
            if char in special_chars:
                return True
        return False

    def get_invalid_requirements(self):
        invalid_requirements = []
        if not self.length_of_characters():
            invalid_requirements.append("Password must be at least 8 characters long.")
        if not self.have_uppercase_letter():
            invalid_requirements.append("Password must contain at least one uppercase letter.")
        if not self.have_lower_letter():
            invalid_requirements.append("Password must contain at least one lowercase letter.")
        if not self.contains_digit():
            invalid_requirements.append("Password must contain at least one digit.")
        if not self.contain_special_character():
            invalid_requirements.append("Password must contain at least one special character.")

        return '\n'.join(invalid_requirements)


given_password = 'Aziz#213'
validator = Password(given_password)
result = validator.validate()
print(result)


