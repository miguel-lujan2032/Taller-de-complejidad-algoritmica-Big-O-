def buscar_par_especifico(lista, objetivo):
    pasos = 0
    for i in range(len(lista)):
        pasos += 1
        if lista[i] % 2 == 0 and lista[i] == objetivo:
            return True, pasos
    return False, pasos


def algoritmo_misterioso(n):
    i = 1
    operaciones = 0
    while i < n:
        operaciones += 1
        i = i * 2
    return operaciones


def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ejecutar Ejercicio 2.1 (Buscador de pares)")
        print("2. Ejecutar Ejercicio 2.2 (Salto de índices)")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            lista = [int(x) for x in input("Ingresa una lista de números separados por espacio: ").split()]
            objetivo = int(input("Ingresa el número objetivo: "))
            encontrado, pasos = buscar_par_especifico(lista, objetivo)
            if encontrado:
                print(f"✅ El número {objetivo} fue encontrado en {pasos} pasos.")
            else:
                print(f"❌ El número {objetivo} no fue encontrado. Pasos realizados: {pasos}")

        elif opcion == "2":
            n = int(input("Ingresa un número entero: "))
            operaciones = algoritmo_misterioso(n)
            print(f"🔢 Número de operaciones realizadas: {operaciones}")

        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


# Ejecutar el menú
menu()

