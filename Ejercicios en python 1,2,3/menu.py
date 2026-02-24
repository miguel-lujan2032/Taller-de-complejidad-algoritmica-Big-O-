"""
MENÚ INTERACTIVO - ANÁLISIS ASINTÓTICO
Archivo único con todos los ejercicios integrados

ESTE ES EL MENU DE LOS EJERCICOS 1
"""

import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# EJERCICIO 1.1 - Nivel Básico
# ============================================================================

def ejercicio_1_1():
    """
    EJERCICIO 1.1 (Nivel Básico)
    Demostrar que: f(n) = 7n² + 5n + 2 = O(n²)
    """
    print("=" * 70)
    print("DEMOSTRACIÓN: f(n) = 7n² + 5n + 2 = O(n²)")
    print("=" * 70)
    print()
    
    print("PASO 1: Calcular el límite L")
    print("-" * 70)
    print("Calculamos: L = lim(n→∞) [f(n) / g(n)]")
    print()
    print("L = lim(n→∞) [(7n² + 5n + 2) / n²]")
    print("L = lim(n→∞) [7 + 5/n + 2/n²]")
    print("L = 7 + 0 + 0")
    print("L = 7")
    print()
    print("ANÁLISIS DEL RESULTADO:")
    print("-" * 70)
    print("Según el criterio del límite:")
    print("  • Si L = 0  → f(n) = O(g(n))")
    print("  • Si L = c (constante > 0) → f(n) = Θ(g(n))")
    print()
    print(f"Como L = 7 (constante positiva), entonces:")
    print("  ✓ f(n) = O(n²)      [cota superior]")
    print("  ✓ f(n) = Θ(n²)      [cota exacta]")
    print()
    
    print("PASO 2: Definición de Big O")
    print("-" * 70)
    print("Necesitamos demostrar que existe c > 0 y n₀ tal que:")
    print("    7n² + 5n + 2 ≤ c·n²  para todo n ≥ n₀")
    print()
    
    print("PASO 3: Encontrar la constante c")
    print("-" * 70)
    print("Dividimos ambos lados entre n² (válido para n > 0):")
    print("    7 + 5/n + 2/n² ≤ c")
    print()
    print("El término [(7 + 5/n + 2/n²)] es decreciente y tiende a 7")
    print("Elegimos c = 8 (cualquier valor ≥ 7 funciona)")
    print()
    
    print("PASO 4: Encontrar n₀ (cota inferior)")
    print("-" * 70)
    print("Necesitamos verificar que para n ≥ n₀:")
    print("    7n² + 5n + 2 ≤ 8n²")
    print()
    print("Reorganizando:")
    print("    5n + 2 ≤ n²")
    print()
    
    # Encontrar n₀ numéricamente
    for n in range(1, 20):
        left = 5*n + 2
        right = n**2
        if left <= right:
            n0 = n
            print(f"Para n = {n}:")
            print(f"    5({n}) + 2 = {left}")
            print(f"    {n}² = {right}")
            print(f"    {left} ≤ {right} ✓")
            print()
            print(f"Por lo tanto, n₀ = {n0}")
            break
    print()
    
    print("PASO 5: Verificación")
    print("-" * 70)
    print("Verificamos que para n ≥ n₀, f(n) ≤ c·g(n):")
    print()
    
    c = 8
    n0 = 6
    
    print(f"c = {c}, n₀ = {n0}")
    print()
    print(f"{'n':<5} {'f(n) = 7n² + 5n + 2':<30} {'c·n² = {c}n²':<20} {'f(n) ≤ c·n²?':<15}")
    print("-" * 70)
    
    for n in [5, 6, 10, 20, 50, 100]:
        f_n = 7*n**2 + 5*n + 2
        c_gn = c * n**2
        cumple = "✓" if f_n <= c_gn else "✗"
        print(f"{n:<5} {f_n:<30} {c_gn:<20} {cumple:<15}")
    
    print()
    print("=" * 70)
    print("CONCLUSIÓN:")
    print("=" * 70)
    print(f"✓ Se demostró que f(n) = 7n² + 5n + 2 = O(n²)")
    print(f"  con c = 8 y n₀ = 6")
    print()
    print(f"✓ También es f(n) = Θ(n²) porque L = 7 ≠ 0")
    print()
    print(f"Esto significa que 7n² domina el término de menor orden")
    print("y f(n) crece al mismo ritmo que n² (cota exacta)")
    print("=" * 70)


