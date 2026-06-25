# Review
a = '*'
print(f'{a}\n{a*2}\n{a*3}\n{a*4}\n{a*5}')
print('---------------------------------')
print('{0}\n{1}\n{2}\n{3}\n{4}'.format(a, a*2, a*3, a*4, a*5))
# print('{}\n{}\n{}\n{}\n{}'.format(a, a*2, a*3, a*4, a*5))
print('---------------------------------')
print('{0}\n{0}{0}\n{0}{0}{0}\n{0}{0}{0}{0}\n{0}{0}{0}{0}{0}'.format(a))

print('kitab evi'[-6:0:-1])
print('kitab evi'[-6:-7:-1])

# List
l = [12, 0, 'Mina', True, [1, 2, 'alma']]
print(len(l))
print(l[2])
print(type(l[2][0]))
print(l[4][2][-1])
print(l[4][2].rfind('a'))

# List methods
l.append('Javidan')
print(l)
l[4].append('Javidan')
print(l)

l.append(['Javidan', 'Aytakin'])
print(l)

l.insert(1, 'Dayanat')
print(l)

l[3] = 'Gulnara'
print(l)
#
# name = 'Narmin'
# name[2] = 'z'
# print(name)

l.append('Aytaj')
print(l)

l.extend(['Aytaj', 'Sheyla'])
print(l)

l.remove(['Javidan', 'Aytakin'])
print(l)

l[5].remove('Javidan')
print(l)

l.append('Gulnara')
print(l)

del l[10]
print(l)

l.pop()
print(l.pop())

print(l.remove(True))

l.pop()
print(l.pop())
print(l)

print(12 in l)

x = '+994 51-738-17-33'
x = x.replace('-', ' ')
print(x)

x_list = x.split('-')
print(x_list)

x = '-'.join(x_list)
print(x)

name_age = input("Adinizi ve yashinizi boshluqla ayrilmish shekilde daxil edin: ")
l = name_age.split(' ')
print(f'Menim adim {l[0]}dir. Menim {l[1]} yashim var.')

# task1
t1_list = [1, 2, 3]
t1_list.append(4)
print(t1_list)

# task2
t2_list = ["apple", "banana", "cherry"]
t2_list.insert(1, "orange")
print(t2_list)

# task3
t3_list = ["apple", "banana", "cherry"]
t3_list.remove("banana")
print(t3_list)

# task4
t4_list = [1, 2, 3, 4, 5]
t4_list.pop()
print(t4_list)

# task5
t5_list = ["apple", "banana", "cherry"]
print(t5_list.index("cherry"))

# task6
t6_list = ["red", "blue", "red", "green", "red"]
print(t6_list.count("red"))

# task7
t7_list = [3, 1, 4, 1, 5, 9]
t7_list.sort()
print(t7_list)  # ascending order

t7_list.sort(reverse=True)  # descending order
print(t7_list)

# task8
t8_list = [1, 2, 3, 4, 5]
t8_list.reverse()
print(t8_list)

# task9
t9_list = ["apple", "banana", "cherry"]
t9_list.clear()
print(t9_list)

# task 10
t10_list = ["apple", "banana", "cherry"]
fruits_copy = t10_list.copy()
print(fruits_copy)

# task11
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# task12
words_list = ['Python', 'is', 'powerful']
print(', '.join(words_list))

# task13
words_list2 = ['Python', 'is', 'fun']
print(' '.join(words_list2))

# task14
data = "apple,banana,cherry"
print(data.split(','))

# task15
t15_list = ['red', 'green', 'blue', 'yellow', 'purple']
del t15_list[1:3]
print(t15_list)
