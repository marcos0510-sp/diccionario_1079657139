"""
Gestor de Compras
Programa para gestionar una lista de compras con opciones para:
- Agregar artículos
- Ver lista de compras
- Calcular total
- Eliminar artículos
"""

def agregar_articulo(lista_compras):
    """Agrega un nuevo artículo a la lista de compras"""
    print("\n--- Agregar Artículo ---")
    nombre = input("Nombre del producto: ").strip()
    
    try:
        precio = float(input("Precio del producto: $"))
        cantidad = int(input("Cantidad: "))
        
        if precio < 0 or cantidad < 0:
            print("Error: El precio y la cantidad no pueden ser negativos.")
            return
        
        articulo = {
            "producto": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        
        lista_compras.append(articulo)
        print(f"✓ {nombre} agregado a la lista.")
    
    except ValueError:
        print("Error: Ingresa un precio (número decimal) y cantidad (número entero) válidos.")


def ver_lista(lista_compras):
    """Muestra la lista de compras actual"""
    print("\n--- Lista de Compras ---")
    
    if not lista_compras:
        print("La lista de compras está vacía.")
        return
    
    print(f"{'Producto':<20} {'Precio':<10} {'Cantidad':<10} {'Subtotal':<10}")
    print("-" * 50)
    
    for articulo in lista_compras:
        subtotal = articulo["precio"] * articulo["cantidad"]
        print(f"{articulo['producto']:<20} ${articulo['precio']:<9.2f} {articulo['cantidad']:<10} ${subtotal:<9.2f}")


def calcular_total(lista_compras):
    """Calcula y muestra el total de la lista de compras"""
    print("\n--- Calcular Total ---")
    
    if not lista_compras:
        print("La lista de compras está vacía.")
        return
    
    total = 0
    for articulo in lista_compras:
        subtotal = articulo["precio"] * articulo["cantidad"]
        total += subtotal
    
    print(f"Total de la compra: ${total:.2f}")


def eliminar_articulo(lista_compras):
    """Elimina un artículo de la lista de compras"""
    print("\n--- Eliminar Artículo ---")
    
    if not lista_compras:
        print("La lista de compras está vacía.")
        return
    
    nombre = input("Nombre del producto a eliminar: ").strip()
    
    articulo_encontrado = None
    for articulo in lista_compras:
        if articulo["producto"].lower() == nombre.lower():
            articulo_encontrado = articulo
            break
    
    if articulo_encontrado:
        lista_compras.remove(articulo_encontrado)
        print(f"✓ {nombre} eliminado de la lista.")
    else:
        print(f"Error: {nombre} no se encontró en la lista.")


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("    GESTOR DE COMPRAS")
    print("="*40)
    print("1. Agregar artículo")
    print("2. Ver lista de compras")
    print("3. Calcular total")
    print("4. Eliminar artículo")
    print("5. Salir")
    print("="*40)


def main():
    """Función principal del programa"""
    lista_compras = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_articulo(lista_compras)
        elif opcion == "2":
            ver_lista(lista_compras)
        elif opcion == "3":
            calcular_total(lista_compras)
        elif opcion == "4":
            eliminar_articulo(lista_compras)
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
