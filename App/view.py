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
import webbrowser
from DISClib.ADT import list as lt
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
listLocations=None
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.init()
        controller.loadData(cont,'UFOS-utf8-small.csv') 

    elif int(inputs[0]) == 2:
        nombre= input("Escriba el nombre de la ciudad: ")
        print("========== Req No. 1 Inputs ==========\n" + "UFO Sighting in the city of: " + str(nombre))
        print("\n")
        
        rta=controller.requerimiento_1(nombre,cont)
        print("========== Req No. 1 Answer ==========\n" + "There are "+str(rta[3])+" different cities with UFO sightings...\n")
        print("The city with most UFO sightings is: ")
        listToTable = rta[0]
        table = t.createTable(listToTable,False)
        print(table)

    elif int(inputs[0]) == 3:
        rangeMin= float(input("Limite inferior (en segundos): "))
        rangeMax= float(input("Limite superior (en segundos): "))
        print("========== Req No. 2 Imputs ==========\n")
        print('UFO sightings between '+str(rangeMin)+ ' and '+str(rangeMax)+'\n')
        print("\n")
        
        rta = controller.requerimiento_2(cont,rangeMin,rangeMax)
        print('========== Req No. 2 Answer ==========\n')
        print('There are '+str(rta[3])+' different durations of UFO sightings...\n')
        listToTable = rta[0]
        table = t.createTable(listToTable)
        print('The TOP 5 durations with longest UFO sightings are: \n'+str(table))
        pass

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
        print("======================================Req. No 4 Inputs======================================")
        print("UFO sightings between {} and {}".format(rangeMin,rangeMax))
        rta = controller.requerimiento_4(cont,rangeMin,rangeMax)
        total = rta[3]
        variableName = 'date'
        print("======================================Req. No 4 Answers======================================")
        print("There are {} different UFO sightings dates [YYYY-M-DD]…. \nThe oldest UFO sightings date is: ".format(total))        
        print(t.simpleTable(rta[1],rta[2],variableName))
        listToTable = rta[0]
        table = t.createTable(listToTable,False)
        print(table)

    elif int(inputs[0]) == 6:
        latMin = float(input("Latitud mínima: ") )
        latMax = float(input("Latitud máxima: ") )
        longMin = float(input("Longitud mínima: ") )
        longMax = float(input("Longitud máxima: ") )
        rta = model.searchLocation(cont,latMin,latMax,longMin,longMax)
        listLocations = rta[0]
        table = t.createTable(listLocations,True)
        print(table)
        print(rta[1])
    
    elif int(inputs[0]) == 7:
        if listLocations==None:
            print("Ejecute primero la opción 6")
        else:
            model.bono(listLocations)
            webbrowser.open("Docs\\Mapas\\mapa.html")

    else:
        sys.exit(0)

