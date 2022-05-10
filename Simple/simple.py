import random
import doctest

def genDiccionario():
    """ 
    Genera un diccionario con numeros aleatodrios de 1 a 100
    """

    lista = [{'id': i, 'edad': random.randint(1, 100)} for i in range(10)]
    return lista

def ordenamiento(lista):
    """
    Ordena la lista de diccionarios en orner descendente segun la edad.
    >>> ordenamiento([{'id': 0, 'edad': 51},
    ...               {'id': 1, 'edad': 66},
    ...               {'id': 2, 'edad': 34},
    ...               {'id': 3, 'edad': 77},
    ...               {'id': 4, 'edad': 92},
    ...               {'id': 5, 'edad': 33},
    ...               {'id': 6, 'edad': 43},
    ...               {'id': 7, 'edad': 31},
    ...               {'id': 8, 'edad': 55},
    ...               {'id': 9, 'edad': 90}])
    [{'id': 4, 'edad': 92}, {'id': 7, 'edad': 31}]

    >>> ordenamiento([{'id': 0, 'edad': 65},
    ...               {'id': 1, 'edad': 36},
    ...               {'id': 2, 'edad': 76},
    ...               {'id': 3, 'edad': 69},
    ...               {'id': 4, 'edad': 99},
    ...               {'id': 5, 'edad': 76},
    ...               {'id': 6, 'edad': 83},
    ...               {'id': 7, 'edad': 68},
    ...               {'id': 8, 'edad': 39},
    ...               {'id': 9, 'edad': 15}])
    [{'id': 4, 'edad': 99}, {'id': 9, 'edad': 15}]

    >>> ordenamiento([{'id': 0, 'edad': 72},
    ...               {'id': 1, 'edad': 89},
    ...               {'id': 2, 'edad': 26},
    ...               {'id': 3, 'edad': 7},
    ...               {'id': 4, 'edad': 54},
    ...               {'id': 5, 'edad': 10},
    ...               {'id': 6, 'edad': 52},
    ...               {'id': 7, 'edad': 51},
    ...               {'id': 8, 'edad': 17},
    ...               {'id': 9, 'edad': 50}])
    [{'id': 1, 'edad': 89}, {'id': 3, 'edad': 7}]

    >>> ordenamiento([{'id': 0, 'edad': 33},
    ...               {'id': 1, 'edad': 74},
    ...               {'id': 2, 'edad': 23},
    ...               {'id': 3, 'edad': 22},
    ...               {'id': 4, 'edad': 8},
    ...               {'id': 5, 'edad': 53},
    ...               {'id': 6, 'edad': 9},
    ...               {'id': 7, 'edad': 35},
    ...               {'id': 8, 'edad': 60},
    ...               {'id': 9, 'edad': 20}])
    [{'id': 1, 'edad': 74}, {'id': 4, 'edad': 8}]
    """

    lista.sort(key=lambda e: e['edad'], reverse=True)
    return [lista[0], lista[-1]]

if __name__ == '__main__':

    print('**************Comienzo del TEST****************************', end='\n\n')
    print(doctest.testmod(),end='\n\n')
    print('**************Fin del TEST****************************\n')

    diccionarios = genDiccionario()
    lista_Ordenada = ordenamiento(diccionarios)

    print("Id Persona mas Joven: ", lista_Ordenada[-1]['id'])
    print("Id Persona mas Vieja: ", lista_Ordenada[0]['id'])