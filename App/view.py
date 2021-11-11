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
    print("\nBienvenido! ")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por Hora/Minutos del día")
    print("5- Contar avistamientos en un rango de fechas")
    print("6- Contar avistamientos en una zona geográfica")
    print("7- Visualizar avistamientos en una zona geográfica")
    print("0- Salir")

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
        controller.loadData(cont,'UFOS-utf8-large.csv') 

    elif int(inputs[0]) == 2:
        nombre= input("Escriba el nombre de la ciudad: ")
        print("========== Req No. 1 Inputs ==========\n" + "UFO Sighting in the city of: " + str(nombre))
        print("\n")
        rta=controller.requerimiento_1(nombre,cont)

        print("========== Req No. 1 Answer ==========\n" + "There are "+str(rta[3])+" different cities with UFO sightings...\n")
        print("The city with most UFO sightings is: {}".format(rta[4]))

        print("There are {} sightings at the: {} city".format(rta[2],nombre))
        listToTable = rta[0]
        table = t.createTable(listToTable,False)
        print(table)

    elif int(inputs[0]) == 3:
        rangeMin= float(input("Limite inferior (en segundos): "))
        rangeMax= float(input("Limite superior (en segundos): "))
        print("========== Req No. 2 Inputs ==========\n")
        print('UFO sightings between '+str(rangeMin)+ ' and '+str(rangeMax)+'\n')
        print("\n")
        
        rta = controller.requerimiento_2(cont,rangeMin,rangeMax)

        print('========== Req No. 2 Answer ==========\n')
        print('There are '+str(rta[3])+' different durations of UFO sightings...\n')
        listToTable = rta[0]
        variableName = 'time'
        print('The longest UFO sightings are: \n')
        print(t.simpleTable(rta[1],rta[2],variableName))
        table = t.createTable(listToTable,None  )
        print('There are '+str(rta[4])+' sightings between: '+str(rangeMin)+ ' and '+str(rangeMax)+'\n')
        print('The first 3 and last 3 UFO sightings in the duration time are: \n'+str(table))
        pass

    elif int(inputs[0]) == 4:
        rangeMin= input("Límite inferior en formato HH: MM. ")
        rangeMax= input("Límite superior en formato HH: MM. ")
        print('========== Req No. 3 Inputs ==========\n')
        print('UFO sightings between '+str(rangeMin)+' and '+ str(rangeMax)+'\n')
        rta=controller.requerimiento_3(cont,rangeMin,rangeMax)
        variableName = 'time'
        listToTable = rta[0]
        table = t.createTable(listToTable,'time')
        print('========== Req No. 3 Answer ==========\n')
        print('There are '+str(rta[3])+' UFO sightings with different time [hh:mm:ss]...\n')
        print('The latest UFO sightings time is: \n')
        print(t.simpleTable(rta[1],rta[2],variableName))
        print('There are '+str(rta[4])+' sightings between: '+str(rangeMin)+ ' and '+str(rangeMax)+'\n')
        print('The first 3 and last 3 UFO sightings in this time are: \n'+table)
        


    elif int(inputs[0]) == 5:
        rangeMin = input("Límite inferior en formato AAAA-MM-DD: ") 
        rangeMax = input("Límite inferior en formato AAAA-MM-DD: ") 
        print("+======================================Req. No 4 Inputs======================================+\n")
        print("UFO sightings between {} and {}".format(rangeMin,rangeMax))
        rta = controller.requerimiento_4(cont,rangeMin,rangeMax)
        total = rta[3]
        total_range = rta[4]
        listToTable = rta[0]
        variableName = 'date'
        print("\n+======================================Req. No 4 Answers======================================+\n")
        print("There are {} UFO sightings with different dates [YYYY-MM-DD]…. \nThe oldest UFO sightings date is: ".format(total))        
        print(t.simpleTable(rta[1],rta[2],variableName))
        print("\nThere are {} sightings between: {} and {}".format(total_range,rangeMin,rangeMax))
        print("The first 3 and last 3 UFO sightings in this time are:\n")
        table = t.createTable(listToTable,'date')
        print(table)

    elif int(inputs[0]) == 6:
        latMin = float(input("Latitud mínima: ") )
        latMax = float(input("Latitud máxima: ") )
        longMin = float(input("Longitud mínima: ") )
        longMax = float(input("Longitud máxima: ") )
        print("+======================================Req. No 5 Inputs======================================+\n")
        print("UFO sightings between latitude {} and {}".format(latMin,latMax))
        print("plus longitude range of {} and {}".format(longMin,longMax))
        rta = model.searchLocation(cont,latMin,latMax,longMin,longMax)
        listLocations = rta[0]
        numElem =rta[1]
        print("\n+======================================Req. No 5 Answers======================================+\n")
        print("There are {} different UFO sightings in the current area".format(numElem))
        table = t.createTable(listLocations,'Location')
        print("The first 3 and last 3 UFO sightings in this area are: \n")
        print(table)
        
    
    elif int(inputs[0]) == 7:
        if listLocations==None:
            print("Ejecute primero la opción 6")
        else:
            model.bono(listLocations)
            webbrowser.open("Docs\\Mapas\\mapa.html")

    else:
        sys.exit(0)

