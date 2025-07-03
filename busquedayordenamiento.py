import random
import time

# Bubble Sort para ordenar el inventario de productos
def bubble_sort(productos):
    n = len(productos)
    # Recorre toda la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Compara producto actual con el siguiente
            if productos[j] > productos[j + 1]:
                # Si están en desorden, intercambia
                productos[j], productos[j + 1] = productos[j + 1], productos[j]
    return productos

# Insertion Sort para ordenar el inventario
def insertion_sort(productos):
    # Empieza desde el segundo elemento
    for i in range(1, len(productos)):
        clave = productos[i]
        j = i - 1
        # Mueve los elementos mayores que clave una posición adelante
        while j >= 0 and clave < productos[j]:
            productos[j + 1] = productos[j]
            j -= 1
        productos[j + 1] = clave
    return productos

# Búsqueda binaria para encontrar un producto específico
def busqueda_binaria(productos, objetivo):
    inicio = 0
    fin = len(productos) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if productos[medio] == objetivo:
            return medio  # Devuelve el índice del producto
        elif productos[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1  # Producto no encontrado

# Función para medir el tiempo de ejecución
def medir_tiempo(func, productos):
    inicio = time.time()
    func(productos)
    fin = time.time()
    return fin - inicio

# =========================
# SIMULACIÓN DEL CASO PRÁCTICO
# =========================

# Simulamos un inventario con códigos numéricos aleatorios
productos_chicos = [random.randint(1000, 9999) for _ in range(10)]
productos_grandes = [random.randint(1000, 9999) for _ in range(5000)]

print("Inventario pequeño original (10 productos):")
print(productos_chicos)

# Ordena el inventario con Bubble Sort
tiempo_bubble = medir_tiempo(bubble_sort, productos_chicos.copy())
print(f"Inventario ordenado con Bubble Sort: {productos_chicos}")
print(f"Tiempo tomado con Bubble Sort: {tiempo_bubble:.6f} segundos\n")

# Ordena el inventario con Insertion Sort
tiempo_insertion = medir_tiempo(insertion_sort, productos_chicos.copy())
print(f"Inventario ordenado con Insertion Sort: {productos_chicos}")
print(f"Tiempo tomado con Insertion Sort: {tiempo_insertion:.6f} segundos\n")

# Ahora probamos con inventario grande
print("Inventario grande original (5000 productos). Ordenando...\n")

tiempo_bubble_grande = medir_tiempo(bubble_sort, productos_grandes.copy())
print(f"Tiempo Bubble Sort inventario grande: {tiempo_bubble_grande:.6f} segundos")

tiempo_insertion_grande = medir_tiempo(insertion_sort, productos_grandes.copy())
print(f"Tiempo Insertion Sort inventario grande: {tiempo_insertion_grande:.6f} segundos\n")

# Realiza búsqueda binaria en el inventario ordenado
productos_grandes_ordenados = insertion_sort(productos_grandes.copy())
producto_buscado = productos_grandes_ordenados[2500]  # Elegimos un producto existente
indice = busqueda_binaria(productos_grandes_ordenados, producto_buscado)

if indice != -1:
    print(f"Producto {producto_buscado} encontrado en posición {indice} del inventario ordenado.")
else:
    print(f"Producto {producto_buscado} no encontrado en el inventario.")

