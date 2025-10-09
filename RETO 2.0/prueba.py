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


# Variable global para guardar resultados
ultimo_resumen = None


def simulacion_balance():
    global ultimo_resumen

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

        if masa_nueva <= 0 or brazo_nuevo <= 0:
            print("El peso y el brazo deben ser mayores que 0.")
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

    resumen = {
        "pesos": {
            "valores": pesos,
            "min": stats_pesos["min"],
            "max": stats_pesos["max"],
            "promedio": stats_pesos["promedio"],
        },
        "momentos": {
            "valores": momentos,
            "min": stats_momentos["min"],
            "max": stats_momentos["max"],
            "promedio": stats_momentos["promedio"],
        },
        "centros_gravedad": {
            "valores": centros_gravedad,
            "min": stats_cg["min"],
            "max": stats_cg["max"],
            "promedio": stats_cg["promedio"],
        },
        "limites_cg": {
            "inferior": limite_inferior,
            "superior": limite_superior,
        },
    }

    ultimo_resumen = resumen
    print("\nSimulación completada y resultados guardados.")


def imprimir_listas_y_diccionarios():
    if not ultimo_resumen:
        print("\nNo hay resultados guardados aún. Ejecuta primero la simulación (opción 1).")
        return

    print("\n=== IMPRESIÓN DE LISTAS Y DICCIONARIOS ===")

    # Mostrar límites
    limites = ultimo_resumen["limites_cg"]
    print(f"\nLímites del Centro de Gravedad:")
    print(f"  Inferior: {fmt(limites['inferior'])} m")
    print(f"  Superior: {fmt(limites['superior'])} m")

    # Mostrar cada lista con sus valores y estadísticas
    for clave in ["pesos", "momentos", "centros_gravedad"]:
        contenido = ultimo_resumen[clave]
        valores = contenido["valores"]
        print(f"\n--- {clave.upper()} ---")
        if valores:
            for i, v in enumerate(valores, start=1):
                print(f"Elemento {i}: {v:.3f}")
            print(f"\n  Mínimo   : {fmt(contenido['min'])}")
            print(f"  Máximo   : {fmt(contenido['max'])}")
            print(f"  Promedio : {fmt(contenido['promedio'])}")
        else:
            print("No se registraron datos.")

    input("\nPresiona Enter para volver al menú principal...")


# === MENÚ PRINCIPAL ===
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ejecutar simulación de peso y balance")
    print("2. Imprimir listas y diccionarios")
    print("3. Salir")

    opcion_menu = input("Selecciona una opción: ")

    if opcion_menu == "1":
        simulacion_balance()
    elif opcion_menu == "2":
        imprimir_listas_y_diccionarios()
    elif opcion_menu == "3":
        print("Programa finalizado")
        break
    else:
        print("Opción no válida")
