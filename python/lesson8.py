# Funksiyalar
def about(ad, yash):
    return f'Menim adim {ad}dir, menim {yash}im var.'
    print(ad, yash)


print(about('Gulare', 19))


def calculator(a, b, emeliyyat):
    if emeliyyat == '+':
        return f'{a}{emeliyyat}{b} = {a + b}'
    elif emeliyyat == '-':
        return f'{a}{emeliyyat}{b} = {a - b}'
    elif emeliyyat == '*':
        return f'{a}{emeliyyat}{b} = {a * b}'
    else:
        return f'{a}{emeliyyat}{b} = {a / b}'


print(calculator(34, 7, '*'))


def calculator(c, d):
    c = int(input('c daxil et:'))
    d = int(input('d daxil et:'))
    return c + d


print(calculator(4, 6))

a = 10


def func():
    global a
    b = a + 10
    a += 20
    return a, b


print(type(func()))
print(a)

# def find_triangle(x, y, z):
#     x = int(input('x daxil et:'))
#     y = int(input('y daxil et:'))
#     z = int(input('z daxil et:'))
#
#     if x == y and y == z:
#         return 'Bu beraberyanli ucbucaqdir.'
#     elif x * x + y * y == z * z:
#         return 'Bu ucbucaq duzbucaqli ucbucaqdir'
#     else:
#         return 'Bu ucbucaq muxtelifterefli ucbucaqdir'
#
#
# l = [1, 2, 4, 10, 3, 20, 19]
# print(max(l))
#
#
# def find_min(l):
#     min = l[0]
#     for i in l:
#         if i < min:
#             min = i
#             return min
