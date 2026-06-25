# print(list(map(print, (1, 2, 3))))
# print(list(map(input, (1, 2, 3))))
# print(list(filter(lambda x: x > 5, range(10))))
from functools import reduce

# list comprehensions
l = [12, 4, 5, 16, 7]
print(list(map(lambda x: x * 5, l)))

l_new = []
for i in l:
    l_new.append(int(i) * 5)
print(l_new)

even_numbers = [i * 2 for i in range(10) if i % 2 == 0]

# set comprehensions
# https://medium.com/swlh/set-comprehension-in-python3-for-beginners-80561a9b4007
find_even_numbers = [i ** 2 for i in {5, 5, 6, 7, 8, 9} if i % 2 == 0]
print(find_even_numbers)

# dictionary comprehensions
double_numbers = {str(i): i ** 2 for i in l}
print(double_numbers)

# generator
print((i ** 3 for i in l))

g = (i ** 3 for i in l)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = (str(i ** 3) for i in l)
print(next(g)[3])


def func(a):
    for i in range(a):
        yield i


print(func(3))

g = func(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(list(func(5)))
print(list(func(5)))
print(list(func(5)))


# try:
#     #  calishacaq kod
# except ValueError:
#     # ValueError olaraq calisir
# else:
#     # ValueError calisir
# finally:
#     #  her hald calisir

def func(a, b):
    return a / b


try:
    func(5, 0)
except ZeroDivisionError:
    print('0-a bolunur')
else:
    print('Her shey yolunda')
finally:
    print('Bitdi')


def swap_first_and_last_digits(n):
    n = str(n)
    s = n[-1] + n[1: -1] + n[0]
    return int(s)


print(swap_first_and_last_digits(578))


def func(a):
    return sum(map(int, str(a))) ** 2


print(func(678))


def inverse_fact(result):
    number = 1
    cavab = 1
    while cavab < result:
        number += 1
        cavab *= number
    if cavab == result:
        return number
    else:
        return 'factorial deyil'


print(inverse_fact(120))


# tapsiriqlar
# 8. 1 və n arasında yerləşən sadə ədədləri list şəkilində çap edin.
# check if a single number is prime
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# find prime numbers in given range [1, n + 1]
def check_primes(n):
    prime_numbers = map(lambda x: x if is_prime(x) else None, range(2, n))
    return [num for num in prime_numbers if num is not None]


print(check_primes(12))


# 9. n natural ədədinin cüt rəqəmlərinin cəmini tapın.
def sum_of_even_numbers(numb):
    return sum(int(digit) for digit in str(numb) if int(digit) % 2 == 0)


print(sum_of_even_numbers(24356))

# 10. n ədədi hər hansı bir natural k ədədin kvadratı ya da kubudur. k ədədini və boşluq olmaqla qüvvətini çap edin.
