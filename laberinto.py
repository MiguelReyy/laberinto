laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
]

muros = set(((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)))

posicion_actual = (0, 0)

"""esta funcion la utilizo para que mi ordenador sepa donde poner una x, una p y nada"""
def imprimir_laberinto(posicion_jugador):
    for i, fila in enumerate(laberinto):
        for j, columna in enumerate(fila):
            if (i, j) == posicion_jugador:
                print('P', end=' ')
            elif (i, j) in muros:
                print('X', end=' ')
            else:
                print(columna, end=' ')
        print()
"""con esta funcion indico el movimiento del jugador expresado en i y j"""
def moverse(posicion_jugador, direccion):
    i, j = posicion_jugador
    nueva_posicion = ()

    if direccion == 'arriba' and i > 0 and (i - 1, j) not in muros:
        nueva_posicion = (i - 1, j)
    elif direccion == 'abajo' and i < 0 and (i + 1, j) not in muros:
        nueva_posicion = (i + 1, j)
    elif direccion == 'izquierda' and j > 0 and (i, j - 1) not in muros:
        nueva_posicion = (i, j - 1)
    elif direccion == 'derecha' and j < 0 and (i, j + 1) not in muros:
        nueva_posicion = (i, j + 1)

    return nueva_posicion

while True:
    imprimir_laberinto(posicion_actual)
    if laberinto[posicion_actual[0]][posicion_actual[1]] == 'S':
        print('¡Felicidades! Has llegado a la salida.')
        break

    direccion = input("Ingrese la dirección (arriba, abajo, izquierda, derecha): ").lower()
    nueva_posicion = moverse(posicion_actual, direccion)

    if nueva_posicion:
        posicion_actual = nueva_posicion
    else:
        print("Movimiento no válido. Inténtalo de nuevo.")