# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#  в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

inputStr = input("Введите координаты точки (X,Y): ")
coordStr = inputStr.split(",")

X = int(coordStr[0])
Y = int(coordStr[1])

if X == 0 or Y == 0:
    print('Ошибка ввода')
else:
    if X > 0 and Y > 0:
        print('1')
    elif X < 0 and Y > 0:
        print('2')
    elif X < 0 and Y < 0:
        print('3')
    elif X > 0 and Y < 0:
        print('4')
