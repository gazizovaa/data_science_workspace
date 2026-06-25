# """
# Siz bütün yolların mükəmməl bir şəbəkəyə salındığı Karteziya şəhərində yaşayırsınız.
# Görüşünüz var və görüşə 10 dəqiqə tez gəlmisiniz və istəyirsiniz ki, bu müddəti gəzərək
# keçirəsiniz. Şəhər vətəndaşlarına bir gəzinti appı təqdim edir hansı ki, bu app sizə
# gəzmək üçün istiqamətləri əks etdirən bir hərfdən ibarət sətirləri göndərir
# (məs. ['n', 's', 'w', 'e']). Hər istiqamət üzrə bir blok gedirsiniz və bu sizin 1
# dəqiqənizi alır. Siz elə bir algoritm yazmalısınız ki, bu gəzinti sizin nə az nə çox
# 10 dəqiqənizi alıbsa və gəzintinin sonunda başlanğıc nöqtəsindəsinizsə sizə True əks
# halda False cavabı qaytarsın.
# """
#
# # direction = input('Enter your directions: ').split(',')
# # time = 0
# # while len(direction) <= 10:
# #     if len(direction == 10):
# #         if direction == 'north':
# #             time = time + 1
# #         elif direction == 'west':
# #             time = time + 1
# #         elif direction == 'east':
# #             time = time + 1
# #         elif direction == 'south':
# #             time = time + 1
# #         else:
# #             print('You are in the wrong direction.')
# #     else:
# #         print('False')
#
# a = 20
# while True:
#     a += 1
#     if a == 100:
#         break
#     print(a)
#
# # b = 1
# # while b < 50:
# #     if b == 3 or b == 9 or b == 20:
# #         continue
# #     else:
# #         print(b)
# #         b += 1
#
# # sual1
# # list = []
# # names = input("Enter names separated by commas: ").split(',')
# # list.extend(names)
# # if len(list) == 0:
# #     print('no one likes this')
# # elif len(list) == 1:
# #     print(f'{list[0]} likes this')
# # elif len(list) == 2:
# #     print(f'{list[0]} and {list[1]} like this')
# # elif len(list) == 3:
# #     print(f'{list[0]}, {list[1]} and {list[2]} like this')
# # else:
# #     print(f'{list[0]}, {list[1]} and {len(list) + 2} others like this')
#
# # sual2
# # word = input('Bir soz daxil edin: ').lower()
# # result = ''
# # for char in word:
# #     if word.count(char) == 1:
# #         result += '('
# #     elif word.split(' ').count(char) > 1:
# #         result += '('
# #     else:
# #         result += ')'
# # print(result)
#
# # tuples
# t = (2, 3, [2, 4], 5, 'salam')
# a = ('alma', )
# print(type(t))
# print(t.index(2))
# print(t.count(2))
# print(t + a)

# sets
s = {2, 3, 4.5, 'ağac'}
s2 = {2, 3, 90, 64, 'meyvə'}
s.add(20)
print(s)
s.pop()
print(s.pop())
print(s.union(s2))
print(s.intersection(s2))
#
s.update([5,6,7])
print(s)
# s.remove([3, 4.5])
print(s.difference(s2))
print(s.symmetric_difference(s2))
# print(s.issuperset(s2))
# print(s.issubset(s2))
