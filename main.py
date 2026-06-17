import csv

#1. Cargar el archivo CSV y almacenar los datos en una lista de diccionarios.
def cargar_paises():
    paises = []

    try:
        with open("paises.csv", "r", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["Nombre"],
                    "poblacion": int(fila["Población"]),
                    "superficie": int(fila["Superficie"]),
                    "continente": fila["Continente"]
                }

                paises.append(pais)

        print("Archivo cargado correctamente.")
        return paises

    except FileNotFoundError:
        print("Error!!! No se encontró el archivo paises.csv.")
        return []

#1.1 Mostrar la lista de países con su información completa (nombre, población, superficie y continente).
def mostrar_paises(paises):

    if len(paises) == 0:
        print("No hay países cargados.")
        return

    print("\n=== LISTA DE PAÍSES ===")

    for pais in paises:
        print(f"● Nombre: {pais['nombre']}")
        print(f"● Población: {pais['poblacion']}")
        print(f"● Superficie (Km²): {pais['superficie']}")
        print(f"● Continente: {pais['continente']}")
        print("-" * 30)


    
#Validaciones
### Función para pedir un número entero al usuario, con validación de entrada. ###  Se asegura de que el número sea un entero positivo y no esté vacío.
def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato == "":
            print("Error!!! No puede estar vacío.")
            continue

        try:
            numero = int(dato)

            if numero <= 0:
                print("Error!!! Debe ser mayor que cero.")
                continue

            return numero

        except ValueError:
            print("Error!!! Se debe ingresar solo números.")

### Función para pedir un texto al usuario, con validación de entrada. ### Se asegura de que el texto no esté vacío y solo contenga letras.
def pedir_texto(mensaje):

    while True:
        try:
            texto = input(mensaje).strip()

            if texto == "":
                raise ValueError("No puede estar vacío.")

            if not texto.isalpha():
                raise ValueError("Solo puede contener letras.")

            return texto

        except ValueError as error:
            print("Error!!!", error)



#2. Agregar un nuevo país a la lista, verificando que no exista previamente.

