"""
Búsqueda en Lista
Programa que trabaja con una lista de números e implementa funciones de búsqueda,
cálculo de promedio, filtrado y ordenamiento.
"""

# Lista de números a trabajar
numeros = [12, 45, 78, 23, 56, 89, 34, 67]


def buscar_numero(numero):
    """
    Devuelve el índice del número en la lista, o -1 si no existe.
    Usa un bucle con comprobación.
    """
    for i in range(len(numeros)):
        if numeros[i] == numero:
            return i
    return -1


def promedio_lista(lista):
    """
    Calcula y devuelve el promedio de todos los elementos.
    Usa sum() y len() para simplificar el cálculo.
    """
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


def numeros_mayores(umbral):
    """
    Devuelve una nueva lista con todos los números mayores que el umbral indicado.
    Usa comprensión de listas.
    """
    return [numero for numero in numeros if numero > umbral]


def ordenar_lista(lista):
    """
    Ordena los números de menor a mayor y devuelve la lista ordenada.
    Usa la función sorted().
    """
    return sorted(lista)


def mostrar_lista_actual():
    """Muestra la lista actual de números"""
    print(f"\nLista actual: {numeros}")
    print(f"Cantidad de elementos: {len(numeros)}\n")


def opcion_buscar():
    """Opción 1: Buscar un número en la lista"""
    print("\n--- Buscar Número ---")
    try:
        numero = int(input("Ingresa el número a buscar: "))
        indice = buscar_numero(numero)
        
        if indice != -1:
            print(f"✓ El número {numero} se encontró en el índice {indice}")
        else:
            print(f"✗ El número {numero} no se encuentra en la lista")
    except ValueError:
        print("Error: Ingresa un número válido")


def opcion_promedio():
    """Opción 2: Calcular el promedio de la lista"""
    print("\n--- Calcular Promedio ---")
    promedio = promedio_lista(numeros)
    print(f"Promedio de la lista: {promedio:.2f}")


def opcion_filtrar():
    """Opción 3: Filtrar números mayores a un umbral"""
    print("\n--- Filtrar Números Mayores ---")
    try:
        umbral = int(input("Ingresa el umbral: "))
        resultado = numeros_mayores(umbral)
        
        if resultado:
            print(f"Números mayores a {umbral}: {resultado}")
            print(f"Total encontrados: {len(resultado)}")
        else:
            print(f"No hay números mayores a {umbral}")
    except ValueError:
        print("Error: Ingresa un número válido")


def opcion_ordenar():
    """Opción 4: Ordenar la lista"""
    print("\n--- Ordenar Lista ---")
    lista_ordenada = ordenar_lista(numeros)
    print(f"Lista ordenada: {lista_ordenada}")


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("      BÚSQUEDA EN LISTA")
    print("="*50)
    print("1. Buscar número")
    print("2. Calcular promedio")
    print("3. Filtrar números mayores")
    print("4. Ordenar lista")
    print("5. Ver lista actual")
    print("6. Salir")
    print("="*50)


def main():
    """Función principal del programa"""
    print("BIENVENIDO AL PROGRAMA DE BÚSQUEDA EN LISTA")
    mostrar_lista_actual()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            opcion_buscar()
        elif opcion == "2":
            opcion_promedio()
        elif opcion == "3":
            opcion_filtrar()
        elif opcion == "4":
            opcion_ordenar()
        elif opcion == "5":
            mostrar_lista_actual()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
