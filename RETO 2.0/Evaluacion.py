def stats(valores):
    if not valores:
        return {"min": None, "max": None, "promedio": None}
    return {
        "min": min(valores),
        "max": max(valores),
        "promedio": sum(valores) / len(valores),
    }

def fmt(x):
    return None if x is None else f"{x:.3f}"

def simulacion_balance():
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
            masa_nueva = float(input("Ingrese el peso (kg): "))
            brazo_nuevo = float(input("Ingrese el brazo (m): "))
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

    # Calcular estadísticas
    stats_pesos = stats(pesos)
    stats_momentos = stats(momentos)
    stats_cg = stats(centros_gravedad)

    # Construir resumen
    resumen = {
        "pesos": {
            "valores": pesos,
            "min": stats_pesos["min"],
            "max": stats_pesos["max"],
            "promedio": stats_pesos["promedio"]
        },
        "momentos": {
            "valores": momentos,
            "min": stats_momentos["min"],
            "max": stats_momentos["max"],
            "promedio": stats_momentos["promedio"]
        },
        "centros_gravedad": {
            "valores": centros_gravedad,
            "min": stats_cg["min"],
            "max": stats_cg["max"],
            "promedio": stats_cg["promedio"]
        },
        "limites_cg": {
            "inferior": limite_inferior,
            "superior": limite_superior
        }
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
    return resumen

resumen_guardado = None  

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ejecutar simulación de peso y balance")
    print("2. Mostrar listas del resumen")
    print("3. Salir")

    opcion_menu = input("Selecciona una opción: ")

    if opcion_menu == "1":
        resumen_guardado = simulacion_balance()
    elif opcion_menu == "2":
        if resumen_guardado:
            print("\n=== LISTAS DEL RESUMEN ===")
            for clave, contenido in resumen_guardado.items():
                if isinstance(contenido, dict) and "valores" in contenido:
                    print(f"\n{clave.upper()}:")
                    print(" ", " ".join(f"{v:.3f}" for v in contenido["valores"]))
        else:
            print("\nPrimero debes ejecutar la simulación (opción 1).")
    elif opcion_menu == "3":
        print("Programa finalizado")
        break
    else:
        print("Opción No Válida")