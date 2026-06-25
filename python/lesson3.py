# carriage return - overlapping
t = "alma\rarmud"
print(t)

print("hsf" * 5)

print('*' + '\n' + '*' * 2 + '\n' + '*' * 3 + '\n' + '*' * 4 + '\n' + '*' * 5)

# String methods
a = 'alma'
print(a.upper())
print(a.lower())
print(a.capitalize())
print(len('dsgj. kdj'))
print(a.replace('m', 'n'))
print('kitab'.find('a'))
print('kitabsfa'.rfind('a'))
print('a' in 'kitab')
print('A' in 'kitab'.upper())

# user input
a = input("Bir soz daxil edin:")
print(a)

print('alma'.index('a'))

# print('defter'[start, stop, step])
print('defter'[2:4])
print('defter'[1:4:2])
print('defter'[:4:2])
print('defter'[:4:-1])
print('defter'[-1:4:-1])

# find a reverse of your name
name = input("Adinizi daxil edin:")
print(name[::-1])

a = input("Neche almam var:")
b = input("Neche armudum var?")
print('Menim {} almam ve {} armudum var.'.format(a, b))
print(f'Menim {a} almam ve {b} armudum var.')

name = input("Adinizi daxil edin:")
age = input("Yashinizi daxil edin:")
print(f'Menim adim {name} ve {age} yashim var. Adimda {len(name)} herf var.')

c = 5
d = 'alma'
print(str(c) + d)
print(float(c))

print('alma'.count('a'))

print(input('Bir eded daxil edin:').count('5'))

random_numb = input("Bir reqem daxil edin:")
print(int(random_numb) + int(random_numb * 2) + int(random_numb * 3))

# task1
name = input("Enter your first name:")
print(name[0] + name[len(name) // 2] + name[-1])

# task2
str1 = "JhonDipPeta"
middle_three = str1[len(str1) // 2 - 1: len(str1) // 2 + 2]
print(middle_three)

# task3
first_numb = int(input("Enter your first number:"))
second_numb = int(input("Enter your second number:"))
print(first_numb * second_numb)

# task4
print("my", "name", "Gulnara", sep="**")

# task5
s1 = "America"
s2 = "Japan"
print(s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1])
