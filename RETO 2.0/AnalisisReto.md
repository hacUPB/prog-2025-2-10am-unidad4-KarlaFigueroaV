# Analisis 
## Listas
se utilizaron listas para almacenar los valores acumulados de cada iteración durante la simulación. Se crearon tres listas: pesos, momentos y centros_gravedad. Cada vez que el usuario ingresaba un nuevo elemento (pasajero, carga o combustible), el programa calculaba el peso total, el momento total y el centro de gravedad, y luego añadía esos valores a sus respectivas listas. Esto permitió registrar la evolución de los datos paso a paso, en lugar de sobrescribirlos como ocurría en el código original.
## Diccionario
se utilizó un diccionario llamado resumen para agrupar las tres listas en una sola estructura. Este diccionario contiene tres claves: "pesos", "momentos" y "centros_gravedad", cada una asociada a su lista correspondiente. Al final de la simulación, el diccionario se imprime para mostrar todos los datos acumulados. El uso del diccionario facilita la visualización conjunta de los resultados y permite acceder fácilmente a cada conjunto de datos por su nombre.


