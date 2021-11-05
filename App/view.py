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
import model
import config as cf
import sys
import controller
assert cf
import tabless as t
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
    print("5- Contar avistamientos en un rango de fechas")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.init()
        controller.loadData(cont,'UFOS-utf8-large.csv') 

    elif int(inputs[0]) == 2:
        nombre= input("Escriba el nombre de la ciudad: ")
        print(nombre)
        rta=controller.requerimiento_1(nombre,cont)
        listToTable = rta[0]
        table = t.createTable(listToTable,False)
        print(table)

    elif int(inputs[0]) == 3:
        rangeMin= float(input("Limite inferior (en segundos): "))
        rangeMax= float(input("Limite superior (en segundos): "))
        rta = controller.requerimiento_2(cont,rangeMin,rangeMax)
        listToTable = rta[0]
        table = t.createTable(listToTable)
        print(table)

    elif int(inputs[0]) == 4:
        rangeMin= input("Límite inferior en formato HH: MM. ")
        rangeMax= input("Límite superior en formato HH: MM. ")
        rta=controller.requerimiento_3(cont,rangeMin,rangeMax)
        listToTable = rta[0]
        table = t.createTable(listToTable,False)
        print(table)

    elif int(inputs[0]) == 5:
        rangeMin = input("Límite inferior en formato AAAA-MM-DD: ") 
        rangeMax = input("Límite inferior en formato AAAA-MM-DD: ") 
        rta = controller.requerimiento_4(cont,rangeMin,rangeMax)
        listToTable = rta[0]
        table = t.createTable(listToTable,False)
        print(table)

    elif int(inputs[0]) == 6:
        latMin = float(input("Latitud mínima: ") )
        latMax = float(input("Latitud máxima: ") )
        longMin = float(input("Longitud mínima: ") )
        longMax = float(input("Longitud máxima: ") )
        rta = model.searchLocation(cont,latMin,latMax,longMin,longMax)
        listToTable = rta[0]
        table = t.createTable(listToTable,True)
        print(table)
        print(rta[1])
    else:
        sys.exit(0)

