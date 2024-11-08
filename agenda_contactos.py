def mostrar_menu():
    """
    Muestra el menú principal de opciones para gestionar la agenda de contactos.

    Esta función imprime en pantalla las opciones disponibles:
    agregar, eliminar, buscar, listar contactos y salir del programa.
    """
    print("\nAgenda de contacto")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")


def agregar_contacto(agenda):
    """
    Agrega un nuevo contacto a la agenda con su nombre, teléfono y email.

    Args:
        agenda (dict): Diccionario que almacena los contactos. Cada contacto se guarda
                       con el nombre completo como clave, y un diccionario con 'teléfono'
                       y 'email' como valores.
    """
    nombre = (
        input("Por favor introduzca el nombre completo del contacto: ").strip().title()
    )
    telefono = input("Por favor introduzca el teléfono del contacto: ").strip()
    email = input("Por favor introduzca el email del contacto: ").strip().lower()

    agenda[nombre] = {"teléfono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")


def eliminar_contacto(agenda):
    """
    Elimina un contacto existente de la agenda.

    Args:
        agenda (dict): Diccionario que almacena los contactos.
                       Se busca el contacto por su nombre completo.
    """
    nombre = (
        input("Por favor introduzca el nombre completo del contacto: ").strip().title()
    )

    if nombre in agenda:
        del agenda[nombre]
        print("\n¡Contacto borrado exitosamente!")
    else:
        print(f"\nLa persona: {nombre} no se encuentra en la agenda.")


def buscar_contacto(agenda):
    """
    Busca un contacto en la agenda por su nombre completo y muestra su información si existe.

    Args:
        agenda (dict): Diccionario que almacena los contactos.
                       La búsqueda se realiza por el nombre completo.
    """
    nombre = (
        input("Por favor introduzca el nombre completo del contacto: ").strip().title()
    )

    if nombre in agenda:
        print("\nContacto encontrado:")
        print(
            f"Nombre: {nombre}, Teléfono: {agenda[nombre]['teléfono']}, Email: {agenda[nombre]['email']}"
        )
    else:
        print("\nContacto no encontrado.")


def listar_contactos(agenda):
    """
    Muestra una lista de todos los contactos en la agenda.

    Args:
        agenda (dict): Diccionario que almacena los contactos.
                       Cada contacto incluye el nombre, teléfono y email.
    """
    print("Lista de contactos:")
    for i, (contacto, info) in enumerate(agenda.items(), start=1):
        print(
            f"{i}) Nombre: {contacto}, Teléfono: {info['teléfono']}, Email: {info['email']}"
        )


def agenda_contactos():
    """
    Ejecuta la aplicación de la agenda de contactos, permitiendo interactuar con el menú principal.

    Esta función inicializa la agenda con algunos contactos predefinidos y permite al usuario
    elegir opciones del menú para agregar, eliminar, buscar y listar contactos.
    """
    agenda = {
        "Aldrich Torres": {"teléfono": "123-456-7890", "email": "aldrich@example.com"},
        "Margi Pérez": {"teléfono": "098-765-4321", "email": "margi@example.com"},
        "Enrico López": {"teléfono": "234-567-8901", "email": "enrico@example.com"},
        "Christoper Wong": {
            "teléfono": "345-678-9012",
            "email": "christoper@example.com",
        },
        "Cherice Gómez": {"teléfono": "456-789-0123", "email": "cherice@example.com"},
    }

    while True:
        mostrar_menu()
        opcion = input("\nPor favor, elija una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos. ¡Hasta luego!")
            break
        else:
            print("Elija una opción válida.")


agenda_contactos()
