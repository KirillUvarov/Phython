# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

quarter = int(input('Введите 1-4 четверть плоскости:'))

if quarter == 1:
    print('x∈(0, ∞) u y∈(0, ∞)')
elif quarter == 2:
    print('x∈(∞, 0) u y∈(0, ∞)')
elif quarter == 3:
    print('x∈(∞, 0) u y∈(∞, 0)')
elif quarter == 4:
    print('x∈(0, ∞) u y∈(∞, 0)')
else:
    print('Где вы видели такую четверть?!?!')