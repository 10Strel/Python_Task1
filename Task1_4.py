# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти координатной сетки: '))

if number not in [1,2,3,4]:
    print('Ошибка ввода')
else:
    if number == 1:
        print(f'X: от 0 до oo, Y: от 0 до oo')
    elif number == 2:
        print(f'X: от -oo до 0, Y: от 0 до oo')
    elif number == 3:
        print(f'X: от -oo до 0, Y: от -oo до 0')
    else:
        print(f'X: от 0 до oo, Y: от -oo до 0')

