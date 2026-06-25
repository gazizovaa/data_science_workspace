l = ['Gulnaz', 17, True]
l.append(['Aydan', False])
print(l)

l.extend(['Aydan', False])
print(l)
l.pop(2)
print(l)

list = [10, 2, 3, 4, 17]
print(list)
#
list.sort(reverse=False)  # ascending order
print(list)
#
list.reverse()
# reversed(l)
sorted(list)
print(list)
#
# Dictionary
d = {'ad': 'Mina', 'yash': 23}
d['boy'] = 164
print(d['ad'])
print(d.keys())
print(d.values())

# user_input = input('Adinizi, soyadinizi ve yashinizi daxil edin: ')
# l = user_input.split(' ')
# print(f'Menim adim {l[0]} ve soyadim {l[1]}dir. {l[2]} yashim var.')
# d = {'ad': l[0], 'soyad': l[1], 'yash': int(l[2])}
# print(d)
#

user_input = input('Adinizi, soyadinizi ve yashinizi daxil edin: ').split(' ')
print(f'Menim adim {user_input[0]} ve soyadim {user_input[1]}dir. {user_input[2]} yashim var.')
d = {'ad': user_input[0], 'soyad': user_input[1], 'yash': int(user_input[2])}
print(d)

# Tuples
t = ('Gulare', 'Esmer', 32, '85')
print(t)

# conditionals
# create a calculator
oper = input('Toplama emeliyyatini yazin: ').split(' ')
# ['5', '+', '6']
if oper[1] == '+':
    print(int(oper[0]) + int(oper[2]))
elif oper[1] == '-':
    print(int(oper[0]) - int(oper[2]))
elif oper[1] == '*':
    print(int(oper[0]) * int(oper[2]))
elif oper[1] == '/':
    print(int(oper[0]) / int(oper[2]))
else:
    print('Bu operatoru tanimiram')

# a = 5
# if a == 3:
#     print(a*3)
# else:
#     print(a*2)

print('--------------------------------------------------------------------------')

# dictionary tasks
# task1
student = {'name': 'John', 'age': 20}
print(student)

# task2
student2 = {}
student2['name'] = 'Alice'
student2['age'] = 21
student2['grade'] = 'A'
student2['grade'] = 'A+'
print(student2)

# task3
given_person = {'name': 'Alice', 'age': 30, 'city': 'Seattle'}
print(given_person.keys())
print(given_person.values())

# task4
data = {'city': 'New York', 'population': 8000000}
if 'city' in data:
    print('Key exists')
else:
    print('Key does not exist')

# Basic Condition Tasks
# task1
user_input = int(input('bir eded daxil edin: '))
if user_input > 0:
    print('Positive')
elif user_input < 0:
    print('Negative')
else:
    print('Zero')

# task2
score = int(input('aldiginiz qiymeti daxil edin: '))
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
elif score < 60:
    print('F')
else:
    print('Invalid letter grade')

# task3
numbers = input('3 eded daxil edin:').split(' ')
max_numb = int(max(numbers))
print(max_numb)

# task4
eded = int(input('Bir eded daxil edin: '))
if eded % 2 == 0 and eded % 3 == 0:
    print('Divisible by 2 and 3')
elif eded % 2 == 0:
    print('Divisible by 2')
elif eded % 3 == 0:
    print('Divisible by 3')
else:
    print('Not divisible by 2 or 3')

# task5
eded2 = int(input('Bir eded daxil edin:'))
if eded2 % 2 == 0:
    print('Even')
else:
    print('Odd')

# task6
age_and_citzship = input('Yashinizi ve vetendasliq statusunuzu daxil edin: ').split(' ')
age = int(age_and_citzship[0])
citizenship_status = age_and_citzship[1]
if citizenship_status == 'Y' and age >= 18:
    print('Eligible to vote')
elif citizenship_status == 'Y' and age < 18:
    print('Too young to vote')
else:
    print('Not eligible to vote')
