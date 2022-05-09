import random

def genDiccionario():

    lista = [{'id': i, 'edad': random.randint(1, 100)} for i in range(10)]
    return lista

def ordanamiento(lista):

    lista.sort(key=lambda e: e['edad'], reverse=True)
    return lista

if __name__ == '__main__':

    diccionarios = genDiccionario()
    lista_Ordenada = ordanamiento(diccionarios)

    print(lista_Ordenada)
    print("Id Persona mas Joven: ", lista_Ordenada[-1]['id'])
    print("Id Persona mas Vieja: ", lista_Ordenada[0]['id'])