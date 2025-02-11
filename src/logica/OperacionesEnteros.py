from src.logica.FaltanParametros import FaltanParametros

class OperacionesEnteros:
    def __init__(self, numeros):
        if not isinstance(numeros, list):
            raise TypeError('Error: Los números deben proporcionarse en una lista.')
        if len(numeros) < 2:
            raise FaltanParametros('Error: Se necesitan al menos dos números para calcular el MCD.')
        self.__numeros = numeros

    def calcularMCD(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros('Error: Se requieren al menos dos números para calcular el MCD.')
        elif len(self.__numeros) > 1:
            return self.MCDMasDosNumeros()
        else:
            return 0

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCDMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError(f'Error: Todos los valores deben ser enteros. Valor inválido: {n}')

        cantidadNumeros = len(self.__numeros)
        mcd = self.MCD(self.__numeros[0], self.__numeros[1])
        i = 0
        while i < (cantidadNumeros - 2):
            mcd = self.MCD(mcd, self.__numeros[i + 2])
            i += 1
        return mcd