import numpy
import doctest

def numerosCorridos(matriz):
    """
    Recibe matriz de 5x5 randomizada con números enteros, encontra secuencia de 4
    números consecutivos horizontal o vertical y si la encuentra devuelve la posición inicial y
    final.
    Ejemplo de numeros consecutivos Verticalmente
    >>> numerosCorridos([[2, 4, 1, 2, 1],
    ...                  [1, 4, 1, 2, 3],
    ...                  [3, 1, 2, 4, 1],
    ...                  [2, 4, 3, 4, 1],
    ...                  [2, 0, 4, 3, 2]])
    [[2, 3], [5, 3]]

    Ejemplo de matriz sin numeros consecutivos
    >>> numerosCorridos([[3, 0, 4, 2, 0],
    ...                  [4, 3, 3, 2, 4],
    ...                  [2, 4, 2, 3, 4],
    ...                  [4, 1, 4, 1, 4],
    ...                  [1, 1, 1, 4, 2]])
    []

    Ejemplo de numeros consecutivos Horizontalmente
    >>> numerosCorridos([[2, 4, 1, 2, 1],
    ...                  [1, 4, 1, 2, 3],
    ...                  [3, 1, 2, 4, 1],
    ...                  [0, 1, 2, 3, 1],
    ...                  [2, 0, 4, 3, 2]])
    [[4, 1], [4, 4]]
    """

    respuesta = []

    for i in range(5):
        for j in range(2):
            if matriz[i][j] == matriz[i][j+1]-1 == matriz[i][j+2]-2 == matriz[i][j+3]-3:
                # Busca los numeros consecutivos de forma horizontal
                respuesta.append([i+1, j+1])
                respuesta.append([i+1, j+4])
                break
            if matriz[j][i] == matriz[j+1][i]-1 == matriz[j+2][i]-2 == matriz[j+3][i]-3:
                # Busca los numeros consecutivos de forma vertical
                respuesta.append([j+1, i+1])
                respuesta.append([j+4, i+1])
                break
    return respuesta

if __name__ == '__main__':
    print('**************Comienzo del TEST****************************', end='\n\n')
    print(doctest.testmod(),end='\n\n')
    print('**************Fin del TEST*********************************\n')
    m_random = numpy.random.randint(5, size=(5, 5))

    print(m_random)
    print()

    coordenadas = numerosCorridos(m_random)
            
    if coordenadas:
        print(f'Posicion inicial:\tfila: {coordenadas[0][0]} - columna: {coordenadas[0][1]}')
        print(f'Posicion final:\t\tfila: {coordenadas[1][0]} - columna: {coordenadas[1][1]}')
    else:
        print('No existen 4 numeros concecutivos')