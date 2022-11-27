# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def funcLeftSize(X, Y, Z):
    return (bool)(not(X or Y or Z))

def funcRightSize(X, Y, Z):
    return (bool)(not(X) and not(Y) and not(Z))    

for X in [0,1]:
    for Y in [0,1]:
        for Z in [0,1]:            
            print(f'X = {X}, Y = {Y}, Z = {Z}: {funcLeftSize(X,Y,Z)} = {funcRightSize(X,Y,Z)}')

