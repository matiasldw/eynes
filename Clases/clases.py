import math

class Circulo:
    
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * math.pow(self.radio, 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f'Circulo de radio {self.radio}, Area: {self.area()}, Perimetro: {self.perimetro()}'

    def set_radio(self, radio):
        self.radio = radio

    def multiplo(self, n):
        return Circulo(self.radio * n)

if __name__ == '__main__':

    while True:
        # Valida el radio hasta que  el usuario ingrese uno valido
        try:
            r = int(input('Ingrese el radio: '))
            if r <= 0:
                raise ValueError ('El valor no puede 0 (cero) o menor.')
            c1 = Circulo(r)
            break
        except ValueError as MensajeDeError:
            print(f'{MensajeDeError} Reintente: ', end='')
    
    # Imprime los metodos
    print(f'Area:\t\t{c1.area()}')
    print(f'Perimetro:\t{c1.perimetro()}')
    print(c1, end='\n\n')

    try:
        # Pide un nuevo radio valido (>=0) de no hacerlo no permite un reintento
        r = int(input('Ingrese el nuevo radio: '))
        if r <= 0:
            raise ValueError ('El valor no podia ser 0 (cero) o menor.')
        c1.set_radio(r)
        print(f'Area:\t\t{c1.area()}')
        print(f'Perimetro:\t{c1.perimetro()}')
        print(c1, end='\n\n')
    except ValueError as MensajeDeError:
        print(MensajeDeError)

    try:
        # Pide un radio valido (>=0) para devolver otro objeto 'Circulo' con radio = al radio del circulo1 * el radio ingresado. De no hacerlo no permite un reintento
        r = int(input('Valor al cual de le multiplicara el radio: '))
        if r <= 0:
            raise ValueError ('El valor no podia ser 0 (cero) o menor.')
        c2 =c1.multiplo(r)
        print(f'Area:\t\t{c2.area()}')
        print(f'Perimetro:\t{c2.perimetro()}')
        print(c2, end='\n\n')
    except ValueError as MensajeDeError:
        print(MensajeDeError)