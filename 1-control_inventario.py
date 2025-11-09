"""

Alumno: Alfredo Gaspar Contreras
Matricula: 202512146
Materia: Programacion Basica
Fecha: 08 de Noviembre 2025

PROGRAMA 1 — Control de inventario (Arreglos unidimensionales y búsqueda/ordenamiento)

Contexto
Una tienda desea mantener un control básico de su inventario.
Cada producto tiene un nombre y un precio. El programa debe permitir registrar,
ordenar y buscar productos.

Requerimientos
1. Crea dos listas paralelas:
        1.1 productos (nombres de los productos)
        1.2 precios (precio correspondiente a cada producto)
2. Permite al usuario:
        2.1 Registrar al menos 15 productos con sus precios.
        2.2 Mostrar los productos ordenados alfabéticamente (usa Bubble Sort o Selection Sort).
        2.3 Buscar un producto por nombre usando búsqueda lineal.
3. Muestra el resultado de la búsqueda y el listado ordenado:
        3.1 Salida esperada
                Inventario ordenado:
                ['Café' , 'Harina' , 'Leche' , 'Pan' , 'Sal']
                Buscar producto: Leche
                Precio: 24.5
"""

import os
from datetime import datetime
from time import strftime
import readchar

# crea el menú de opciones como una lista
menu = ['[1] Registrar productos.','[2] Ordenar productos.','[3] Buscar un producto.','[4] Salir']


# listas paralelas
productos = []
precios = []


def limpia_pantalla():
    """Limpia la pantalla de la consola dependiendo del sistema operativo."""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:                # Para Linux, macOS, y otros sistemas Unix
        os.system('clear')


def es_float(valor):
    '''Valida que una cadena leída sea un número flotante.'''
    try:
        float(valor)
        return True
    except ValueError:
        return False


def valida_opcion_menu(mensaje,opciones):
    valor = input("opcion---> ")
    while (not valor.isdigit()) or (int(valor) > opciones) or (int(valor) < 1):
        print(mensaje)
        print()
        valor = input("opcion---> ")
    return int(valor)


def despliega_menu(menu, opciones):
    limpia_pantalla()
    print()
    for i in range(opciones):
        print(menu[i])
    print()
    opcion_elegida = valida_opcion_menu(f"Las opciones válidas son del 1 al {opciones}. Por favor vuelva a intentar",opciones)
    return opcion_elegida


def presiona_tecla():
    ''' Esta funcion solo espera a que el usuario tecle cualquier caracter para continuar con el flujo del programa'''
    print("Presiona cualquier tecla para continuar...")
    print()
    readchar.readkey()
    limpia_pantalla()


def lee_listas_paralelas(lista1, lista2, mensaje):
    articulo = "nada"
    while articulo != "":
        print(mensaje)
        articulo = input(".    articulo               ---> ")
        if articulo != "":
            lista1.append(articulo)
            precio = "a"
            while not es_float(precio) and articulo != "":
                precio = input(".    precio (solo números)  ---> ")
                if es_float(precio):
                    lista2.append(precio)
    return lista1, lista2


def despliega_inventario(productos, precios):
    print()
    print("=========== Listado de productos ordenados - inicio ============")
    for i in range(len(productos)):
        print(f"{i+1}) producto: {productos[i]} , precio: {precios[i]}")
    print("=========== Listado de productos ordenados - fin ============")
    print()


def selection_sort(lista1, lista2):
    for i in range(len(lista1) - 1):
        min_value_position = i
        for j in range(i + 1, len(lista1)):
            if lista1[j] < lista1[min_value_position]:
                min_value_position = j
        if min_value_position != i:
            temp_producto = lista1[i]
            temp_precio = lista2[i]
            lista1[i] = lista1[min_value_position]
            lista1[min_value_position] = temp_producto
            lista2[i] = lista2[min_value_position]
            lista2[min_value_position] = temp_precio
    return lista1, lista2


def busqueda_lineal(elemento, lista1):
    for i in range(len(lista1)):
        if lista1[i] == elemento:
            return i, True
    return None, False


def busca_producto(mensaje):
    articulo = "nada"
    while articulo != "":
        print(mensaje)
        articulo = input(".    articulo               ---> ")
        if articulo != "":
            indice, encontrado = busqueda_lineal(articulo, productos)
            print()
            if encontrado:
                print(f"El artículo buscado es: {productos[indice]} y su precio es: {precios[indice]}")
            else:
                print("El artículo no se encuentra en la lista.")
            print()


# Programa principal
opcion_elegida = 99  # asegura que la primera vez se ejecute el ciclo
while opcion_elegida != 4:
    opcion_elegida = despliega_menu(menu, 4)
    limpia_pantalla()

    match opcion_elegida:
        case 1:
            lee_listas_paralelas(productos, precios, "Para terminar, teclea Enter en producto. Recuerda que el precio debe ser numérico.")
        case 2:
            productos, precios = selection_sort(productos, precios)
            despliega_inventario(productos, precios)
            presiona_tecla()
        case 3:
            busca_producto("Teclea el nombre del producto o presiona Enter para terminar.")
            presiona_tecla()
        case 4:
            print("Saliendo del programa...")


