"""
Alumno: Alfredo Gaspar Contreras
Matricula: 202512146
Materia: Programacion Basica
Fecha: 08 de Noviembre 2025

PROGRAMA 3 — Calificaciones de un grupo (Arreglos bidimensionales y operaciones básicas) 

Contexto 
    Un docente quiere registrar las calificaciones de sus alumnos en tres evaluaciones y 
    calcular el promedio general. 

Requerimientos 
    1. Crea una lista bidimensional (lista de listas) donde cada fila contenga: 
            [nombre_alumno, cal1, cal2, cal3]. 
    2. Permite ingresar datos de al menos 10 alumnos. 
    3. Calcula y muestra: 
            o El promedio individual de cada alumno. 
            o El promedio general del grupo. 
            o La lista de alumnos aprobados y reprobados (considera 6 como calificación mínima aprobatoria). 
    4. Usa funciones para organizar tu programa: 
            o capturar_datos() 
            o mostrar_resultados() 
            o calcular_promedios() 

Salida esperada 
    Alumno: Ana  → Promedio: 8.3  
    Alumno: Luis → Promedio: 5.6  
    Alumno: Marta → Promedio: 9.0  
    Promedio general del grupo: 7.6 
    Aprobados: 2 
    Reprobados: 1

"""

import os
from datetime import datetime
from time import strftime
import readchar

lista_alumnos = []

# crea el menú de opciones como una lista
menu = [
    '[1] Ingresar datos de alumnos',
    '[2] Calcular promedios',
    '[3] salir'
    ]


def limpia_pantalla():
    """Limpia la pantalla de la consola dependiendo del sistema operativo."""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:                # Para Linux, macOS, y otros sistemas Unix
        os.system('clear')


def valida_opcion_menu(mensaje, opciones):
    valor = input("opcion---> ")
    while (not valor.isdigit()) or (int(valor) > opciones) or (int(valor) < 1):
        print(mensaje)
        print()
        valor = input("opcion---> ")
        print()
    return int(valor)


def despliega_menu(menu, opciones):
    limpia_pantalla()
    for i in range(opciones):
        print(menu[i])
    print()
    opcion_elegida = valida_opcion_menu(f"Las opciones válidas son del 1 al {opciones}. Por favor vuelva a intentar", opciones)
    print (f"regreso: {opciones}")
    return opcion_elegida


def presiona_tecla():
    print("Presiona cualquier tecla para continuar...")
    print()
    readchar.readkey()
    limpia_pantalla()


def es_float(valor):
    '''Valida que una cadena leída sea un número flotante.'''
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
def despliega_lista_promedios (alumnos):
    promedio_general = 0
    aprobados = 0
    reprobados = 0
    for i in range (len(alumnos)):
        promedio = 0
        
        print ()
        print (f"Estudiante: {i+1}")
        print ( "===============")
        print (f"nombre: {alumnos[i][0]}")
        for j in range (len (alumnos[i])):
            if j >= 1 :
                print (f"calificacion {j}: {alumnos[i][j]}")
                promedio = alumnos[i][j] + promedio
        promedio = promedio / 3
        promedio_general = promedio + promedio_general
        print (f"promedio individual --> {promedio}")
        if promedio > 6 :
            print ("<<<APROBADO>>>")
            aprobados = aprobados+1
        else :
            print ("<<<REPROBADO>>>")
            reprobados = reprobados+1
        print ()
    if len(alumnos)>0:
        print (f"promedio general del grupo --> {promedio_general/len(alumnos)}")
        print (f"total de aprobados:  {aprobados}")
        print (f"total de reprobados: {reprobados}")
    print ()

def captura_datos (alumnos):
    nombre_alumno = "Jhon Doe"
    nuevo_alumno = []
    numero_minimo_alumnos = 0
    while nombre_alumno != "" and (numero_minimo_alumnos < 10):
        nuevo_alumno = []
        print ()
        print("para terminar introduzca <ENTER> en Alumno")
        print ()
        nombre_alumno = input("Alumno               ---> ")
        if nombre_alumno != "": 
            nuevo_alumno.append(nombre_alumno)
            for i in range(3):
                calificacion = input("    calificacion (solo números)  ---> ")
                while not es_float(calificacion):
                    calificacion = input(f"    calificacion{i} (solo números)  ---> ")
                nuevo_alumno.append(float(calificacion))
            lista_alumnos.append(nuevo_alumno)
            numero_minimo_alumnos =+1
    if numero_minimo_alumnos < 10:
        print ("Es necesario tener al menos 10 alumnos. Para capturar mas alumnos favor de volver a entrar a la opcion 1.")
    #print (lista_alumnos)
    return lista_alumnos


# Programa principal
opcion_elegida = 99  # asegura que la primera vez se ejecute el ciclo while
while opcion_elegida != 3:
    opcion_elegida = despliega_menu(menu, 3)
    limpia_pantalla()

    match opcion_elegida:
        case 1:
            datos_alumno = captura_datos (lista_alumnos)
            lista_alumnos = datos_alumno
            print ()
            presiona_tecla ()
        case 2:
            despliega_lista_promedios (lista_alumnos)
            print ()
            presiona_tecla()
        case 3:
            print("Saliendo del programa...")



