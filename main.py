from src.logica.OperacionesEnteros import OperacionesEnteros

if __name__ == '__main__':    
    try:
        cantidadNumeros = int(input("Cantidad de números: "))
        numeros = []
        for i in range(cantidadNumeros):
            print(f"Número {i+1:2}: ", end="", flush=True)
            numeros.append(int(input("")))
        
        print(f"Números = {numeros}")
        operacionesEnteros = OperacionesEnteros(numeros)
        print(f"MCD= {operacionesEnteros.calcularMCD()}")
    except ValueError:
        print('Error: Por favor, introduce un número entero válido.')
    except Exception as e:
        print(f'Error inesperado: {e}')