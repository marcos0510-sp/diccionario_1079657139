"""
Directorio de Contactos
Programa para gestionar un directorio de contactos usando diccionarios anidados.
Funcionalidades:
- Agregar contacto
- Ver todos los contactos
- Buscar por nombre
- Actualizar teléfono
- Eliminar contacto
"""

def agregar_contacto(directorio):
    """Agrega un nuevo contacto al directorio"""
    print("\n--- Agregar Contacto ---")
    
    nombre = input("Nombre del contacto: ").strip()
    
    # Verificar si el contacto ya existe
    if nombre.lower() in directorio:
        print(f"Error: El contacto '{nombre}' ya existe en el directorio.")
        return
    
    try:
        email = input("Email: ").strip()
        telefono = input("Teléfono: ").strip()
        ciudad = input("Ciudad: ").strip()
        
        # Validar que los campos no estén vacíos
        if not email or not telefono or not ciudad:
            print("Error: Todos los campos son obligatorios.")
            return
        
        # Crear la entrada en el diccionario anidado
        directorio[nombre.lower()] = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono,
            "ciudad": ciudad
        }
        
        print(f"✓ Contacto '{nombre}' agregado exitosamente.")
    
    except Exception as e:
        print(f"Error: {e}")


def ver_todos_contactos(directorio):
    """Muestra todos los contactos del directorio"""
    print("\n--- Ver Todos los Contactos ---")
    
    if not directorio:
        print("El directorio está vacío.")
        return
    
    print(f"\nTotal de contactos: {len(directorio)}\n")
    print("=" * 70)
    
    for clave, datos in directorio.items():
        print(f"Nombre:    {datos['nombre']}")
        print(f"Email:     {datos['email']}")
        print(f"Teléfono:  {datos['telefono']}")
        print(f"Ciudad:    {datos['ciudad']}")
        print("-" * 70)


def buscar_contacto(directorio):
    """Busca un contacto por nombre usando .get()"""
    print("\n--- Buscar Contacto ---")
    
    nombre = input("Nombre a buscar: ").strip().lower()
    
    # Usar .get() para evitar errores si no existe
    contacto = directorio.get(nombre)
    
    if contacto:
        print(f"\n✓ Contacto encontrado:")
        print(f"Nombre:    {contacto['nombre']}")
        print(f"Email:     {contacto['email']}")
        print(f"Teléfono:  {contacto['telefono']}")
        print(f"Ciudad:    {contacto['ciudad']}")
    else:
        print(f"Error: No se encontró ningún contacto con el nombre '{nombre}'.")


def actualizar_telefono(directorio):
    """Actualiza el teléfono de un contacto"""
    print("\n--- Actualizar Teléfono ---")
    
    nombre = input("Nombre del contacto a actualizar: ").strip().lower()
    
    # Buscar el contacto
    if nombre not in directorio:
        print(f"Error: No se encontró el contacto '{nombre}'.")
        return
    
    nuevo_telefono = input("Nuevo teléfono: ").strip()
    
    if not nuevo_telefono:
        print("Error: El teléfono no puede estar vacío.")
        return
    
    # Acceder al diccionario anidado y actualizar el campo
    directorio[nombre]["telefono"] = nuevo_telefono
    print(f"✓ Teléfono de {directorio[nombre]['nombre']} actualizado a: {nuevo_telefono}")


def eliminar_contacto(directorio):
    """Elimina un contacto del directorio usando .pop()"""
    print("\n--- Eliminar Contacto ---")
    
    nombre = input("Nombre del contacto a eliminar: ").strip().lower()
    
    # Usar .pop() para eliminar la entrada completa
    contacto_eliminado = directorio.pop(nombre, None)
    
    if contacto_eliminado:
        print(f"✓ Contacto '{contacto_eliminado['nombre']}' eliminado del directorio.")
    else:
        print(f"Error: No se encontró el contacto '{nombre}'.")


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("    DIRECTORIO DE CONTACTOS")
    print("="*50)
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar por nombre")
    print("4. Actualizar teléfono")
    print("5. Eliminar contacto")
    print("6. Salir")
    print("="*50)


def main():
    """Función principal del programa"""
    directorio = {}
    
    # Agregar algunos contactos de ejemplo
    directorio["juan"] = {
        "nombre": "Juan García",
        "email": "juan@gmail.com",
        "telefono": "555-1234",
        "ciudad": "Madrid"
    }
    
    directorio["maria"] = {
        "nombre": "María López",
        "email": "maria@gmail.com",
        "telefono": "555-5678",
        "ciudad": "Barcelona"
    }
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            agregar_contacto(directorio)
        elif opcion == "2":
            ver_todos_contactos(directorio)
        elif opcion == "3":
            buscar_contacto(directorio)
        elif opcion == "4":
            actualizar_telefono(directorio)
        elif opcion == "5":
            eliminar_contacto(directorio)
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
