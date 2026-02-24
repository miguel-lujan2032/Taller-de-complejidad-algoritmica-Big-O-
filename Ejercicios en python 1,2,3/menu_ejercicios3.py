def interseccion_naive(lista1, lista2):
    """Versión ingenua O(n^2) usando bucles anidados"""
    resultado = []
    for x in lista1:
        for y in lista2:
            if x == y and x not in resultado:
                resultado.append(x)
    return resultado

def interseccion_set(lista1, lista2):
    """Versión optimizada O(n) usando conjuntos"""
    return list(set(lista1) & set(lista2))

def fibonacci(n):
    """Versión recursiva simple O(2^n)"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Intersección de listas (naive)")
        print("2. Intersección de listas (sets)")
        print("3. Calcular Fibonacci recursivo")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            lista1 = input("Ingresa la primera lista separada por comas: ").split(",")
            lista2 = input("Ingresa la segunda lista separada por comas: ").split(",")
            print("Intersección (naive):", interseccion_naive(lista1, lista2))
        
        elif opcion == "2":
            lista1 = input("Ingresa la primera lista separada por comas: ").split(",")
            lista2 = input("Ingresa la segunda lista separada por comas: ").split(",")
            print("Intersección (sets):", interseccion_set(lista1, lista2))
        
        elif opcion == "3":
            n = int(input("Ingresa el valor de n: "))
            print(f"Fibonacci({n}) =", fibonacci(n))
            print("⚠️ Nota: Esta implementación es muy lenta para valores grandes como n=50.")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar menú
menu()
