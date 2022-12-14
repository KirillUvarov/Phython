# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
# ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

users = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5']
data = list(enumerate(users))
print(data) #[(0, 'user_1'), (1, 'user_2'), (2, 'user_3'), (3, 'user_4'), (4, 'user_5')]