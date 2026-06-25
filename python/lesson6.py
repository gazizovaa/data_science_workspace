# while loop
a = 5
while a < 10:
    print('Salam')
    a = a + 1

while True:
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

# count = 1
# while count <= 3:
#     print("Hello Geek")
#     count += 1

# for loop
for i in {'1': 'Mina'}:
    print(i * 5)

a = '*'
for i in [1, 2, 3, 4, 5]:
    print(a * i)

print('---------------------------------------------')

b = 1
while b <= 5:
    print(b * '*')
    b = b + 1

while True:
    x = 1
    l = []
    while x <= 5:
        l.append(int(input('eded daxil edin: ')))
        x = x + 1
    print(f'Minimum number is: {min(l)}\tMaximum number is: {max(l)}')

x = 1
l = []
while x <= 5:
    l.append(int(input('5 eded daxil edin: ')))
    x = x + 1
print(l)
print(f'Minimum number is: {min(l)}\tMaximum number is: {max(l)}')

l = input('Bir metn daxil edin:')
l.reverse()
for i in l:
    print(i)
#
# # tasks
# task1
# fruits = ['apple', 'banana', 'cherry']
# for i in fruits:
#     print(i)
#
# # task2
# numbers_list = [1, 2,3, 4, 5]
# total_numbers = 0
# for i in numbers_list:
#     total_numbers = total_numbers + i
#     print(total_numbers)
#
# # task3
# list = []
# x = 0
# for i in input('Ededler daxil edin: ').split(' '):
#     list.append(int(i))
#     x = x + 1
# print(i)
#
# # task4
# input_string = input("Bir metn daxil edin: ")
# vowel_count = 0
# vowels = 'aeiouAEIOU'
#
# for char in input_string:
#     if char in vowels:
#         vowel_count += 1
#
# print("Number of vowels in the string:", vowel_count)
#
#
# # task5
# fact = 1
# i = 1
# numbers = int(input('Istenilen bir eded daxil edin: '))
# while i > 0:
#     fact = fact * i
#     print(fact)
#
#
# # task6
# count = 0
# items = ['apple', 'banana', 'apple', 'orange', 'apple']
# for i in items:
#     if i == 'apple':
#         count = count + 1
# print(count)
#
# # task7
# x = 1
# task7_list = []
# while x <= 10:
#     task7_list.append(int(input('Bir eded daxil edin:')))
#     x = x + 1
# print(max(task7_list))
# print(min(task7_list))
#
# task8
# limit = int(input('Enter a positive integer limit: '))
# sum_of_numbers = 0
# i = 2
# while i <= limit:
#     sum_of_numbers = sum_of_numbers + i
#     i = i + 2
# print(sum_of_numbers)
