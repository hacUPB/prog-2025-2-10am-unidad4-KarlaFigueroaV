# CÓDIGO 2 RETO PYTHON (PESO Y BALANCE)

pesos = []
momentos = []
centros_gravedad = []

peso_total = 0
momento_total = 0
limite_inferior = 10
limite_superior = 20
n = 0

while True:
    print("\nOpciones de carga:")
    print("1. Pasajero")
    print("2. Carga")
    print("3. Combustible")
    print("4. Terminar")
    opcion = input("Selecciona: ")

    if opcion == "4":
        print("\nSimulación finalizada.")
        break

    masa_nueva = float(input("Ingrese el peso (kg): "))
    brazo_nuevo = float(input("Ingrese el brazo (m): "))

    peso_total += masa_nueva
    momento_total += masa_nueva * brazo_nuevo
    cg = momento_total / peso_total
    n += 1

    # Guardar en las listas
    pesos.append(peso_total)
    momentos.append(momento_total)
    centros_gravedad.append(cg)

    print(f"\nElemento agregado número: {n}")
    print(f"Peso total: {peso_total:.2f} kg")
    print(f"Centro de gravedad (CG): {cg:.2f} m")

    if limite_inferior <= cg <= limite_superior:
        print(" Avión balanceado")
    else:
        print("¡Avión inestable!")

# Diccionario con las listas
resumen = {
    "pesos": pesos,
    "momentos": momentos,
    "centros_gravedad": centros_gravedad
}

print("\n=== Diccionario de resultados ===")
for clave, valores in resumen.items():
    print(f"{clave}: {valores}")

input("\nPresiona Enter para salir...")  
