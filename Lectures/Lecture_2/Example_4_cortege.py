# Кортеж - неизменяемый список. 
# присвоить новое значение его элементам не получится

a = (3, 1, 5, 4)
# print (a)
# print(a[-2])

for item in a:
    print(item)

# Кортежи
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
# print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment

# = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue