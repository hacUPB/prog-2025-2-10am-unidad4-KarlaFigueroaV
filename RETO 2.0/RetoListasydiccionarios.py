# CÓDIGO 2 RETO PYTHON (PESO Y BALANCE)

def stats(valores):
    if not valores:
        return {"min": None, "max": None, "promedio": None}
    return {
        "min": min(valores),
        "max": max(valores),
        "promedio": sum(valores) / len(valores),
    }

def fmt(x):
    """Formatea a 3 decimales o devuelve None sin romper f-strings."""
    return None if x is None else f"{x:.3f}"

pesos = []
momentos = []
centros_gravedad = []

peso_total = 0.0
momento_total = 0.0
limite_inferior = 10.0
limite_superior = 20.0
n = 0

while True:
    print("\nOpciones de carga:")
    print("1. Pasajero")
    print("2. Carga")
    print("3. Combustible")
    print("4. Terminar")

    opcion = input("Selecciona: ").strip()

    if opcion == "4":
        print("\nSimulación finalizada.")
        break

    if opcion not in {"1", "2", "3"}:
        print("Opción inválida. Intenta de nuevo.")
        continue

    try:
        masa_nueva = float(input("Ingrese el peso (kg): ").strip())
        brazo_nuevo = float(input("Ingrese el brazo (m): ").strip())
    except ValueError:
        print("Entrada inválida. Debes ingresar números.")
        continue

    if masa_nueva <= 0:
        print("El peso debe ser mayor que 0.")
        continue

    peso_total += masa_nueva
    momento_total += masa_nueva * brazo_nuevo
    cg = momento_total / peso_total
    n += 1

    pesos.append(peso_total)
    momentos.append(momento_total)
    centros_gravedad.append(cg)

    print(f"\nElemento agregado número: {n}")
    print(f"Peso total: {peso_total:.2f} kg")
    print(f"Centro de gravedad (CG): {cg:.2f} m")

    if limite_inferior <= cg <= limite_superior:
        print("Avión balanceado")
    else:
        print("¡Avión inestable!")

resumen = {
    "pesos": {"valores": pesos, **stats(pesos)},
    "momentos": {"valores": momentos, **stats(momentos)},
    "centros_gravedad": {"valores": centros_gravedad, **stats(centros_gravedad)},
    "limites_cg": {"inferior": limite_inferior, "superior": limite_superior},
}

print("\n=== Diccionario de resultados ===")
for clave, contenido in resumen.items():
    if isinstance(contenido, dict) and "valores" in contenido:
        vals_fmt = [f"{v:.3f}" for v in contenido["valores"]]
        print(f"\n{clave}:")
        print(f"  valores  : {vals_fmt}")
        print(f"  min      : {fmt(contenido['min'])}")
        print(f"  max      : {fmt(contenido['max'])}")
        print(f"  promedio : {fmt(contenido['promedio'])}")
    else:
        print(f"\n{clave}: {contenido}")

input("\nPresiona Enter para salir...")