"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import model
from DISClib.ADT import orderedmap as om
import textwrap
from tabulate import tabulate
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""




def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por Hora/Minutos del día")

catalog = None

"""
Menu principal
"""

def launchMenu():
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            cont = controller.init()
            controller.loadData(cont,'UFOS-utf8-small.csv') 

        elif int(inputs[0]) == 2:
            nombre= input("Escriba el nombre de la ciudad: ")
            print(nombre)
            rta=controller.requerimiento_1(nombre,cont)
            listToTable = rta[0]
            listTable = rta[1]
            table = createTable(listToTable,listTable)
            print(table)


        elif int(inputs[0]) == 3:
            rangeMin= float(input("Limite inferior (en segundos): "))
            rangeMax= float(input("Limite superior (en segundos): "))
            rta = controller.requerimiento_2(cont,rangeMin,rangeMax)
            listToTable = rta[0]
            listTable = rta[1]
            table = createTable(listToTable,listTable)
            print(table)

        elif int(inputs[0]) == 4:
            rangeMin= input("Límite inferior en formato HH: MM. ")
            rangeMax= input("Límite superior en formato HH: MM. ")
            rta=controller.requerimiento_3(cont,rangeMin,rangeMax)
            listToTable = rta[0]
            listTable = rta[1]
            table = createTable(listToTable,listTable)
            print(table)

        elif int(inputs[0]) == 5:
            rangeMin = input("Límite inferior en formato AAAA-MM-DD: ") 
            rangeMax = input("Límite inferior en formato AAAA-MM-DD: ") 
            rta = controller.requerimiento_4(cont,rangeMin,rangeMax)
            listToTable = rta[0]
            listTable = rta[1]
            table = createTable(listToTable,listTable)
            print(table)
        else:
            sys.exit(0)

#CREACIÓN DE TABLAS
def distribuir(elemento,cantidad):
    str_distribuido = '\n'.join((textwrap.wrap(elemento,cantidad)))
    return str_distribuido

def chkUnknown(origen,clave):
    if origen[clave]==None or origen[clave]=='' or origen[clave]==5000 or origen[clave]=='2100-12-24': return 'Unknown' #El 5000 se pone para compensar una de las funciones de comparación de años.
    else: return origen[clave]
def selectInfo(position,ListArtworks,FilteredList):
#       ↓↓↓ Todo este montón de líneas se encargan de sacar la info. necesaria del diccionario grande y con textwrap lo separa en líneas de un igual tamaño.
        artwork = lt.getElement(ListArtworks,position)

        datetime = artwork['datetime']
        city=distribuir(chkUnknown(artwork,'city'),20)
        state=distribuir(chkUnknown(artwork,'state'),10)
        country=distribuir(chkUnknown(artwork,'country'),20)
        shape=distribuir(chkUnknown(artwork,'shape'),20)
        duration_seconds=distribuir(chkUnknown(artwork,'duration (seconds)'),15)

#       Se crea una lista con todo lo que pide el requerimiento.

        artwork_entrega = [datetime,city,state,country,shape,duration_seconds]


#       Se pone un nuevo registro con la info de cada obra en la lista grande declarada al inicio.
        FilteredList.append(artwork_entrega)

def createTable(filteredList,listTable):
    for position in range(1,4):
        selectInfo(position,filteredList,listTable)
    for position in range(lt.size(filteredList)-2,lt.size(filteredList)+1):
        selectInfo(position,filteredList,listTable)

    headers = ['datetime','city','state','country','shape','duration (seconds)']

    table = tabulate(listTable,headers=headers,numalign='right',tablefmt='grid') 
    return table
#↑↑↑ Termina el formatting de las tablas ↑↑↑

launchMenu()