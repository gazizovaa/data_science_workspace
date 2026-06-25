# # # prime numbers
# # def prime_numbers(x, y):
# #     list_of_numbers = list(range(x, y + 1))
# #     for num in range(x, y + 1):
# #         for k in range(2, num):
# #             if num % k == 0:
# #                 list_of_numbers.remove(num)
# #                 break
# #             else:
# #                 continue
# #         return list_of_numbers
# #
# #
# # print(prime_numbers(1, 101))
# #
# #
# # # Fibonacci numbers
# # def fib(num):
# #     a = 0
# #     b = 1
# #     even_numbers = []
# #     odd_numbers = []
# #     while a <= num:
# #         # print(f'{a}', end=' ')
# #         if a % 2 == 0:
# #             even_numbers.append(a)
# #         else:
# #             odd_numbers.append(a)
# #         a, b = b, a + b
# #     print(f'Even numbers are {even_numbers}')
# #     print(f'Odd numbers are {odd_numbers}')
# #
# #
# # fib(1000)
# #
# #
def addition(a=int(input('a-ni daxil ele: ')), b=int(input('b-ni daxil ele: '))):  # a, b - default values
    return a + b


print(addition(9, 5))


def addition():
    a = int(input('a-ni daxil ele:'))
    b = int(input('a-ni daxil ele:'))
    return a + b


print(addition())


def addition(b, /, *, a):
    return a + b


print(addition(23, a=3))


# #
# #
# # # positional arguments
# # def addition(*args):
# #     sum = 0
# #     for i in args:
# #         sum += i
# #     return sum
# #
# #
# # print(addition(5, 8, 2))
# #
# #
# # # keyword arguments
# # def addition(**args):
# #     return f"Menim adim {args['name']}dir. Menim shifrem {args['passs']}"
# #
# #
# # print(addition(name='Gulnara', passs='Azi_Div29494'))
# #
# #
# # # Numbers (e-olymp)
# # def numbers(a, b):
# #     s = ''
# #     for i in range(a, b + 1):
# #         s += str(i)
# #     return sum(list(map(int, list(s))))
#
#
# TASK3
# sual 1
def minMax(n):
    numbers = []
    for _ in range(n):
        num = int(input(''))
        numbers.append(num)

    min_number = min(numbers)
    max_number = max(numbers)
    print(f'Minimum number is {min_number}, Maximum number is {max_number}.')
    return min_number ** max_number


# sual 2
def calculate_milk_needs(number_of_students):
    volume_of_milk_cup = 200
    volume_of_milk_packet = 900
    number_of_cups = number_of_students

    number_of_milk_packets = (number_of_cups * volume_of_milk_cup) // volume_of_milk_packet
    if (number_of_cups * volume_of_milk_cup) % volume_of_milk_packet != 0:
        number_of_milk_packets += 1
    print(f'{number_of_students} tort ve {number_of_milk_packets} packet sud teleb olunur.')


calculate_milk_needs(30)


def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        i += 1
    return factorial


print(fact(5))


# sual 4
def check_palindrome(soz):
    soz = soz.lower()
    return soz == soz[::-1]


soz = input('Bir soz daxil edin: ')
if check_palindrome(soz):
    print('Bu soz palindromdur.')
else:
    print('Bu soz palindrome deyil.')


# tapşırıqlar
# tapşırıq - 1
def reverse_words():
    get_list = input('Enter words: ').split(' ')
    new_list = []
    for word in get_list:
        new_list.append(word[::-1])
    return new_list


print(reverse_words())


# tapşırıq - 2
def check_uniqueness():
    string = input('Enter a word: ')
    is_unique = True
    for char in string:
        if string.count(char) > 1:
            is_unique = False
            continue
    return is_unique


print(check_uniqueness())

# tapşırıq - 3
l_subset = [[]]
empty_l = [1, 2, 3]
for i in empty_l:
    l_subset += [[i] + k for k in l_subset]
print(l_subset)


# tapşırıq - 4
def write_with_capital_letters():
    global each_word
    user_sentence = input('Enter a sentence: ').split(' ')
    capitalize_words = [each_word.title() for each_word in user_sentence]
    return ' '.join(capitalize_words)


print(write_with_capital_letters())
# tapşırıq - 5