# ============================================================================
# EJERCICIO 1.2 - Nivel Intermedio
# ============================================================================

def ejercicio_1_2():
    """
    EJERCICIO 1.2: Demostración de que ln(n) = O(n)
    """
    print("=" * 70)
    print("DEMOSTRACIÓN: ln(n) = O(n)")
    print("=" * 70)

    # DEMOSTRACIÓN TEÓRICA
    print("\n1. DEMOSTRACIÓN TEÓRICA:")
    print("-" * 70)
    print("Para probar que ln(n) = O(n), necesitamos encontrar constantes c > 0 y n₀")
    print("tales que ln(n) ≤ c·n para todo n ≥ n₀")
    print()
    print("Teorema: ln(n) ≤ n para todo n ≥ 1")
    print()
    print("Prueba:")
    print("  • Consideramos h(n) = n - ln(n)")
    print("  • h'(n) = 1 - 1/n = (n-1)/n")
    print("  • Para n ≥ 1: h'(n) ≥ 0, entonces h(n) es no decreciente")
    print("  • h(1) = 1 - ln(1) = 1 - 0 = 1 ≥ 0")
    print("  • Por lo tanto: n - ln(n) ≥ 0 para todo n ≥ 1")
    print("  • Es decir: ln(n) ≤ n para todo n ≥ 1")
    print()
    print("Conclusión:")
    print("  Elegimos c = 1 y n₀ = 1")
    print("  ln(n) ≤ 1·n para todo n ≥ 1")
    print("  Por lo tanto: ln(n) = O(n) ✓")

    # DEMOSTRACIÓN NUMÉRICA
    print("\n\n2. DEMOSTRACIÓN NUMÉRICA:")
    print("-" * 70)
    print(f"{'n':>8} {'ln(n)':>12} {'n':>12} {'ln(n)/n':>12} {'c=1 válido?':>15}")
    print("-" * 70)

    valores_n = [1, 2, 5, 10, 50, 100, 500, 1000, 10000, 100000, 1000000]

    for n in valores_n:
        ln_n = math.log(n)
        razon = ln_n / n
        es_valido = "Sí ✓" if ln_n <= n else "No ✗"
        print(f"{n:>8} {ln_n:>12.4f} {n:>12} {razon:>12.6f} {es_valido:>15}")

    print("\nObservación: Para todo n ≥ 1, ln(n) ≤ n y ln(n)/n → 0 cuando n → ∞")
    print("Esto confirma que ln(n) = O(n)")

    # VISUALIZACIÓN GRÁFICA
    print("\n\n3. VISUALIZACIÓN GRÁFICA:")
    print("-" * 70)

    # Crear datos para la gráfica
    n_values = np.linspace(1, 100, 1000)
    ln_n = np.log(n_values)
    linear_n = n_values

    # Crear figura
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Gráfica 1: Comparación directa
    ax1.plot(n_values, ln_n, 'b-', linewidth=2, label='f(n) = ln(n)')
    ax1.plot(n_values, linear_n, 'r-', linewidth=2, label='g(n) = n (cota superior)')
    ax1.fill_between(n_values, ln_n, linear_n, alpha=0.3, color='green', 
                      label='Región donde ln(n) ≤ n')
    ax1.set_xlabel('n', fontsize=12)
    ax1.set_ylabel('Valor', fontsize=12)
    ax1.set_title('Comparación: ln(n) vs n', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)

    # Gráfica 2: Razón ln(n)/n
    razon_values = ln_n / n_values
    ax2.plot(n_values, razon_values, 'g-', linewidth=2, label='ln(n)/n')
    ax2.axhline(y=1, color='r', linestyle='--', linewidth=2, label='c = 1')
    ax2.plot(1, 0, 'ro', markersize=10, label='n₀ = 1')
    ax2.fill_between(n_values, razon_values, 1, alpha=0.2, color='green')
    ax2.set_xlabel('n', fontsize=12)
    ax2.set_ylabel('ln(n)/n', fontsize=12)
    ax2.set_title('Razón ln(n)/n (tiende a 0)', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig('ejercicio_1_2_grafica.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfica guardada como 'ejercicio_1_2_grafica.png'")
    plt.show()

    # CONCLUSIÓN FINAL
    print("\n\n" + "=" * 70)
    print("CONCLUSIÓN:")
    print("=" * 70)
    print("""
Se ha demostrado que ln(n) = O(n) de tres formas:

1. MATEMÁTICAMENTE:
   - Probamos que existe c = 1 y n₀ = 1 tales que ln(n) ≤ 1·n para todo n ≥ 1
   - Por definición de O grande, esto implica ln(n) = O(n)

2. NUMÉRICAMENTE:
   - Verificamos para múltiples valores de n que ln(n) ≤ n siempre se cumple
   - La razón ln(n)/n disminuye conforme n aumenta

3. VISUALMENTE:
   - Las gráficas muestran que n domina a ln(n)
   - La función ln(n) nunca excede la función n para n ≥ 1

RESPUESTA: ln(n) = O(n) con c = 1 y n₀ = 1 ✓
""")
    print("=" * 70)


# ============================================================================
# EJERCICIO 1.3 - Nivel Avanzado
# ============================================================================

def ejercicio_1_3():
    """
    EJERCICIO 1.3: Relación Asintótica entre n! y 2^n
    """
    print("=" * 80)
    print("ANÁLISIS: Relación Asintótica entre n! y 2^n")
    print("=" * 80)

    # DEMOSTRACIÓN TEÓRICA
    print("\n1. DEMOSTRACIÓN TEÓRICA:")
    print("-" * 80)
    print("Para determinar cuál crece más rápido, analizamos el límite de la razón:")
    print()
    print("  lim (n → ∞) n! / 2^n = ?")
    print()
    print("Método: Prueba de la Razón (Ratio Test)")
    print("=" * 80)
    print()
    print("Sea a_n = n! / 2^n")
    print()
    print("Calculamos a_(n+1) / a_n:")
    print()
    print("  a_(n+1) / a_n = [(n+1)! / 2^(n+1)] / [n! / 2^n]")
    print("                = [(n+1)! / n!] · [2^n / 2^(n+1)]")
    print("                = (n+1) · (1/2)")
    print("                = (n+1)/2")
    print()
    print("Observación:")
    print("  • Para n ≥ 1: (n+1)/2 ≥ 1 y crece sin límite")
    print("  • Conforme n → ∞: (n+1)/2 → ∞")
    print()
    print("Conclusión:")
    print("  ∴ lim (n → ∞) n! / 2^n = ∞")
    print()
    print("✓ n! crece MUCHO más rápido que 2^n")
    print("✓ n! = ω(2^n)  [omega grande]")
    print("✓ 2^n = O(n!)  [O grande]")
    print()

    # ANÁLISIS COMPARATIVO
    print("\n2. COMPARACIÓN INTUITIVA:")
    print("-" * 80)
    print("Analicemos los últimos factores de ambas expresiones:")
    print()
    print("Para n = 10:")
    print("  n!  = 1·2·3·4·5·6·7·8·9·10 = (1·2·3·4·5) · (6·7·8·9·10)")
    print("       Primeros 5 términos: 120")
    print("       Últimos 5 términos: 30,240")
    print("  2^n = 2·2·2·2·2·2·2·2·2·2 = 1,024")
    print()
    print("  Razón: 10! / 2^10 = 3,628,800 / 1,024 ≈ 3,546")
    print()
    print("Para n = 20:")
    print("  n!  = 1·2·3·...·20 ≈ 2.43 × 10^18")
    print("  2^n = 2^20 ≈ 1.05 × 10^6")
    print("  Razón: n! / 2^n ≈ 2.31 × 10^12  (¡trillones!)")
    print()
    print("Explicación: n! multiplica por números cada vez más grandes (n con valores")
    print("grandes), mientras que 2^n siempre multiplica por 2. Esto hace que n! domine")
    print("completamente.")

    # DEMOSTRACIÓN NUMÉRICA
    print("\n\n3. DEMOSTRACIÓN NUMÉRICA:")
    print("-" * 80)
    print(f"{'n':>3} {'n!':>15} {'2^n':>15} {'n!/2^n':>15} {'Ratio (n+1)/2':>15}")
    print("-" * 80)

    n_values_small = list(range(1, 21))

    for n in n_values_small:
        factorial_n = math.factorial(n)
        power_2_n = 2**n
        razon = factorial_n / power_2_n
        ratio = (n + 1) / 2
        
        print(f"{n:>3} {factorial_n:>15} {power_2_n:>15} {razon:>15.2e} {ratio:>15.1f}")

    print()
    print("Observación clave: El ratio a_(n+1)/a_n = (n+1)/2 crece linealmente")
    print("Esto explica el crecimiento explosivo de n! respecto a 2^n")

    # VISUALIZACIÓN GRÁFICA
    print("\n\n4. VISUALIZACIÓN GRÁFICA:")
    print("-" * 80)

    # Para los primeros términos usamos escala linear
    n_linear = np.arange(1, 13)
    factorial_linear = [math.factorial(n) for n in n_linear]
    power_linear = [2**n for n in n_linear]

    # Para términos posteriores usamos escala logarítmica
    n_log = np.arange(1, 21)
    factorial_log = [math.factorial(n) for n in n_log]
    power_log = [2**n for n in n_log]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # Gráfica 1: Escala Linear (primeros términos)
    ax1.plot(n_linear, factorial_linear, 'ro-', linewidth=2, markersize=8, label='n!')
    ax1.plot(n_linear, power_linear, 'bs-', linewidth=2, markersize=8, label='2^n')
    ax1.set_xlabel('n', fontsize=11)
    ax1.set_ylabel('Valor', fontsize=11)
    ax1.set_title('Comparación: n! vs 2^n (escala linear)', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 13)

    # Gráfica 2: Escala Logarítmica
    ax2.semilogy(n_log, factorial_log, 'ro-', linewidth=2, markersize=8, label='n!')
    ax2.semilogy(n_log, power_log, 'bs-', linewidth=2, markersize=8, label='2^n')
    ax2.set_xlabel('n', fontsize=11)
    ax2.set_ylabel('Valor (escala log)', fontsize=11)
    ax2.set_title('Comparación: n! vs 2^n (escala logarítmica)', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_xlim(0, 21)

    # Gráfica 3: Razón n!/2^n
    razon_completa = [math.factorial(n) / (2**n) for n in n_log]
    ax3.semilogy(n_log, razon_completa, 'go-', linewidth=2.5, markersize=9)
    ax3.set_xlabel('n', fontsize=11)
    ax3.set_ylabel('n! / 2^n (escala log)', fontsize=11)
    ax3.set_title('Razón n!/2^n (crece exponencialmente)', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3, which='both')
    ax3.set_xlim(0, 21)

    # Gráfica 4: Factor de crecimiento (n+1)/2
    ax4.plot(n_log, [(n+1)/2 for n in n_log], 'mo-', linewidth=2.5, markersize=9)
    ax4.set_xlabel('n', fontsize=11)
    ax4.set_ylabel('a_(n+1) / a_n = (n+1)/2', fontsize=11)
    ax4.set_title('Factor de Crecimiento por Paso', fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim(0, 21)
    ax4.axhline(y=1, color='r', linestyle='--', alpha=0.5, label='Factor = 1')
    ax4.legend(fontsize=10)

    plt.tight_layout()
    plt.savefig('ejercicio_1_3_grafica.png', dpi=150, bbox_inches='tight')
    print("✓ Gráficas guardadas como 'ejercicio_1_3_grafica.png'")
    plt.show()

    # ANÁLISIS DE LA TASA DE CRECIMIENTO
    print("\n\n5. ANÁLISIS DE LA TASA DE CRECIMIENTO:")
    print("-" * 80)
    print(f"{'n':>3} {'a_(n+1)/a_n':>15} {'Interpretación':>40}")
    print("-" * 80)

    for n in range(1, 16):
        factor = (n + 1) / 2
        interpretation = f"({n+1})/2 = {factor:.1f}"
        if factor < 1:
            interpretation += " < 1 (disminuye)"
        elif factor == 1:
            interpretation += " = 1 (constante)"
        else:
            interpretation += f" > 1 (multiplica por {factor:.1f}x)"
        print(f"{n:>3} {factor:>15.1f} {interpretation:>40}")

    print()
    print("Conclusión: Cada paso (n → n+1) multiplica la razón n!/2^n por (n+1)/2")
    print("Este factor CRECE CON n, haciendo que n! supere a 2^n de forma explosiva")

    # CONCLUSIÓN FINAL
    print("\n\n" + "=" * 80)
    print("CONCLUSIÓN FINAL:")
    print("=" * 80)
    print("""
1. RELACIÓN ASINTÓTICA:
   ✓ n! = ω(2^n)
   ✓ 2^n = O(n!)
   ✓ lim (n → ∞) n! / 2^n = ∞

2. ¿CUÁL CRECE MÁS RÁPIDO?
   ✓ n! crece EXPONENCIALMENTE MÁS RÁPIDO que 2^n

3. INTUICIÓN MATEMÁTICA:
   • n! = 1·2·3·4·...·n (productos cada vez más grandes)
   • 2^n = 2·2·2·...·2 (siempre multiplica por 2)
   
   A partir de n=3: (n+1)/2 ≥ 1 y crece linealmente
   Esto debe multiplicar a n!/2^n cada paso, creando crecimiento explosivo

4. ORDEN DE MAGNITUD:
   • n=10:   10! / 2^10  ≈ 3.5 × 10^3
   • n=20:   20! / 2^20  ≈ 2.3 × 10^12
   • n=30:   30! / 2^30  ≈ 1.2 × 10^21

RESPUESTA: n! crece MUCHO más rápido que 2^n ✓
""")
    print("=" * 80)


# ============================================================================
# FUNCIONES DEL MENÚ
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    """Muestra el menú principal"""
    limpiar_pantalla()
    print("=" * 80)
    print(" ANÁLISIS ASINTÓTICO - MENÚ INTERACTIVO ".center(80))
    print("=" * 80)
    print()
    print("  Seleccione un ejercicio para ver su análisis:")
    print()
    print("  [1] Ejercicio 1.1 - Nivel Básico")
    print("      Demostrar que f(n) = 7n² + 5n + 2 = O(n²)")
    print()
    print("  [2] Ejercicio 1.2 - Nivel Intermedio")
    print("      Demostrar que ln(n) = O(n)")
    print()
    print("  [3] Ejercicio 1.3 - Nivel Avanzado")
    print("      Relación asintótica entre n! y 2^n")
    print()
    print("  [0] Salir del programa")
    print()
    print("-" * 80)

def ejecutar_ejercicio(num_ejercicio):
    """Ejecuta el ejercicio especificado"""
    if num_ejercicio == 1:
        limpiar_pantalla()
        ejercicio_1_1()
    elif num_ejercicio == 2:
        limpiar_pantalla()
        ejercicio_1_2()
    elif num_ejercicio == 3:
        limpiar_pantalla()
        ejercicio_1_3()
    
    input("\nPresione ENTER para volver al menú...")

def main():
    """Función principal - bucle del menú"""
    while True:
        mostrar_menu_principal()
        opcion = input("Ingrese su opción (0-3): ").strip()
        
        if opcion == '1':
            ejecutar_ejercicio(1)
        elif opcion == '2':
            ejecutar_ejercicio(2)
        elif opcion == '3':
            ejecutar_ejercicio(3)
        elif opcion == '0':
            limpiar_pantalla()
            print("=" * 80)
            print("¡Gracias por usar el sistema de análisis asintótico!")
            print("=" * 80)
            sys.exit(0)
        else:
            print("\n❌ Opción inválida. Por favor, ingrese una opción del 0 al 3.")
            input("Presione ENTER para intentar de nuevo...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n¡Programa interrumpido por el usuario!")
        sys.exit(0)
