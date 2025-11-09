"""
Alumno: Alfredo Gaspar Contreras
Matricula: 202512146
Materia: Programacion Basica
Fecha: 08 de Noviembre 2025

PROGRAMA 2 — Analizador de texto (Manejo de cadenas) 

Contexto 
    En una empresa de marketing, se necesita analizar textos de los clientes para 
    conocer su extensión y la frecuencia de ciertas palabras. 
    
    Requerimientos 
            1. Solicita al usuario una cadena de texto (puede ser una opinión o comentario). 
            2. Realiza las siguientes operaciones: 
                    o Cuenta cuántas palabras y caracteres tiene. 
                    o Convierte el texto a mayúsculas y minúsculas. 
                    o Reemplaza una palabra por otra (por ejemplo, cambiar “malo” por “bueno”). 
                    o Cuenta cuántas veces aparece una palabra específica (por ejemplo, “gracias”). 
            3. Muestra los resultados en pantalla con formato claro. 

Salida esperada 
    Texto ingresado: Me gusta el servicio, gracias por la atención. 
    Número de palabras: 8 
    Número de caracteres: 43 
    Versión en mayúsculas: ME GUSTA EL SERVICIO, GRACIAS POR LA ATENCIÓN. 
    La palabra 'gracias' aparece 1 vez.

"""

import os
from datetime import datetime
from time import strftime
import readchar

# crea el menú de opciones como una lista
menu = [
    '[1] Introducir cadena de texto.',
    '[2] Contar palabras.',
    '[3] Convertir texto (minusculas <=> MAYUSCULAS).',
    '[4] Reemplazar palabra',
    '[5] Contar apariciones de una palabra',
    '[6] salir'
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

def introduce_cadena_texto ():
    cadena_texto = input ("Texto               ---> ")
    return (cadena_texto, cadena_texto.split())

def reemplaza_palabra (cadena_texto_palabras):
    encontrada = False
    numero_de_reemplazos = 0
    palabra_a_reemplazar = input("Que palabra quieres cambiar         ---> ")
    palabra_de_reemplazo = input("Por cual palabra la quieres cambiar ---> ")
    for i in range(len(cadena_texto_palabras)):
        if palabra_a_reemplazar == cadena_texto_palabras [i]:
            cadena_texto_palabras [i] = palabra_de_reemplazo
            encontrada = True
            numero_de_reemplazos +=1
        
    if encontrada:
        cadena_texto_original = " ".join(cadena_texto_palabras)
        print ()
        print (f"la palabra:    '{palabra_de_reemplazo}' se reemplazo:    {numero_de_reemplazos} veces")
        print ()
        print (f"resultando en: '{cadena_texto_original}'")
    else:
        print ()
        print (f"la palabra:    '{palabra_a_reemplazar}' no fue encontrada en la cadena original:")
        print (f"la cadena original es: {cadena_texto_original}")
        print ()

def cuenta_palabras_especificas (cadena_texto_palabras):
    numero_de_apariciones = 0
    palabra_a_buscar = input("Que palabra quieres encontrar         ---> ")
    for i in range(len(cadena_texto_palabras)):
        if palabra_a_buscar == cadena_texto_palabras [i]:
            numero_de_apariciones +=1
    print ()
    print (f"la palabra:    '{palabra_a_buscar}' aparece:    {numero_de_apariciones} veces")
    print ()

# Programa principal
opcion_elegida = 99  # asegura que la primera vez se ejecute el ciclo while
while opcion_elegida != 6:
    opcion_elegida = despliega_menu(menu, 6)
    limpia_pantalla()

    match opcion_elegida:
        case 1:
            texto = introduce_cadena_texto ()
            cadena_texto_original , cadena_texto_palabras = texto
            print ()
            print (f"la cadena de texto introducida fue:\n\n{cadena_texto_original}")
            print ()
            presiona_tecla ()
        case 2:
            print(f"numero de palabras:     {len(cadena_texto_palabras)}")
            cadena_sin_espacios = cadena_texto_original.replace (" ", "")
            print(f"numero de caracteres:   {len(cadena_sin_espacios)}")
            print ()
            presiona_tecla()
        case 3:
            cadena_texto_mayusculas = cadena_texto_original.upper ()
            cadena_texto_minusculas = cadena_texto_original.lower ()
            print(f"Cadena de texto en MAYUSCULAS:   {cadena_texto_mayusculas}")
            print(f"Cadena de texto en minusculas:   {cadena_texto_minusculas}")
            print ()
            presiona_tecla()
        case 4:
            reemplaza_palabra(cadena_texto_palabras)
            print ()
            presiona_tecla()
        case 5:
            cuenta_palabras_especificas(cadena_texto_palabras)
            print ()
            presiona_tecla()
        case 6:
            print("Saliendo del programa...")



