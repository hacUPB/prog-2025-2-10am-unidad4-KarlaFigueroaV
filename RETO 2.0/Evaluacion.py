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
    return None if x is None else f"{x:.3f}"
 
 
 
pesos = []
momentos = []
centros_gravedad = []
 
limites_cg = {
    "inferior": 10.0,
    "superior": 20.0
}
 
 
def peso_balance():
    global pesos, momentos, centros_gravedad
 
    pesos.clear()
    momentos.clear()
    centros_gravedad.clear()
 
    peso_total = 0.0
    momento_total = 0.0
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
 
        if limites_cg["inferior"] <= cg <= limites_cg["superior"]:
            print("Avión balanceado")
        else:
            print("¡Avión inestable!")
 
    print("\nSimulación completada. Datos guardados correctamente.")
 
 
def imprimir_listas_diccionarios():
    if not pesos:
        print("\nNo hay datos aún. Ejecuta la simulación primero (opción 1).")
        return
 
    print("\n=== LISTAS DE RESULTADOS ===")
 
    listas = {
        "Pesos": pesos,
        "Momentos": momentos,
        "Centros de Gravedad": centros_gravedad,
    }
 
    for nombre, lista in listas.items():
        print(f"\n--- {nombre.upper()} ---")
 
     
        lista_con_formato = "[" + ", ".join(f"{v:.3f}" for v in lista) + "]"
        print(f"Lista: {lista_con_formato}")
 
        for i, valor in enumerate(lista, start=1):
            print(f"Elemento {i}: {valor:.3f}")
 
 
        estad = stats(lista)
        print(f"\n  Mínimo   : {fmt(estad['min'])}")
        print(f"  Máximo   : {fmt(estad['max'])}")
        print(f"  Promedio : {fmt(estad['promedio'])}")
        print(f"  Total elementos: {len(lista)}")
 
    print("\n=== DICCIONARIO DE LÍMITES DEL C.G. ===")
    for clave, valor in limites_cg.items():
        print(f"{clave}: {fmt(valor)}")
 
    input("\nPresiona Enter para volver al menú principal...")
 
 
# === Menú principal ===
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ejecutar simulación de peso y balance")
    print("2. Imprimir listas y diccionario de límites")
    print("3. Salir")
 
    opcion_menu = input("Selecciona una opción: ")
 
    if opcion_menu == "1":
        peso_balance()
    elif opcion_menu == "2":
        imprimir_listas_diccionarios()
    elif opcion_menu == "3":
        print("Programa finalizado. ¡Hasta luego!")
        break
    else:
        print("Opción no válida.")