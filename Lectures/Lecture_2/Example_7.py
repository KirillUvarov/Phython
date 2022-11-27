# Списки

list1 = [1, 2, 3, 48, 753]
# list2 = list1

# list1[0] = 123 #меняем значение первого значения первого списка
# list2[1] = 333 #меняем значение второго значения второго списка

# print()

# for e in list1:
#     print(e)


# print()

# for e in list2:
#     print(e)

#Удаление последнего значения списка .pop()
print(len(list1)) #выводим количество значений в списке - 5
print(list1)
print(list1.pop(3)) #удаляем элемент с индексом 3

#Добавляем элемент .insert(индекс, значение)
print(list1.insert(3, 44))
print(list1)

#Добавляем значение в конец
print(list1.append(11))
print(list1)