def agregar_pais(paises):

    nombre = pedir_texto("\nIngrese el nombre del país: ").strip() # Eliminar espacios en blanco al inicio y al final

    # Verificar que no exista
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower(): # Comparar sin importar mayúsculas o minúsculas
            print("Error!!! El país ya existe.")
            return

    try:
        poblacion = pedir_entero("\nIngrese la población: ") # Agregar Población del nuevo país
        superficie = pedir_entero("\nIngrese la superficie en km²: ") # Agregar Superficie del nuevo país
        continente = pedir_texto("\nIngrese el continente: ").strip() # Agregar Continente del nuevo país, eliminar espacios en blanco al inicio y al final

        nuevo_pais = { 
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        paises.append(nuevo_pais) # Agregar el nuevo país a la lista de países

        print("\nPaís agregado correctamente.")

    except ValueError:
        print("Error!!! Debe ingresar números válidos.") # Verificar que se ingresen números válidos para población y superficie.


#3 Actualizar la población y superficie de un país existente, buscando por su nombre.
def actualizar_pais(paises):

    nombre = pedir_texto("Ingrese el nombre del país a actualizar: ").strip()

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            try:
                nueva_poblacion = pedir_entero("Ingrese la nueva población: ") # Agregar nueva población del país a actualizar, con validación de entrada para asegurarse de que sea un número entero positivo y no esté vacío.
                nueva_superficie = pedir_entero("Ingrese la nueva superficie: ") # Agregar nueva superficie del país a actualizar, con validación de entrada para asegurarse de que sea un número entero positivo y no esté vacío.

                if nueva_poblacion <= 0 or nueva_superficie <= 0:
                    raise ValueError("Los valores deben ser mayores que cero.") # Verificar que los nuevos valores de población y superficie sean mayores que cero.

                pais["poblacion"] = nueva_poblacion
                pais["superficie"] = nueva_superficie

                print("País actualizado correctamente.")
                return

            except ValueError as error:
                print("Error!!!", error)
                return

    print("No se encontró el país.")


# 4. Buscar un país por su nombre, mostrando su información completa.
def buscar_pais(paises):

    nombre_buscar = pedir_texto("Ingrese el nombre del país: ").strip().lower()

    encontrado = False

    for pais in paises:

        if nombre_buscar in pais["nombre"].lower():

            print("\nPaís encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")

            encontrado = True

    if not encontrado:
        print("No se encontro el país.")

# 5 Filtrar los países por continente, mostrando solo aquellos que pertenecen al continente especificado por el usuario.
def filtrar_por_continente(paises):
    continente_buscar = pedir_texto("Ingrese el continente: ").strip().lower()

    encontrado = False

    for pais in paises:
        if pais["continente"].lower() == continente_buscar:
            print("\nPaís encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True

    if not encontrado:
        print("No se encontraron países en ese continente.")

# 6 Filtrar los países por rango de población, mostrando solo aquellos cuya población esté entre un mínimo y un máximo especificados por el usuario.

def filtrar_por_poblacion(paises):
    try:
        minimo = int(input("Ingrese población mínima: "))
        maximo = int(input("Ingrese población máxima: "))

        if minimo < 0 or maximo < 0:
            print("Error!!! Los valores que ingresaste no pueden ser negativos.")
            return

        elif minimo > maximo:
            print("Error!!! El mínimo no puede ser mayor que el máximo.")
            return

        encontrado = False

        for pais in paises:
            if minimo <= pais["poblacion"] <= maximo:
                print("\nPaís encontrado:")
                print(f"Nombre: {pais['nombre']}")
                print(f"Población: {pais['poblacion']}")
                print(f"Superficie: {pais['superficie']}")
                print(f"Continente: {pais['continente']}")
                encontrado = True

        if not encontrado:
            print("No se encontraron países en ese rango de población.")

    except ValueError:
        print("Error!!! Debe ingresar números válidos.")

# 7 Filtrar los países por rango de superficie, mostrando solo aquellos cuya superficie esté entre un mínimo y un máximo especificados por el usuario.

def filtrar_por_superficie(paises):
    try:
        minimo = int(input("Ingrese superficie mínima: "))
        maximo = int(input("Ingrese superficie máxima: "))

        if minimo < 0 or maximo < 0:
            print("Error!!! Los valores que ingresaste no pueden ser negativos.")
            return

        elif minimo > maximo:
            print("Error!!! El mínimo no puede ser mayor que el máximo.")
            return

        encontrado = False

        for pais in paises:
            if minimo <= pais["superficie"] <= maximo:
                print("\nPaís encontrado:")
                print(f"Nombre: {pais['nombre']}")
                print(f"Población: {pais['poblacion']}")
                print(f"Superficie: {pais['superficie']}")
                print(f"Continente: {pais['continente']}")
                encontrado = True

        if not encontrado:
            print("No se encontraron países en ese rango de superficie.")

    except ValueError:
        print("Error!!! Debe ingresar números válidos.")


# 8 Ordenar los países por nombre, población o superficie, en orden ascendente o descendente, según la elección del usuario.


def ordenar_paises(paises):
    print("\nOrdenar por:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("\nSeleccione una opción: ")

    print("\nTipo de orden:")
    print("1. Ascendente")
    print("2. Descendente")

    orden = input("\nSeleccione una opción: ")

    descendente = False

    if orden == "2":
        descendente = True

    if opcion == "1":
        paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"], reverse=descendente)
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
    elif opcion == "3":
        paises_ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)
    else:
        print("Opción inválida.")
        return

    print("\n" + "=" * 38 + " PAÍSES ORDENADOS " + "=" * 38)

    print("\n{:35} {:<15} {:<15} {:<25}".format(
        "Nombre",
        "Población",
        "Superficie (Km²)",
        "Continente"
    ))

    print("-" * 90)
    for pais in paises_ordenados:
        print("{:<35} {:<15} {:<15} {:<25}".format(
            pais["nombre"],
            pais["poblacion"],
            pais["superficie"],
            pais["continente"]
        ))
# 9 Mostrar estadísticas, como el país con mayor población, el país con menor población, el promedio de población, el promedio de superficie, y la cantidad de países por continente.

def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    pais_mayor_poblacion = paises[0]
    pais_menor_poblacion = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    cantidad_por_continente = {}

    for pais in paises:
        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais

        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\n=== ESTADÍSTICAS ===")
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    print("\nCantidad de países por continente:")
    for continente in cantidad_por_continente:
        print(f"{continente}: {cantidad_por_continente[continente]}")


def mostrar_menu():
    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1. Mostrar países")
    print("2. Agregar país")
    print("3. Actualizar país")
    print("4. Buscar país por nombre")
    print("5. Filtrar por continente")
    print("6. Filtrar por rango de población")
    print("7. Filtrar por rango de superficie")
    print("8. Ordenar países")
    print("9. Mostrar estadísticas")
    print("10. Salir")


def menu_principal():
    paises = cargar_paises()

    continuar = True

    while continuar:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais(paises)

        elif opcion == "5":
            filtrar_por_continente(paises)

        elif opcion == "6":
            filtrar_por_poblacion(paises)

        elif opcion == "7":
            filtrar_por_superficie(paises)

        elif opcion == "8":
            ordenar_paises(paises)

        elif opcion == "9":
            mostrar_estadisticas(paises)

        elif opcion == "10":
            print("Saliendo del programa...")
            continuar = False

        else:
            print("Opción inválida!!! Intente nuevamente...")


menu_principal()
