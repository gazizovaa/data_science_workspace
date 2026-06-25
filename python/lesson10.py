def func(x, y):
    return x + y


print(func(4, 5))

# lambda functions - adsiz funksiyalar
print((lambda x, y: x + y)(4, 5))

func = lambda x, y: x + y
print(func(4, 5))

message = lambda: 'Hello'
print(message())

# map
l = ['1', '2', '3', '4', '5']
l_new = []
for i in l:
    l_new.append(int(i))
print(l_new)

print(tuple(map(int, l)))

print(list(map(lambda x: int(x) ** 2, l)))


def func(x):
    return int(x) ** 2


list(map(func, l))
print(set(map(lambda x: int(x) ** 2, l)))


# filter
def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def check(a, b):
    new_list = []
    for i in range(a, b + 1):
        if prime(i):
            new_list.append(i)
    return new_list


# # filter method
def check(a, b):
    return list(filter(prime, range(a, b)))


print(check(20, 50))


# find even numbers
def even_numbers(a, b):
    return list(filter(lambda x: x % 2 == 0, range(a, b)))


print(even_numbers(20, 30))

l1 = [1, 12, 36, 5, 44, 5, 11, 8]
l1.sort()
print(sorted(l1))
l1.sort(key=lambda x: str(x)[0])  # ilk reqemlerinin artan sirasi ile duzsun
print(l1)

# reduce method
from functools import reduce

l2 = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, l2))

# zip method
l3 = ['1', '2', '3', '4', '5', '8', '9']
l4 = [1, 2, 3, 4, 5, 6]
print(dict(zip(l3, l4)))


# task
def find_max(c, d):
    if c > d:
        return c
    return d


l5 = [1, 2, 10, 8, 15, 3, 4, 5]
print(reduce(find_max, l5))

# if-else shortand way
# cavabla if shert1 else shert2
print(reduce(lambda c, d: c if c > d else d, l5))

l5 = [1, 2, 10, 8, 15, 3, 4, 5]


def find_numb(number):
    if number % 2 == 0 and number % 3 == 0:
        return number ** 2
    else:
        if number % 3 == 0:
            return number ** 3
        else:
            if number % 2 == 0:
                return number ** 4
            else:
                return number


print(map(lambda number: number ** 2 if (number % 2 == 0 and number % 3 == 0) else number ** 3 if (number % 3 == 0) else number ** 4 if (
        number % 2 == 0) else number, l5))

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, l5))))

# tapşırıqlar
# 1. functions
# task 1
l6 = [2, 3, 4, 5, 6]
print(list(map(lambda a: a ** 2, l6)))

# task 2
l7 = ['coffee', 'laptop', 'phone', 'watch', 'training']
print(list(map(lambda w: w.upper(), l7)))

# filter tasks
# task 1
print(list(filter(lambda b: b % 2 == 1, range(1, 51))))

# task 2
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(list(filter(lambda word: len(word) > 5, words)))

# lambda
# task 1
print(list(map(lambda c: c ** 2, range(1, 11))))

# task 2
list_of_fruits = ["apple", "banana", "orange", "umbrella", "grape", "elephant", "kiwi"]
print(list(filter(lambda fruit: fruit[0].lower() in 'aeiou', list_of_fruits)))

# reduce task
given_list = [2, 4, 6, 8, 10]
print(reduce(lambda k, l: k * l, given_list))
