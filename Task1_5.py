# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

inputStr = input("Введите координаты точки 1 (X,Y): ")
coordStr = inputStr.split(",")

X1 = int(coordStr[0])
Y1 = int(coordStr[1])

inputStr = input("Введите координаты точки 2 (X,Y): ")
coordStr = inputStr.split(",")

X2 = int(coordStr[0])
Y2 = int(coordStr[1])

result = round(math.sqrt((X1-X2)**2+(Y1-Y2)**2), 2)
print(f'A({X1},{Y1}); B({X2},{Y2}) -> {result}')
